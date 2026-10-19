/* Social Hug: meniu telefone, laiško paruošimas, šiandienos žymė projektų laiko juostoje */
(function () {
  var d = document;

  var nav = d.querySelector('[data-nav]');
  var btn = nav && nav.querySelector('.nav-menu');
  if (btn) {
    var set = function (open) {
      if (open) nav.setAttribute('data-open', ''); else nav.removeAttribute('data-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    btn.addEventListener('click', function () { set(!nav.hasAttribute('data-open')); });
    nav.querySelectorAll('.nav-sheet a').forEach(function (a) { a.addEventListener('click', function () { set(false); }); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.hasAttribute('data-open')) { set(false); btn.focus(); } });
  }

  /* the form prepares a letter in the visitor's own mail app: nothing is sent from the page */
  d.querySelectorAll('form[data-mailto]').forEach(function (f) {
    var msg = f.querySelector('.form-msg');
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = f.vardas.value.trim(), contact = f.kontaktas.value.trim();
      if (!name || !contact) {
        msg.textContent = 'Įrašykite vardą ir telefoną arba el. paštą, kad galėtume atsakyti.';
        (name ? f.kontaktas : f.vardas).focus();
        return;
      }
      var kas = f.querySelector('input[name="kas"]:checked');
      var body = 'Vardas: ' + name + '\nKontaktas: ' + contact +
        (kas ? '\nSkolą išieško: ' + kas.value : '') +
        (f.zinute.value.trim() ? '\n\n' + f.zinute.value.trim() : '');
      location.href = 'mailto:' + f.getAttribute('data-mailto') +
        '?subject=' + encodeURIComponent('Dėl konsultacijos') + '&body=' + encodeURIComponent(body);
      msg.textContent = 'Laiškas paruoštas jūsų el. pašto programoje. Jei ji neatsidarė, skambinkite +370 600 65500.';
    });
  });

  var bars = d.querySelector('[data-tl-start]');
  if (bars) {
    var a = new Date(bars.getAttribute('data-tl-start')), b = new Date(bars.getAttribute('data-tl-end')), now = new Date();
    if (now > a && now < b) {
      var x = ((now - a) / (b - a) * 100).toFixed(2);
      var m = d.createElement('span');
      m.className = 'tl-now'; m.style.setProperty('--x', x + '%');
      m.innerHTML = '<span>Šiandien</span>';
      m.setAttribute('aria-hidden', 'true');
      bars.appendChild(m);
    }
  }
})();
