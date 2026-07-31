// Fail-visible: klasė ant <html>. Be JS — viskas matoma iš karto.
document.documentElement.classList.add('js');

(function () {
  var d = document, w = window;
  var reduced = w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var isTouch = w.matchMedia('(pointer: coarse)').matches;

  /* ── 1. Glotnus slinkimas — LERP režimas, be inercijos uodegos ── */
  var lenis = null;
  if (!reduced && !isTouch && typeof w.Lenis === 'function') {
    lenis = new w.Lenis({ lerp: 0.1, smoothWheel: true, syncTouch: false });
    (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0);
  }

  // nav aukštis matuojamas, ne spėjamas (mobile'e jis dviejų eilučių)
  function navOffset() {
    var n = d.querySelector('.nav');
    return (n ? n.getBoundingClientRect().height : 72) + 12;
  }

  function goTo(target, instant) {
    if (lenis && !instant) {
      lenis.scrollTo(target, { offset: -navOffset(), duration: 1.05 });
    } else {
      w.scrollTo({
        top: target.getBoundingClientRect().top + w.scrollY - navOffset(),
        behavior: (reduced || instant) ? 'auto' : 'smooth'
      });
    }
  }

  d.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href');
      if (id.length < 2) return;
      var t = d.querySelector(id);
      if (!t) return;
      e.preventDefault();
      goTo(t);
      history.replaceState(null, '', id);
    });
  });

  // atėjus iš kito puslapio su #nuoroda — naršyklės šuolis nepaiso lipnaus nav'o
  if (location.hash.length > 1) {
    var landing = d.querySelector(location.hash);
    if (landing) {
      w.addEventListener('load', function () {
        setTimeout(function () { goTo(landing, true); }, 60);
      });
    }
  }

  /* ── 2. Hero choreografija — viena grupė, paleidžiama iš karto ── */
  var hero = d.querySelector('.hero');
  function startHero() { if (hero) hero.classList.add('hero-go'); }
  if (d.fonts && d.fonts.ready) {
    d.fonts.ready.then(startHero);
    setTimeout(startHero, 700);
  } else {
    requestAnimationFrame(startHero);
  }

  /* ── 3. Sekcijų atidengimas ── */
  var els = [].slice.call(d.querySelectorAll('[data-r]'));
  function show(el) { el.classList.add('r-in'); }

  if (reduced || !('IntersectionObserver' in w)) {
    els.forEach(show);
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        show(e.target);
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -8% 0px' });

    // kas jau matoma pirmame kadre — parodoma iš karto, be laukimo
    els.forEach(function (el) {
      var b = el.getBoundingClientRect();
      if (b.top < w.innerHeight * 0.92 && b.bottom > 0) show(el);
      else io.observe(el);
    });

    // saugikliai — jokia aplinkybė nepalieka turinio nematomo
    setTimeout(function () { els.forEach(show); startHero(); }, 2500);
    w.addEventListener('load', function () {
      setTimeout(function () { els.forEach(show); startHero(); }, 1200);
    });
    d.addEventListener('visibilitychange', function () {
      if (!d.hidden) setTimeout(function () { els.forEach(show); }, 300);
    });
  }

  /* ── 4. Nav būsena nuscrollinus ── */
  var nav = d.querySelector('.nav');
  if (nav) {
    var tick = false;
    function upd() { nav.classList.toggle('is-stuck', w.scrollY > 8); tick = false; }
    w.addEventListener('scroll', function () {
      if (!tick) { tick = true; requestAnimationFrame(upd); }
    }, { passive: true });
    if (lenis) lenis.on('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(upd); } });
    upd();
  }
})();
