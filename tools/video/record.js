// Quay các cảnh Gym God trong Chromium riêng cho từng cảnh.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { createRequire } = require('node:module');

process.env.PLAYWRIGHT_BROWSERS_PATH ??= '0';
const { chromium } = createRequire(path.join(__dirname, '../qa/package.json'))('playwright');

const project = path.resolve(__dirname, '../..');
const raw = path.join(__dirname, 'raw');
const origin = 'http://127.0.0.1:8766';

function setup(options) {
  closeGuide();
  s = Object.assign(fresh(), {
    lang: 'en',
    clicks: 500,
    vm: 0,
    vs: 0,
    tips: Object.fromEntries([...GUIDE.map(([key]) => [key, 1]), ['firstBuy', 1]]),
    ach: Object.fromEntries(ACH.map(({ id }) => [id, 1])),
  }, options);
  s.lv = { ...fresh().lv, ...options.lv };
  shown = s.rk;
  syncRank(true);
  s.cap = s.sta = staMax();
  go(s.scene);
}

async function tapHero(page, count, gap) {
  const hero = await page.locator('#art').boundingBox();
  const offsets = [-.07, .06, 0, .09, -.04, .03];
  for (let i = 0; i < count; i++) {
    await page.mouse.click(hero.x + hero.width * (.5 + offsets[i % offsets.length]),
      hero.y + hero.height * (.54 + offsets[(i + 2) % offsets.length]));
    await page.waitForTimeout(gap);
  }
}

const scenes = {
  workout: {
    setup: { scene: 'office', day: 1, seen: 3, lv: { tay: 4, vai: 4, nguc: 2 } },
    async play(page, mark) {
      const start = mark();
      await page.waitForTimeout(560);
      await page.locator('#go').click();
      await page.waitForFunction(() => s.scene === 'gym' && !moving);
      await page.waitForTimeout(180);
      await tapHero(page, 12, 135);
      const arms = page.locator('#list .buy[data-i="0"]');
      const rankUp = mark();
      await arms.click();
      await page.waitForFunction(() => s.rk === 1 && $('pic').src.endsWith('/rank2.webp'));
      await page.waitForTimeout(600);
      await tapHero(page, 10, 130);
      await page.waitForTimeout(950);
      return { start, rankUp, end: mark() };
    },
  },
  arena: {
    setup: { scene: 'gym', day: 8, kg: 84.5, seen: 5, met: { 0: 1 },
      lv: { tay: 22, vai: 18, nguc: 14, bung: 8, mat: 3 } },
    async play(page, mark) {
      await page.locator('#tabDuel').click();
      const versus = mark();
      await page.locator('#rivals .buy[data-r="0"]').click();
      await page.waitForFunction(() => arena?.step === 'talk');
      // Bỏ phần hội thoại nằm giữa hai đoạn dựng. Đếm ngược và giao đấu vẫn chạy bình thường.
      await page.evaluate(() => next());
      await page.waitForFunction(() => $('aCount').textContent === '1');
      const fight = mark();
      await page.waitForFunction(() => arena?.step === 'fight');
      const area = await page.locator('#arena').boundingBox();
      for (let i = 0; i < 36 && !await page.evaluate(() => s.wins > 0); i++) {
        await page.mouse.click(area.x + area.width * .49, area.y + area.height * .53);
        await page.waitForTimeout(105);
      }
      assert.equal(await page.evaluate(() => s.wins), 1, 'Đoạn quay đấu trường phải kết thúc bằng trận thắng.');
      const win = mark();
      await page.waitForTimeout(250);
      await page.evaluate(() => next());
      await page.locator('#aBack').click();
      await page.waitForTimeout(1100);
      return { versus, fight, win, end: mark() };
    },
  },
  champion: {
    setup: { scene: 'gym', day: 30, seen: 8, wins: 14, stars: 6, kg: 77, cal: 120000000,
      lv: { tay: 70, vai: 60, nguc: 55, bung: 48, mat: 40, chan: 40, lung: 32, cardio: 20 } },
    async play(page, mark) {
      const start = mark();
      await page.waitForTimeout(540);
      await tapHero(page, 24, 115);
      await page.waitForTimeout(1100);
      return { start, end: mark() };
    },
  },
};

async function record(browser, batch, name, width, height, sceneName) {
  const context = await browser.newContext({
    viewport: { width, height },
    recordVideo: { dir: path.join(batch, 'captures'), size: { width, height } },
  });
  const missing = [];
  const errors = [];
  try {
    await context.route('**/*', async route => {
      const url = new URL(route.request().url());
      if (url.hostname === 'sdk.crazygames.com') {
        return route.fulfill({ contentType: 'application/javascript', body: '' });
      }
      if (url.origin !== origin) return route.abort();
      const name = url.pathname === '/' ? 'index.html' : url.pathname.slice(1);
      const file = path.join(project, name);
      if ((name !== 'index.html' && !/^assets\/[a-z]+\/[a-z0-9-]+\.(webp|mp3)$/.test(name)) || !fs.existsSync(file)) {
        missing.push(name);
        return route.fulfill({ status: 404 });
      }
      return route.fulfill({ path: file });
    });

    const start = performance.now();
    const mark = () => Number(((performance.now() - start) / 1000).toFixed(3));
    const page = await context.newPage();
    page.setDefaultTimeout(10000);
    page.on('pageerror', error => errors.push(error.message));
    const video = page.video();
    await page.goto(origin);
    await page.waitForFunction(() => typeof ready !== 'undefined' && ready);
    const scene = scenes[sceneName];
    await page.evaluate(setup, scene.setup);
    await page.waitForFunction(() => !$('pic').hidden && $('pic').src.endsWith('rank' + (s.rk + 1) + '.webp'));
    await page.waitForTimeout(450);
    const marks = await scene.play(page, mark);
    await context.close();
    assert.deepEqual(missing, []);
    assert.deepEqual(errors, []);
    const file = path.join(batch, name + '-' + sceneName + '.webm');
    await video.saveAs(file);
    await video.delete();
    console.log(name, sceneName, marks);
    return { file: path.relative(raw, file), ...marks };
  } finally {
    await context.close();
  }
}

async function main() {
  fs.mkdirSync(raw, { recursive: true });
  const batch = fs.mkdtempSync(path.join(raw, 'trailer-'));
  const browser = await chromium.launch();
  try {
    const manifest = {};
    for (const [name, width, height] of [['land', 1280, 720], ['port', 720, 1080]]) {
      const takes = manifest[name] = {};
      for (const scene of Object.keys(scenes)) {
        takes[scene] = await record(browser, batch, name, width, height, scene);
      }
    }
    fs.writeFileSync(path.join(raw, 'trailer-marks.json'), JSON.stringify(manifest, null, 2));
  } finally {
    await browser.close();
  }
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
