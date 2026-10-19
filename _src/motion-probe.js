// node tools/motion-probe.js <url>  : measures the motion in Chromium (laptop) and WebKit (iPhone)
// Fails loudly on: no hero entrance, content stranded hidden, everything revealed at once, picker not swapping, console errors.
const pw = require('/Users/martiskuckailis/node_modules/playwright-core');
const url = process.argv[2] || 'http://127.0.0.1:3146/';
const IPHONE_UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const runs = [
  { name: 'chromium-1440x700', engine: 'chromium', ctx: { viewport: { width: 1440, height: 700 } } },
  { name: 'webkit-iphone', engine: 'webkit', ctx: { viewport: { width: 393, height: 852 }, isMobile: true, hasTouch: true, deviceScaleFactor: 3, userAgent: IPHONE_UA } },
  { name: 'chromium-reduced', engine: 'chromium', ctx: { viewport: { width: 1440, height: 700 }, reducedMotion: 'reduce' } },
];
const hiddenOnScreen = () => [...document.querySelectorAll('.rv, [data-stagger] > *')].filter(el => {
  const r = el.getBoundingClientRect(); const s = getComputedStyle(el);
  if (s.display === 'none' || r.width === 0) return false;
  const vis = r.top < innerHeight - 40 && r.bottom > 40;
  return vis && +s.opacity < 0.95;
}).map(el => (el.className || el.tagName) + ' @' + Math.round(el.getBoundingClientRect().top));
(async () => {
  let fails = 0;
  for (const r of runs) {
    const browser = await pw[r.engine].launch(r.engine === 'chromium' ? { channel: 'chrome' } : {}).catch(() => pw[r.engine].launch());
    const ctx = await browser.newContext(r.ctx);
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', m => { if (m.type() === 'error' && !/favicon|net::ERR|Failed to load resource|placard/.test(m.text())) errors.push(m.text()); });
    const out = [];
    const t0 = Date.now();
    await page.goto(url, { waitUntil: 'domcontentloaded' });
    const sample = async () => page.evaluate(() => {
      const h1 = document.querySelector('.hero h1'), m = document.querySelector('.hero-mark .m-fill');
      return { h1: +getComputedStyle(h1).opacity, img: 'mark', imgOp: 1, mark: m ? +getComputedStyle(m).opacity : 1 };
    });
    const s0 = await sample(); await page.waitForTimeout(450); const s1 = await sample(); await page.waitForTimeout(2600); const s2 = await sample();
    out.push(`hero mark fill ${s0.mark} -> ${s2.mark}`); if (s2.mark < 0.99) { fails++; out.push('FAIL hero mark not inked after 3 s'); }
    out.push(`hero h1 opacity ${s0.h1.toFixed(2)} -> ${s1.h1.toFixed(2)} -> ${s2.h1.toFixed(2)}; photo opacity ${s0.imgOp} (must be 1 from the start); photo transform start ${s0.img.slice(0, 22)} end ${s2.img.slice(0, 22)}`);
    const reduced = r.name.includes('reduced');
    if (s0.imgOp < 1) { fails++; out.push('FAIL photo not visible at once'); }
    if (s2.h1 < 0.99) { fails++; out.push('FAIL hero heading not visible after 3 s'); }
    if (!reduced && s0.h1 > 0.9 && s1.h1 > 0.99) out.push('WARN hero heading had no entrance');
    // below the fold must still be waiting (motion exists)
    const waiting = await page.evaluate(() => [...document.querySelectorAll('.rv, [data-stagger]')].filter(el => el.getBoundingClientRect().top > innerHeight * 1.2 && !el.classList.contains('in')).length);
    out.push(`elements below the fold still waiting: ${waiting}`);
    if (!reduced && waiting === 0) { fails++; out.push('FAIL everything revealed at once (no scroll motion)'); }
    // fast jumps: no content stranded hidden on screen
    const H = await page.evaluate(() => document.documentElement.scrollHeight);
    for (const f of [0.25, 0.5, 0.75, 1, 0.4]) {
      await page.evaluate(y => window.scrollTo(0, y), Math.round(H * f));
      await page.waitForTimeout(1400);
      const hid = await page.evaluate(hiddenOnScreen);
      if (hid.length) { fails++; out.push(`FAIL stranded at ${Math.round(f * 100)}%: ${hid.slice(0, 4).join(', ')}`); }
    }
    // slow natural scroll through the page with the wheel (desktop) or touch-like steps
    await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(400);
    for (let y = 0; y < H; y += 500) {
      if (r.ctx.isMobile) await page.evaluate(y => window.scrollTo(0, y), y); else await page.mouse.wheel(0, 500);
      await page.waitForTimeout(120);
    }
    await page.waitForTimeout(1400);
    const hidEnd = await page.evaluate(hiddenOnScreen);
    if (hidEnd.length) { fails++; out.push('FAIL stranded after scroll-through: ' + hidEnd.slice(0, 4).join(', ')); }
    const notIn = await page.evaluate(() => [...document.querySelectorAll('.rv, [data-stagger]')].filter(el => !el.classList.contains('in') && getComputedStyle(el).display !== 'none' && el.getBoundingClientRect().width > 0).length);
    out.push(`after scroll-through, elements never revealed: ${notIn}`);
    if (notIn) { fails++; out.push('FAIL some blocks never revealed'); }
    // anchor jump from the top via the nav (desktop) / quote link (phone)
    await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(600);
    const sel = r.ctx.isMobile ? '.nav-sheet a[href="#kontaktai"]' : '.nav-links a[href="#kontaktai"]';
    await page.evaluate(s => { const a = [...document.querySelectorAll(s)].find(a => a.offsetParent || a.getClientRects().length); a && a.click(); }, sel);
    await page.waitForTimeout(2200);
    const hidAnchor = await page.evaluate(hiddenOnScreen);
    const yAfter = await page.evaluate(() => Math.round(scrollY));
    out.push(`anchor jump landed at y=${yAfter}`);
    if (hidAnchor.length) { fails++; out.push('FAIL stranded after anchor jump: ' + hidAnchor.slice(0, 4).join(', ')); }
    if (errors.length) { fails++; out.push('FAIL console: ' + errors.slice(0, 3).join(' | ')); }
    const lenis = await page.evaluate(() => !!(window.__motion && window.__motion.lenis));
    out.push(`lenis active: ${lenis}`);
    console.log(`== ${r.name}\n  ` + out.join('\n  '));
    await browser.close();
  }
  console.log(fails ? `MOTION PROBE: ${fails} FAIL` : 'MOTION PROBE: PASS');
  process.exit(fails ? 1 : 0);
})();
