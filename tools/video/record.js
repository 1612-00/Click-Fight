// Quay gameplay cho video xem trước CrazyGames. Chạy bằng Playwright MCP: browser_run_code_unsafe với filename = tools/video/record.js
// (cần server xem thử `game` đang chạy, và ffmpeg của Playwright: xem tools/video/build.py). Sau đó: python tools/video/build.py
// Mỗi cảnh một ngữ cảnh trình duyệt mới, bộ nhớ trống: không đụng bản lưu thật. Mốc bắt đầu/kết thúc (ms) ghi vào tên file.
async (page) => {
  const RAW = 'D:/Game/gym-god/tools/video/raw';   // build.py đọc ở đây
  const URL = 'http://127.0.0.1:8766/';
  const browser = page.context().browser();
  const wait = ms => new Promise(r => setTimeout(r, ms));
  // trạng thái dựng sẵn cho từng cảnh: tiếng Anh, đã xem hết hướng dẫn, đủ thành tựu (để không có thông báo thành tựu chen vào)
  const SET = `window.__set = o => {
    const lv = Object.assign(fresh().lv, o.lv || {}); delete o.lv;
    s = Object.assign(fresh(), {lang: 'en', mute: 2, clicks: 500, tips: Object.fromEntries(GUIDE.map(g => [g[0], 1])), ach: Object.fromEntries(ACH.map(a => [a.id, 1]))}, o);
    s.lv = lv; s.cap = s.sta = staMax(); shown = -1; syncRank(true); buildTexts(); drawArt(); go(s.scene); s.cap = s.sta = staMax(); ui();
  }`;
  const box = async (p, sel) => { const b = await p.locator(sel).first().boundingBox(); return {x: b.x + b.width / 2, y: b.y + b.height / 2, w: b.width, h: b.height}; };
  async function taps(p, n, gap = 125) {   // cú bấm thật (isTrusted), khoảng 7 lần/giây, rải quanh thân nhân vật
    const c = await box(p, '#art');
    for (let i = 0; i < n; i++) {
      await p.mouse.click(c.x + (Math.random() - .5) * c.w * .35, c.y + (Math.random() - .45) * c.h * .4);
      await wait(gap + Math.random() * 30);
    }
  }
  const scenes = {
    a: {   // nhân viên yếu ớt bấm tập, mua Ngực, LỘT XÁC lên hạng 2
      setup: `__set({rk: 0, best: 0, day: 2, lv: {tay: 5, vai: 4, nguc: 1}, scene: 'gym', seen: 3}); s.cal = bulk(EX[2], 1) - 11 * clickPower() - 1.5 * pps();`,
      run: async p => { await taps(p, 13); const b = await box(p, '#list .buy[data-i="2"]'); await p.mouse.click(b.x, b.y); await wait(150); await taps(p, 18); },
    },
    b: {   // thách đấu Hank the Guard và thắng
      setup: `__set({best: 2, day: 9, wins: 3, kg: 83.6, fat: 20, lv: {tay: 14, vai: 12, nguc: 7, bung: 5}, scene: 'gym', seen: 5});`,
      run: async p => {
        let b = await box(p, '#tabDuel'); await p.mouse.click(b.x, b.y); await wait(350);
        await p.locator('#rivals .fight[data-r="3"]').scrollIntoViewIfNeeded(); b = await box(p, '#rivals .fight[data-r="3"]'); await p.mouse.click(b.x, b.y); await wait(200);
        for (let k = 0; k < 8 && await p.evaluate('!!duel'); k++) await taps(p, 5);
        await wait(1100);
      },
    },
    c: {   // chọn bữa tối, đi ngủ, sáng hôm sau ở văn phòng
      setup: `__set({best: 2, day: 9, wins: 4, kg: 84.2, fat: 45, lv: {tay: 14, vai: 12, nguc: 7, bung: 5}, scene: 'home', seen: 5});`,
      run: async p => { await wait(500); const b = await box(p, '#meals .meal:nth-child(2)'); await p.mouse.click(b.x, b.y); await wait(1000); const z = await box(p, '#sleep'); await p.mouse.click(z.x, z.y); await wait(4300); },
    },
    d: {   // thần gym hạng 6 bấm ra số lớn
      setup: `__set({best: 5, day: 41, wins: 14, stars: 6, kg: 76.5, lv: {tay: 80, vai: 70, nguc: 62, bung: 55, mat: 45, chan: 45, lung: 36, cardio: 24}, scene: 'gym', seen: 8}); s.cal = 2.4e9;`,
      run: async p => { await taps(p, 30, 105); },
    },
  };
  const out = [];
  for (const o of [{name: 'land', w: 1280, h: 720}, {name: 'port', w: 720, h: 1080}]) for (const [name, sc] of Object.entries(scenes)) {
    const ctx = await browser.newContext({viewport: {width: o.w, height: o.h}, recordVideo: {dir: RAW + '/tmp', size: {width: o.w, height: o.h}}});
    const t0 = Date.now(), p = await ctx.newPage();
    await p.goto(URL); await p.waitForFunction('ready');
    await p.evaluate(SET); await p.evaluate(sc.setup);
    await wait(1300);   // chờ hiệu ứng loé sáng của go() tắt
    const start = Date.now() - t0; await sc.run(p); const end = Date.now() - t0;
    const open = await p.evaluate('document.querySelectorAll("#modal:not([hidden]),#guide:not([hidden])").length');
    await ctx.close();
    const file = `${RAW}/${o.name}_${name}_${start}_${end}.webm`;
    await p.video().saveAs(file); await p.video().delete();
    out.push({file, open});
  }
  return out;
}
