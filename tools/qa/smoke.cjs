const assert = require('node:assert/strict');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const vm = require('node:vm');
const { after, before, test } = require('node:test');

process.env.PLAYWRIGHT_BROWSERS_PATH ??= '0';
const installWebKit = process.argv.includes('--install-webkit');
const useWebKit = process.argv.includes('--webkit');
if (process.argv.includes('--install-browser') || installWebKit) {
  const cli = path.join(path.dirname(require.resolve('playwright/package.json')), 'cli.js');
  const targets = installWebKit ? ['webkit'] : ['--only-shell', 'chromium'];
  execFileSync(process.execPath, [cli, 'install', ...targets], { stdio: 'inherit' });
  return;
}
const { chromium, webkit } = require('playwright');

const project = path.resolve(__dirname, '../..');
const origin = 'http://127.0.0.1:8766';
const testZip = process.argv.includes('--zip');
const timeout = 12_000;
let browser;
let archiveRoot;

before(async () => {
  const current = fs.readFileSync(path.join(project, 'index.html'));
  const source = current.toString('utf8').match(/<script>([\s\S]*?)<\/script>/);
  assert.ok(source, 'Không tìm thấy JavaScript trong index.html.');
  new vm.Script(source[1], { filename: 'index.html' });
  if (testZip) {
    const zip = path.join(project, 'dist', 'gym-god.zip');
    assert.ok(fs.existsSync(zip), 'Tạo gói bằng python tools/dist.py trước khi chạy test:zip.');
    const temp = fs.realpathSync(os.tmpdir());
    archiveRoot = fs.mkdtempSync(path.join(temp, 'gym-god-qa-'));
    execFileSync('python', ['-m', 'zipfile', '-e', zip, archiveRoot], { stdio: 'inherit' });
    const packaged = fs.readFileSync(path.join(archiveRoot, 'index.html'));
    assert.ok(packaged.equals(current), 'ZIP chứa index.html cũ. Chạy lại python tools/dist.py.');
  }
  const executablePath = process.env.GYM_GOD_QA_CHROMIUM;
  browser = useWebKit ? await webkit.launch() : await chromium.launch(executablePath ? { executablePath } : {});
});

after(async () => {
  try {
    await browser?.close();
  } finally {
    if (archiveRoot) {
      assert.equal(path.dirname(fs.realpathSync(archiveRoot)), fs.realpathSync(os.tmpdir()));
      assert.match(path.basename(archiveRoot), /^gym-god-qa-/);
      fs.rmSync(archiveRoot, { recursive: true, force: true });
    }
  }
});

async function openGame(t) {
  const root = archiveRoot || project;
  const context = await browser.newContext({
    viewport: { width: 375, height: 812 },
    hasTouch: true,
    isMobile: true,
    reducedMotion: 'reduce',
  });
  const errors = [];
  const requests = new Set();
  t.after(async () => {
    await context.close();
    assert.deepEqual(errors, []);
  });

  await context.route('**/*', async route => {
    const url = new URL(route.request().url());
    if (url.hostname === 'sdk.crazygames.com') {
      // Chạy nhánh không có SDK với dữ liệu local của context này.
      return route.fulfill({ contentType: 'application/javascript', body: '' });
    }
    if (url.origin !== origin) return route.abort();
    const name = url.pathname === '/' ? 'index.html' : url.pathname.slice(1);
    const file = path.resolve(root, name);
    const allowed = name === 'index.html' || /^assets\/[a-z]+\/[a-z0-9-]+\.(webp|mp3)$/.test(name);
    if (!allowed || !fs.existsSync(file)) {
      errors.push('Thiếu tài nguyên: ' + name);
      return route.fulfill({ status: 404 });
    }
    requests.add(name);
    return route.fulfill({ path: file });
  });

  const page = await context.newPage();
  page.setDefaultTimeout(timeout);
  page.on('pageerror', error => errors.push(error.message));
  await page.goto(origin);
  await page.waitForFunction(() => typeof ready !== 'undefined' && ready);
  return { page, requests };
}

async function finishGuide(page) {
  const guide = page.locator('#guide');
  for (let i = 0; i < 10 && await guide.isVisible(); i++) {
    await page.locator('#gOk').tap();
  }
  assert.equal(await guide.isVisible(), false);
}

test('Chơi ngày đầu bằng cảm ứng, mua Tay và ngủ sang ngày 2', async t => {
  const { page } = await openGame(t);
  await page.locator('#gOk').waitFor();
  await finishGuide(page);
  await page.locator('#go').tap();
  await page.waitForFunction(() => s.scene === 'gym' && !moving);
  await finishGuide(page);

  const hero = page.locator('#hero');
  for (let i = 0; i < 13; i++) {
    await hero.tap();
    // Game giới hạn cú chạm thật cách nhau ít nhất 50 ms.
    await new Promise(resolve => setTimeout(resolve, 60));
  }
  const arms = page.locator('#list .buy[data-i="0"]');
  assert.equal(await arms.isEnabled(), true);
  assert.equal(await page.evaluate(() => s.tips.firstBuy), 1);
  await arms.tap();
  await page.waitForFunction(() => s.lv.tay === 1 && s.sta < s.cap);
  await page.locator('#goHome').tap();
  await page.locator('#mYes').tap();
  await page.waitForFunction(() => s.scene === 'home' && !moving);
  await finishGuide(page);
  await page.locator('#sleep').tap();
  await page.waitForFunction(() => s.day === 2 && s.scene === 'office' && !moving);
  assert.equal(await page.evaluate(() => s.sta === s.cap && s.lv.tay === 1), true);
});

test('Tải lại trước và sau thời điểm lưu buổi sáng, kể cả khi bản chính hỏng', async t => {
  const { page } = await openGame(t);
  await page.evaluate(() => {
    closeGuide();
    s = Object.assign(fresh(), { day: 5, kg: 84.8, kg1: 84.8, rk: 2, best: 2, cap: 540, sta: 0, used: 540 });
    shown = s.rk;
    EX.forEach((e, i) => { s.lv[e.k] = RANKS[3].goal[i]; });
    go('home');
  });
  await finishGuide(page);

  // Giữ đúng khung hình trước khi đổi ngày để phép thử không phụ thuộc tốc độ máy.
  await page.evaluate(() => {
    const sky = $('nightSky'), animate = sky.animate.bind(sky);
    sky.animate = (...args) => {
      const animation = animate(...args);
      animation.pause();
      return animation;
    };
  });
  await page.locator('#sleep').tap();
  await page.locator('#night').waitFor();
  await page.reload();
  await page.waitForFunction(() => ready && s.day === 5 && s.scene === 'home');

  // Lần này giữ hoạt ảnh sau khi ngày đã đổi, trước khi cửa mở.
  await page.evaluate(() => {
    const sky = $('nightSky'), animate = sky.animate.bind(sky);
    sky.animate = (...args) => {
      const animation = animate(...args);
      if (s.day === 6) animation.pause();
      return animation;
    };
  });
  await page.locator('#sleep').tap();
  await page.waitForFunction(() => s.day === 6);
  assert.equal(await page.locator('#frame').evaluate(el => el.classList.contains('home')), true);
  const snapshots = await page.evaluate(() => [KEY, BAK].map(key => {
    const saved = JSON.parse(localStorage.getItem(key));
    return [saved.day, saved.scene, saved.rk, saved.sta === saved.cap];
  }));
  assert.deepEqual(snapshots, [[6, 'office', 3, true], [6, 'office', 3, true]]);

  await page.evaluate(() => {
    ready = false; // Chặn pagehide tự ghi đè bản chính hỏng trong ca thử.
    localStorage.setItem(KEY, '{broken');
  });
  await page.reload();
  await page.waitForFunction(() => ready && s.day === 6 && s.scene === 'office' && s.rk === 3);
  await page.locator('#go').waitFor();
  assert.equal(await page.locator('#sleep').isVisible(), false);
});

test('Hoãn tải ảnh đối thủ đến khi mở Thi đấu và ngừng cập nhật thẻ ẩn', async t => {
  const { page, requests } = await openGame(t);
  const rivals = () => [...requests].filter(name => name.startsWith('assets/rival/'));
  const characters = () => [...requests].filter(name => name.startsWith('assets/char/')).sort();
  await page.waitForFunction(() => pics[0][0]?.ok && pics[0][1]?.ok);
  assert.deepEqual(characters(), ['assets/char/rank1.webp', 'assets/char/rank2.webp']);
  assert.equal(rivals().length, 0);
  assert.equal(await page.locator('#rivals .card').count(), 0);

  await page.evaluate(() => {
    closeGuide();
    s.kg = 84.5;
    EX.forEach((e, i) => { s.lv[e.k] = RANKS[3].goal[i]; });
    syncRank(true);
    go('gym');
  });
  await finishGuide(page);
  assert.equal(rivals().length, 0);
  await page.locator('#tabDuel').tap();
  await finishGuide(page);
  assert.equal(await page.locator('#rivals .card').count(), 30);
  const last = page.locator('#rivals .card img').last();
  await last.scrollIntoViewIfNeeded();
  await page.waitForFunction(() => {
    const image = $('rivals').querySelector('.card:last-child img');
    return image?.currentSrc.endsWith('/rival-30.webp') && image.naturalWidth > 0;
  });

  await page.locator('#tabEx').tap();
  const hiddenMutations = await page.evaluate(() => new Promise(resolve => {
    let count = 0;
    const observer = new MutationObserver(records => { count += records.length; });
    observer.observe($('rivals'), { subtree: true, attributes: true, childList: true, characterData: true });
    setTimeout(() => { observer.disconnect(); resolve(count); }, 550);
  }));
  assert.equal(hiddenMutations, 0);
});

test('Văn phòng và phòng tập vừa khung điện thoại, tablet và xoay ngang', async t => {
  const { page } = await openGame(t);
  await page.evaluate(() => {
    closeGuide();
    s.lang = 'vi'; s.day = 2; s.cal = 1450;
    s.tips = Object.fromEntries(GUIDE.map(([key]) => [key, 1]));
    Object.assign(s.lv, { tay: 5, vai: 4 });
    buildTexts();
  });
  for (const [width, height] of [[320, 510], [375, 610], [430, 755], [768, 1024], [812, 350], [1280, 720]]) {
    await page.setViewportSize({ width, height });
    await page.waitForFunction(height => innerHeight === height && Math.abs($('frame').clientHeight - height) <= 1, height);
    await page.evaluate(() => {
      s.rk = shown = 0; s.best = 0; s.fat = 0; s.ev = null; s.ch = null;
      go('office');
    });
    await page.waitForFunction(() => !$('pic').hidden && $('pic').src.endsWith('/rank1.webp'));
    assert.equal(await page.locator('#wk').isVisible(), false);
    const office = await page.evaluate(() => {
      const hero = $('hero').getBoundingClientRect(), pic = $('pic').getBoundingClientRect();
      const nav = $('nav').getBoundingClientRect();
      return { imageHeight: pic.height, offset: Math.abs((pic.left + pic.width / 2) - (hero.left + hero.width / 2)),
        navBottom: nav.bottom, scrollWidth: $('frame').scrollWidth };
    });
    assert.ok(office.imageHeight >= 90 && office.navBottom <= height + 1 && office.scrollWidth <= width + 1,
      width + 'x' + height + ' office: ' + JSON.stringify(office));
    if (width <= 900) assert.ok(office.offset <= 1, 'Ảnh văn phòng phải nằm giữa vùng nhân vật');

    await page.evaluate(() => {
      s.rk = shown = 4; s.best = 4; s.fat = 74; s.kg = 82;
      s.cap = s.sta = 760; s.ch = 'party';
      s.ev = 'boss';
      go('office');
    });
    assert.equal(await page.locator('#wk').isVisible(), true);
    assert.ok(await page.locator('#evA').isVisible() && await page.locator('#evB').isVisible());
    await page.evaluate(() => {
      CG = { data: localStorage, game: { settings: { muteAudio: true } } };
      go('gym');
    });
    assert.equal(await page.locator('#boost').isVisible(), true);
    await page.waitForFunction(() => $('pic').src.endsWith('/rank5.webp'));
    const gym = await page.evaluate(() => {
      const hero = $('hero').getBoundingClientRect(), pic = $('pic').getBoundingClientRect();
      const panel = document.querySelector('.panel').getBoundingClientRect();
      const list = $('list');
      return { imageHeight: pic.height, offset: Math.abs((pic.left + pic.width / 2) - (hero.left + hero.width / 2)),
        panelLeft: panel.left, heroRight: hero.right, listHeight: list.clientHeight, listWidth: list.clientWidth,
        listScrollWidth: list.scrollWidth,
        fullyVisible: Array.from(list.children).filter(card => card.getBoundingClientRect().bottom <= list.getBoundingClientRect().bottom).length };
    });
    assert.ok(gym.imageHeight >= 70 && gym.listHeight >= 100 && gym.listScrollWidth <= gym.listWidth + 1,
      width + 'x' + height + ' gym: ' + JSON.stringify(gym));
    if (width <= 900) assert.ok(gym.offset <= 1, 'Ảnh phòng tập phải nằm giữa vùng nhân vật');
    if (width === 375) assert.ok(gym.fullyVisible >= 2, JSON.stringify(gym));
    if (width > height) assert.ok(gym.panelLeft >= gym.heroRight - 1, 'Màn ngang đặt sổ tập cạnh sân khấu');
  }
});

test('Đổi nhân vật khi ảnh tải chậm hoặc bị thiếu giữ ảnh hợp lệ ở giữa', async t => {
  const { page } = await openGame(t);
  await page.setViewportSize({ width: 375, height: 610 });
  await page.evaluate(() => {
    closeGuide();
    s.tips = Object.fromEntries(GUIDE.map(([key]) => [key, 1]));
    go('gym');
  });
  await page.waitForFunction(() => !$('pic').hidden && $('pic').src.endsWith('/rank1.webp'));
  let finish;
  const held = new Promise(resolve => { finish = resolve; });
  await page.route('**/assets/char/c2-rank1.webp', async route => {
    await held;
    await route.fallback();
  });

  try {
    await Promise.all([page.waitForRequest('**/assets/char/c2-rank1.webp'), page.locator('#who').tap()]);
    assert.equal(await page.evaluate(() => s.char === 1 && !$('pic').hidden && $('pic').src.endsWith('/rank1.webp')), true);
    await page.locator('#who').tap();
    assert.equal(await page.evaluate(() => s.char), 0);
  } finally {
    finish();
  }
  await page.waitForFunction(() => pics[1][0]?.ok);
  assert.equal(await page.evaluate(() => $('pic').src.endsWith('/rank1.webp')), true);

  await page.locator('#who').tap();
  await page.waitForFunction(() => !$('pic').hidden && $('pic').src.endsWith('/c2-rank1.webp'));
  await page.route('**/assets/char/c2-rank4.webp', route => route.fulfill({ status: 404 }));
  await page.evaluate(() => {
    s.rk = shown = 3; s.best = 3;
    go('gym');
  });
  await page.waitForFunction(() => !$('pic').hidden && $('pic').src.endsWith('/c2-rank3.webp'));
  await page.reload();
  await page.waitForFunction(() => ready && s.scene === 'office' && s.char === 1
    && !$('pic').hidden && $('pic').src.endsWith('/c2-rank3.webp'));
  const offset = await page.evaluate(() => {
    const hero = $('hero').getBoundingClientRect(), pic = $('pic').getBoundingClientRect();
    return Math.abs((pic.left + pic.width / 2) - (hero.left + hero.width / 2));
  });
  assert.ok(offset <= 1, 'Ảnh dự phòng phải ở giữa sau khi tải lại');

  await page.route('**/assets/char/rank1.webp', route => route.fulfill({ status: 404 }));
  await page.evaluate(() => {
    s.char = 0; s.rk = shown = 0;
    save();
  });
  await page.reload();
  await page.waitForFunction(() => ready && pics[0][0]?.failed && $('pic').hidden && $('guy').hasChildNodes());
  assert.equal(await page.locator('#guy').isVisible(), true);
});
