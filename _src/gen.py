#!/usr/bin/env python3
"""Social Hug: visi puslapiai iš vieno failo. Paleisti: python3 _src/gen.py"""
import json, os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://socialhug.lt'
LOGO = json.load(open(os.path.join(ROOT, '_src', 'logo.json')))
TEL, TEL_H, MAIL = '+37060065500', '+370 600 65500', 'info@socialhug.lt'
ADDR = 'Miško g. 6, Šlienavos k., Samylų sen., Kauno r. sav., LT-53148'
ARR = '<span class="arr" aria-hidden="true">→</span>'


def svg(key, cls, label=None):
    o = LOGO[key]
    a = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true" focusable="false"'
    return f'<svg class="{cls}" viewBox="{o["vb"]}"{a}><g transform="{o["tr"]}"><path d="{o["d"]}"/></g></svg>'


NAV = [('konsultacijos.html', 'Konsultacijos'), ('jaunimas.html', 'Jaunimas'),
       ('projektai.html', 'Projektai'), ('#kontaktai', 'Kontaktai')]


def nav(cur):
    cur_attr = ' aria-current="page"'
    links = ''.join(f'<a href="{h}"{cur_attr if h == cur else ""}>{t}</a>' for h, t in NAV)
    sheet = ''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<header class="nav" data-nav>
  <div class="wrap nav-in">
    <a class="brand" href="index.html" aria-label="VšĮ „Social Hug“, pradžia">{svg('mark', 'b-mark')}{svg('word', 'b-word')}</a>
    <nav class="nav-links" aria-label="Pagrindinė navigacija">{links}<a class="btn nav-tel" href="tel:{TEL}">{TEL_H}</a></nav>
    <button class="nav-menu" type="button" aria-expanded="false" aria-controls="sheet"><span class="bars" aria-hidden="true"></span>Meniu</button>
    <div class="nav-sheet" id="sheet">{sheet}<a class="btn" href="tel:{TEL}">Skambinti {TEL_H}</a></div>
  </div>
</header>'''


def funders_foot():
    return f'''<div class="funders">
          <div class="chip-w"><img class="f-eu" src="assets/eu-badge.webp" alt="Bendrai finansuoja Europos Sąjunga" width="800" height="174" loading="lazy"></div>
          <div class="f-row">
            <div class="chip-w"><img class="f-kr" src="assets/kauno-r-logo.webp" alt="Kauno rajono savivaldybė" width="387" height="384" loading="lazy"></div>
            <div class="chip-w"><img class="f-aid" style="width:100px" src="assets/aid-logo.webp" alt="Projekto „Alternatyvių investicijų detektorius“ ženklas" width="600" height="257" loading="lazy"></div>
          </div>
        </div>'''


def footer():
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        {svg('mark', 'b-mark', 'Social Hug')}{svg('word', 'b-word')}
        <p class="foot-org"><strong>VšĮ „Social Hug“</strong><br>Viešoji įstaiga · įmonės kodas 306626238<br>Miško g. 6, Šlienavos k., Samylų sen.,<br>Kauno r. sav., LT-53148</p>
      </div>
      <nav aria-label="Svetainė">
        <h2>Svetainėje</h2>
        <ul><li><a href="konsultacijos.html">Konsultacijos</a></li><li><a href="jaunimas.html">Jaunimo centras</a></li><li><a href="projektai.html">Projektai</a></li><li><a href="socialinis-verslas.html">Socialinis verslas</a></li></ul>
      </nav>
      <div>
        <h2>Kontaktai</h2>
        <ul><li><a href="tel:{TEL}">{TEL_H}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul>
      </div>
      <div>
        <h2>Projektų finansavimas</h2>
        {funders_foot()}
      </div>
    </div>
    <div class="foot-base"><p>© {date.today().year} VšĮ „Social Hug“</p><p>Projektus finansuoja Kauno rajono savivaldybė ir Europos Sąjunga</p></div>
  </div>
</footer>'''


def contact(title, text):
    return f'''<section class="sec sec-tone" id="kontaktai" aria-labelledby="kontaktai-h">
    <div class="wrap contact">
      <div class="rv">
        <h2 class="t-h2" id="kontaktai-h">{title}</h2>
        <p class="lead" style="margin-top:20px">{text}</p>
        <a class="tel-big" href="tel:{TEL}">{TEL_H}</a><br>
        <a class="lnk mail" href="mailto:{MAIL}">{MAIL}</a>
      </div>
      <dl class="reg rv" style="--d:120ms">
        <div><dt>Adresas</dt><dd>{ADDR}</dd></div>
        <div><dt>Teisinė forma</dt><dd>Viešoji įstaiga</dd></div>
        <div><dt>Įmonės kodas</dt><dd>306626238</dd></div>
        <div><dt>Įsteigta</dt><dd>2023 m. lapkričio 10 d.</dd></div>
      </dl>
    </div>
  </section>'''


def request_form(dark=True):
    chips = ''.join(
        f'<label class="chip"><input type="radio" name="kas" value="{v}"><span>{v}</span></label>'
        for v in ['Antstolis', 'VMI', 'SODRA', 'Kita arba nežinau'])
    return f'''<section class="sec{' dark' if dark else ''}" id="kontaktai" aria-labelledby="kreiptis-h">
    <div class="wrap req">
      <div class="req-side rv">
        <h2 class="t-h2" id="kreiptis-h">Parašykite trumpai apie savo situaciją.</h2>
        <p class="muted">Susisieksime ir sutarsime dėl konsultacijos. Konsultuoja teisininkai ir socialiniai darbuotojai.</p>
        <a class="tel-big" href="tel:{TEL}">{TEL_H}</a><br>
        <a class="lnk mail" href="mailto:{MAIL}">{MAIL}</a>
        <dl class="reg">
          <div><dt>Adresas</dt><dd>{ADDR}</dd></div>
          <div><dt>Įmonės kodas</dt><dd>306626238</dd></div>
        </dl>
      </div>
      <form class="form rv" id="kreiptis" style="--d:120ms" data-mailto="{MAIL}" novalidate>
        <div class="fld"><label for="f-name">Vardas</label><input id="f-name" name="vardas" autocomplete="given-name" required></div>
        <div class="fld"><label for="f-contact">Telefonas arba el. paštas</label><input id="f-contact" name="kontaktas" autocomplete="tel" inputmode="email" required></div>
        <fieldset class="fld fld-wide"><legend>Kas išieško skolą</legend><div class="chips">{chips}</div></fieldset>
        <div class="fld fld-wide"><label for="f-msg">Trumpai apie situaciją</label><textarea id="f-msg" name="zinute" rows="3"></textarea></div>
        <div class="form-foot">
          <button class="btn" type="submit">Paruošti laišką {ARR}</button>
          <p class="muted">Atsidarys jūsų el. pašto programa su paruoštu laišku adresu {MAIL}.</p>
        </div>
        <p class="form-msg" role="status" aria-live="polite"></p>
      </form>
    </div>
  </section>'''


# ---------- projects (one source for every page) ----------
P_KR = dict(
    id='kauno-r', title='Konsultacijos asmenims, turintiems įsiskolinimų',
    cap='Finansavimo sutartis Nr. S-596 · vykdomas iki 2026-12-31',
    short='Teisininkai ir socialiniai darbuotojai konsultuoja asmenis, kurių įsiskolinimus išieško antstoliai, VMI ar SODRA.',
    funder='Finansuoja Kauno rajono savivaldybė',
    logos='<img class="lg-kr" src="assets/kauno-r-logo.webp" alt="Kauno rajono savivaldybės ženklas" width="387" height="384" >')
P_AID = dict(
    id='aid2', title='„Alternatyvių investicijų detektorius“ (AID2)',
    cap='Projekto Nr. 07-023-P-0002 · vykdomas',
    short='Įgyvendinamas 2026-01-13–2029-07-31 kartu su Europos socialinio fondo agentūra. VšĮ „Social Hug“ dalyvauja kaip partneris ir veiklas vykdo nuo 2026-06-15 „Restarto“ vardu.',
    funder='Bendrai finansuojamas Europos Sąjungos fondų ir bendrojo finansavimo lėšomis',
    logos='<img class="lg-eu" src="assets/eu-badge.webp" alt="Bendrai finansuoja Europos Sąjunga" width="800" height="174" loading="lazy">'
          '<img class="lg-aid" src="assets/aid-logo.webp" alt="Projekto „Alternatyvių investicijų detektorius“ ženklas" width="600" height="257" loading="lazy">')


def sheet(p, d=0):
    return f'''<article class="sheet rv" style="--d:{d}ms">
          <div class="sheet-logos">{p['logos']}</div>
          <div class="sheet-body">
            <h3 class="t-h3">{p['title']}</h3>
            <p class="cap">{p['cap']}</p>
            <p class="m-hide">{p['short']}</p>
            <a class="lnk" href="projektai.html#{p['id']}">Projekto aprašymas {ARR}</a>
            <p class="sheet-funder m-hide">{p['funder']}</p>
          </div>
        </article>'''


def sheets_section(title, lead, tone=False):
    return f'''<section class="sec{' sec-tone' if tone else ''}" id="projektai" aria-labelledby="projektai-h" data-client-only>
    <div class="wrap">
      <div class="head">
        <h2 class="t-h2 rv" id="projektai-h">{title}</h2>
        <p class="lead rv" style="--d:120ms">{lead}</p>
      </div>
      <div class="sheets">
        {sheet(P_KR)}
        {sheet(P_AID, 140)}
      </div>
    </div>
  </section>'''


# ---------- pages ----------
def page_index():
    doors = [
        ('konsultacijos.html', 'Socialinės paslaugos ir teisinis konsultavimas',
         'Teisinės ir socialinio darbuotojo konsultacijos asmenims, turintiems įsiskolinimų.', '2 vykdomi projektai'),
        ('jaunimas.html', 'Jaunimo įgalinimas',
         'Atviras jaunimo centras: edukacinės, kūrybinės ir sportinės veiklos vaikams bei paaugliams.', 'Atviras centras'),
        ('socialinis-verslas.html', 'Socialinis verslas',
         'Kryptis, kurią organizacija šiuo metu rengia.', 'Rengiama'),
    ]
    rows = ''.join(f'''<a class="door" href="{h}"><span class="wrap door-in"><span class="door-t">{t}</span><span class="door-d">{d}</span><span class="door-s">{s}{ARR}</span></span></a>''' for h, t, d, s in doors)
    return f'''<section class="hero hero-home" data-hero>
    <div class="wrap">
      <h1 class="t-poster rv" style="--d:0ms" data-signature>Teisinė ir socialinė pagalba<span class="m-hide">, veiklos vaikams</span> Kauno rajone.</h1>
      <div class="hero-row">
        <p class="lead rv" style="--d:140ms">VšĮ „Social Hug“ konsultuoja žmones, turinčius įsiskolinimų, ir organizuoja veiklas vaikams bei paaugliams.</p>
        <div class="acts rv" style="--d:280ms">
          <a class="btn" href="konsultacijos.html#kreiptis">Kreiptis dėl konsultacijos {ARR}</a>
          <a class="lnk" href="tel:{TEL}">{TEL_H}</a>
        </div>
      </div>
      <dl class="facts rv m-hide" style="--d:420ms">
        <div><dt>Organizacija</dt><dd>VšĮ, nuo 2023</dd></div>
        <div><dt>Vykdomi projektai</dt><dd>2 · Kauno r. sav., ES</dd></div>
        <div><dt>Veikiame</dt><dd>Kauno rajone</dd></div>
      </dl>
    </div>
  </section>

  <section class="sec dark" aria-labelledby="kryptys-h">
    <div class="wrap head">
      <h2 class="t-h2 rv" id="kryptys-h">Trys veiklos kryptys.</h2>
      <p class="lead rv muted m-hide" style="--d:120ms">Kiekviena kryptis turi savo puslapį su paslaugomis, veiklomis ir kontaktais.</p>
    </div>
    <div class="doors" data-stagger="90">{rows}</div>
  </section>

  {sheets_section('Vykdomi projektai.', 'Konsultacijas finansuoja Kauno rajono savivaldybė ir Europos Sąjunga. Visa informacija apie projektus skelbiama viešai.')}

  <section class="sec sec-tone" aria-labelledby="apie-h">
    <div class="wrap about">
      <div>
        <h2 class="t-h2 rv" id="apie-h">Padedame suaugusiems susitvarkyti su skolomis, o vaikams atrasti savo gebėjimus.</h2>
        <div class="about-text rv" style="--d:120ms">
          <p>Sunkumų patiriančioms šeimoms ir asmenims teikiame teisines bei socialinio darbuotojo konsultacijas, padedančias suvaldyti finansinius įsipareigojimus ir grįžti į darbo rinką.</p>
          <p class="m-hide">Vaikams ir paaugliams organizuojame edukacines, kūrybines ir sportines veiklas, padedančias atrasti gebėjimus ir stiprinti pasitikėjimą savimi.</p>
        </div>
      </div>
      <div class="ledger rv" style="--d:200ms">
        <span class="cap">Bendradarbiaujame su</span>
        <ul data-stagger="70"><li>savivaldybėmis</li><li>Užimtumo tarnyba</li><li>nevyriausybinėmis organizacijomis</li><li>darbdaviais</li><li>švietimo įstaigomis</li></ul>
      </div>
    </div>
  </section>

  {request_form(dark=True)}'''


def page_konsultacijos():
    services = [
        ('Situacijos įvertinimas', 'Kartu peržiūrime įsiskolinimus ir vykdomus išieškojimus, kad būtų aišku, nuo ko pradėti.'),
        ('Teisinės konsultacijos', 'Dėl skolų, sutarčių ir kitų finansinių įsipareigojimų, taip pat dėl įsiskolinimų, kuriuos išieško antstoliai, VMI ar SODRA.'),
        ('Socialinio darbuotojo konsultacijos', 'Dėl socialinių paslaugų ir paramos galimybių.'),
        ('Informacija apie paramą ir teises', 'Paaiškiname esamus paramos mechanizmus ir skolininko teises.'),
        ('Kelias į darbo rinką', 'Kartu su darbdaviais ir švietimo įstaigomis organizuojame mokymus bei praktines veiklas, padedančias įgyti ar atnaujinti darbo rinkai reikalingus įgūdžius.'),
    ]
    rows = ''.join(f'<div class="row"><h3 class="t-h3">{t}</h3><p>{d}</p></div>' for t, d in services)
    return f'''<section class="hero hero-sub" data-hero>
    <div class="wrap hero-grid">
      <div>
        <h1 class="t-display rv">Teisinė ir socialinė pagalba turintiems įsiskolinimų.</h1>
        <p class="lead rv" style="--d:140ms">Teikiame teisines ir socialinio darbuotojo konsultacijas asmenims, susiduriantiems su ekonominiais sunkumais.<span class="m-hide"> Siekiame, kad žmonės išspręstų sunkumus ir grįžtų į darbo rinką.</span></p>
        <div class="acts rv" style="--d:280ms">
          <a class="btn" href="#kreiptis">Kreiptis dėl konsultacijos {ARR}</a>
          <a class="lnk" href="tel:{TEL}">{TEL_H}</a>
        </div>
      </div>
      <div class="stack rv" style="--d:420ms">
        <span class="cap">Kai skolą išieško</span>
        <ul><li>antstoliai</li><li>VMI</li><li>SODRA</li></ul>
        <p class="note">Konsultuoja teisininkai ir socialiniai darbuotojai.</p>
      </div>
    </div>
  </section>

  <section class="sec sec-tone" aria-labelledby="paslaugos-h">
    <div class="wrap">
      <div class="head">
        <h2 class="t-h2 rv" id="paslaugos-h">Kaip padedame.</h2>
        <p class="lead rv" style="--d:120ms">Pagalba pritaikoma kiekvieno žmogaus situacijai: nuo skolų peržiūros iki grįžimo į darbą.</p>
      </div>
      <div class="rows" data-stagger="80">{rows}</div>
    </div>
  </section>

  {request_form(dark=True)}

  {sheets_section('Paslaugos teikiamos vykdant projektus.', 'Konsultacijas finansuoja Kauno rajono savivaldybė ir Europos Sąjunga.')}'''


def tl_pos(d):
    """2026-01-01..2030-01-01 skalėje, procentais."""
    y, m, dd = map(int, d.split('-'))
    start, end = date(2026, 1, 1), date(2030, 1, 1)
    return round((date(y, m, dd) - start).days / (end - start).days * 100, 2)


def page_projektai():
    a1, b1 = tl_pos('2026-03-25'), tl_pos('2026-12-31')
    a2, p2, b2 = tl_pos('2026-01-13'), tl_pos('2026-06-15'), tl_pos('2029-07-31')
    return f'''<section class="hero hero-sub" data-hero>
    <div class="wrap">
      <div class="hero-grid">
        <div>
          <h1 class="t-display rv">Vykdomi projektai ir jų finansavimas.</h1>
          <p class="lead rv" style="--d:140ms">Skelbiame, kokius projektus vykdo VšĮ „Social Hug“<span class="m-hide">, kas juos finansuoja, kokie jų tikslai ir veiklos</span>.</p>
        </div>
      </div>
      <div class="tl rv" style="--d:280ms" data-signature data-client-only>
        <div class="tl-scale" aria-hidden="true"><span>2026</span><span>2027</span><span>2028</span><span>2029</span></div>
        <div class="tl-bars" data-tl-start="2026-01-01" data-tl-end="2030-01-01">
          <a class="tl-bar" href="#kauno-r" style="--a:{a1}%;--b:{b1}%" aria-label="Sutartis Nr. S-596 su Kauno rajono savivaldybe, nuo 2026-03-25 iki 2026-12-31">
            <span class="tl-run"></span><span class="tl-txt tl-out">Sutartis Nr. S-596 <span class="cap">Kauno r. sav.</span></span>
          </a>
          <a class="tl-bar" href="#aid2" style="--a:{a2}%;--b:{b2}%" aria-label="Projektas AID2, nuo 2026-01-13 iki 2029-07-31, VšĮ Social Hug partnerio veiklos nuo 2026-06-15">
            <span class="tl-run pre" style="--a:{a2}%;--b:{p2}%"></span><span class="tl-run" style="--a:{p2}%;--b:{b2}%"></span><span class="tl-txt" style="left:calc({p2}% + 16px)">AID2 · „Restartas“ <span class="cap">ES fondai</span></span>
          </a>
        </div>
        <div class="tl-key"><span><i></i>VšĮ „Social Hug“ vykdo veiklas</span><span><i class="o"></i>AID2 projektas iki partnerio veiklų pradžios</span></div>
      </div>
    </div>
  </section>

  <section class="sec sec-tone" id="kauno-r" aria-labelledby="kr-h">
    <div class="wrap ann">
      <aside class="ann-side rv">
        <div class="plate"><img src="assets/kauno-r-full.webp" alt="Kauno rajono savivaldybės ženklas" width="716" height="615"></div>
        <p>Projektą finansuoja Kauno rajono savivaldybė.</p>
      </aside>
      <article class="ann-main rv" style="--d:120ms">
        <span class="cap">Finansavimo sutartis Nr. S-596 · vykdomas</span>
        <h2 class="t-h2" id="kr-h">Konsultacijos asmenims, turintiems įsiskolinimų</h2>
        <div class="prose">
          <p>VšĮ „Social Hug“ ir Kauno rajono savivaldybė 2026-03-25 pasirašė finansavimo sutartį Nr. S-596, kurios pagrindu dėl įsiskolinimų, vykdomų pas antstolius, konsultuojami asmenys.</p>
          <p>Vykdant projektinę idėją siekiama, kad padedant teisininkams ir socialiniams darbuotojams kuo daugiau asmenų, turinčių įsiskolinimų, kuriuos išieško antstoliai, VMI ar SODRA, spręstų sunkumus ir grįžtų į darbo rinką.</p>
          <p>Projektas vykdomas iki 2026-12-31.</p>
        </div>
        <dl class="rec">
          <div><dt>Finansuotojas</dt><dd>Kauno rajono savivaldybė</dd></div>
          <div><dt>Projekto vykdytojas</dt><dd>VšĮ „Social Hug“</dd></div>
          <div><dt>Finansavimo sutartis</dt><dd><span class="cap">Nr. S-596</span></dd></div>
          <div><dt>Sutartis pasirašyta</dt><dd><span class="cap">2026-03-25</span></dd></div>
          <div><dt>Vykdomas iki</dt><dd><span class="cap">2026-12-31</span></dd></div>
          <div><dt>Kam skirta</dt><dd>Asmenims, turintiems įsiskolinimų, kuriuos išieško antstoliai, VMI ar SODRA</dd></div>
          <div><dt>Pagalba</dt><dd>Teisininkų ir socialinių darbuotojų konsultacijos</dd></div>
          <div><dt>Būsena</dt><dd>Vykdomas</dd></div>
        </dl>
        <div class="ann-acts">
          <a class="lnk" href="konsultacijos.html#kreiptis">Kreiptis dėl konsultacijos {ARR}</a>
          <a class="lnk" href="konsultacijos.html">Teikiamos paslaugos {ARR}</a>
        </div>
      </article>
    </div>
  </section>

  <section class="sec" id="aid2" aria-labelledby="aid-h">
    <div class="wrap ann">
      <aside class="ann-side rv">
        <div class="plate">
          <img src="assets/eu-badge.webp" alt="Bendrai finansuoja Europos Sąjunga" width="800" height="174">
          <img class="lg-aid" src="assets/aid-logo.webp" alt="Projekto „Alternatyvių investicijų detektorius“ ženklas" width="600" height="257">
        </div>
        <p>Projektas bendrai finansuojamas Europos Sąjungos fondų ir bendrojo finansavimo lėšomis.</p>
      </aside>
      <article class="ann-main rv" style="--d:120ms">
        <span class="cap">Projekto Nr. 07-023-P-0002 · vykdomas</span>
        <h2 class="t-h2" id="aid-h">„Alternatyvių investicijų detektorius“ (AID2)</h2>
        <div class="prose">
          <p>Projektas „Alternatyvių investicijų detektorius“ (AID2) (Nr. 07-023-P-0002) įgyvendinamas nuo 2026 m. sausio 13 d. iki 2029 m. liepos 31 d. kartu su Europos socialinio fondo agentūra.</p>
          <p>VšĮ „Social Hug“ projekte dalyvauja kaip partneris ir veiklas vykdo nuo 2026 m. birželio 15 d. „Restarto“ vardu.</p>
        </div>
        <dl class="rec">
          <div><dt>Projekto pavadinimas</dt><dd>„Alternatyvių investicijų detektorius“ (AID2)</dd></div>
          <div><dt>Veiklos pavadinimas</dt><dd>„Restartas“</dd></div>
          <div><dt>Projekto numeris</dt><dd><span class="cap">07-023-P-0002</span></dd></div>
          <div><dt>Įgyvendinimo pradžia</dt><dd><span class="cap">2026 m. sausio 13 d.</span></dd></div>
          <div><dt>Įgyvendinimo pabaiga</dt><dd><span class="cap">2029 m. liepos 31 d.</span></dd></div>
          <div><dt>Įgyvendinama kartu su</dt><dd>Europos socialinio fondo agentūra</dd></div>
          <div><dt>VšĮ „Social Hug“ vaidmuo</dt><dd>Projekto partneris</dd></div>
          <div><dt>Partnerio veiklų pradžia</dt><dd><span class="cap">2026 m. birželio 15 d.</span></dd></div>
          <div><dt>Finansavimo šaltinis</dt><dd>Europos Sąjungos fondų ir bendrojo finansavimo lėšos</dd></div>
          <div><dt>Būsena</dt><dd>Vykdomas</dd></div>
        </dl>
        <div class="blk"><h3>Projekto tikslas</h3><p>Stiprinti socialinę integraciją ir didinti socialinę riziką bei socialinę atskirtį patiriančių žmonių galimybes sėkmingai įsilieti į darbo rinką.</p></div>
        <div class="blk"><h3>Projekto veiklos</h3><p>Projektas skirtas plėtoti socialinės integracijos paslaugas ir padėti žmonėms aktyviau dalyvauti bendruomenės gyvenime.</p></div>
        <div class="blk"><h3>Kam skirta</h3><p>VšĮ „Social Hug“, kaip projekto partneris, dirba su nedirbančiais asmenimis, turinčiais įsiskolinimų, perduotų antstoliams priverstiniam išieškojimui.</p><p>Jeigu susiduriate su sunkumais dėl įsiskolinimų, kviečiame susisiekti: kartu ieškosime geriausių sprendimų.</p></div>
        <div class="ann-acts">
          <a class="lnk" href="https://www.esf.lt/projektai/alternatyviu-investiciju-detektorius-aid2/" target="_blank" rel="noopener">Projektas ESF agentūros svetainėje {ARR}</a>
          <a class="lnk" href="konsultacijos.html">Teikiamos paslaugos {ARR}</a>
        </div>
      </article>
    </div>
  </section>

  {contact('Klausimai apie projektus.', 'Atsakome į klausimus dėl projektų veiklų ir dalyvavimo sąlygų.')}'''


def page_jaunimas():
    acts = [
        ('Dramos užsiėmimai', 'Sceninė raiška ir kūrybinės dirbtuvės.'),
        ('Viešojo kalbėjimo užsiėmimai', 'Drąsa kalbėti auditorijai ir aiškiai dėstyti mintis.'),
        ('Kūrybinės ir edukacinės veiklos', 'Galimybė išbandyti naujas patirtis, atrasti pomėgius ir stiprinti saviraišką.'),
        ('Sportinės veiklos', 'Judėjimas, komanda ir sveikas užimtumas.'),
        ('Atviros erdvės veiklos', 'Programą nuolat pildome, ateiti galima ir tiesiog pabūti.'),
    ]
    rows = ''.join(f'<div class="row"><h3 class="t-h3">{t}</h3><p>{d}</p></div>' for t, d in acts)
    goals = [
        ('Užimtumas ir įtrauktis', 'Įtraukti kuo daugiau vaikų ir paauglių į prasmingas, ugdančias ir socialinę integraciją skatinančias veiklas.'),
        ('Gebėjimų atradimas', 'Padėti atrasti pomėgius ir gebėjimus, stiprinti kūrybiškumą bei saviraišką.'),
        ('Pasitikėjimas ir savarankiškumas', 'Stiprinti pasitikėjimą savimi, atsparumą ir savarankiškumą.'),
        ('Dalyvavimas visuomenėje', 'Skatinti asmeninį augimą ir motyvaciją aktyviai dalyvauti visuomeniniame gyvenime.'),
    ]
    g = ''.join(f'<div class="goal"><h3 class="t-h3">{t}</h3><p>{d}</p></div>' for t, d in goals)
    return f'''<section class="hero hero-sub" data-hero>
    <div class="wrap hero-grid">
      <div>
        <h1 class="t-display rv">Atviras jaunimo centras vaikams ir paaugliams.</h1>
        <p class="lead rv" style="--d:140ms">Organizuojame edukacines, kūrybines ir sportines veiklas<span class="m-hide">, kurios leidžia išbandyti naujas patirtis, atrasti pomėgius ir atskleisti gebėjimus</span>.</p>
        <div class="acts rv" style="--d:280ms">
          <a class="btn" href="#kontaktai">Klausti apie veiklas {ARR}</a>
          <a class="lnk" href="tel:{TEL}">{TEL_H}</a>
        </div>
      </div>
      <div class="stack rv" style="--d:420ms">
        <span class="cap">Veiklos centre</span>
        <ul><li>edukacinės</li><li>kūrybinės</li><li>sportinės</li></ul>
        <p class="note">Atviras centras vaikams ir paaugliams.</p>
      </div>
    </div>
  </section>

  <section class="sec sec-tone" aria-labelledby="veiklos-h">
    <div class="wrap">
      <div class="head">
        <h2 class="t-h2 rv" id="veiklos-h">Ką organizuojame centre.</h2>
        <p class="lead rv" style="--d:120ms">Išsami veiklų programa rengiama. Apie vykstančius užsiėmimus galite pasiteirauti telefonu arba el. paštu.</p>
      </div>
      <div class="rows" data-stagger="80">{rows}</div>
    </div>
  </section>

  <section class="sec dark" aria-labelledby="tikslai-h">
    <div class="wrap">
      <div class="head">
        <h2 class="t-h2 rv" id="tikslai-h">Ko siekiame veiklomis.</h2>
      </div>
      <div class="goals" data-stagger="90">{g}</div>
    </div>
  </section>

  {contact('Klauskite apie veiklas.', 'Atsakome į klausimus apie užsiėmimus, tvarkaraštį ir dalyvavimo sąlygas.')}'''


def page_sv():
    return f'''<section class="hero hero-sub" data-hero>
    <div class="wrap hero-grid">
      <div>
        <h1 class="t-display rv">Socialinis verslas: trečioji veiklos kryptis.</h1>
        <p class="lead rv" style="--d:140ms">Kryptis šiuo metu rengiama. Informaciją apie socialinio verslo veiklas paskelbsime jas pradėję įgyvendinti.</p>
        <div class="acts rv" style="--d:280ms">
          <a class="btn" href="konsultacijos.html">Socialinės paslaugos {ARR}</a>
          <a class="lnk" href="jaunimas.html">Jaunimo centras</a>
        </div>
      </div>
      <div class="stack rv" style="--d:420ms">
        <span class="cap">Veiklos kryptys</span>
        <ul><li>konsultacijos <small>vykdoma</small></li><li>jaunimas <small>vykdoma</small></li><li>soc. verslas <small>rengiama</small></li></ul>
      </div>
    </div>
  </section>

  {contact('Turite pasiūlymą ar idėją?', 'Jei svarstote bendradarbiavimą socialinio verslo srityje, parašykite mums.')}'''


def page_404():
    return f'''<section class="hero lost" data-hero>
    <div class="wrap">
      <h1 class="t-display rv">Puslapis nerastas.</h1>
      <p class="lead rv" style="--d:140ms">Nuoroda pasenusi arba puslapis perkeltas.</p>
      <div class="acts rv" style="--d:280ms"><a class="btn" href="index.html">Į pradžią {ARR}</a><a class="lnk" href="konsultacijos.html">Konsultacijos</a></div>
    </div>
  </section>'''


PAGES = [
    ('index.html', '', 'Socialinės paslaugos ir teisinė pagalba Kauno r. | Social Hug',
     'Teisinės ir socialinio darbuotojo konsultacijos turintiems įsiskolinimų. Atviras jaunimo centras vaikams ir paaugliams. VšĮ „Social Hug“, Kauno rajonas.', page_index, '1.0'),
    ('konsultacijos.html', 'konsultacijos.html', 'Konsultacijos turintiems įsiskolinimų, Kauno r. | Social Hug',
     'Teisininkų ir socialinių darbuotojų konsultacijos asmenims, kurių įsiskolinimus išieško antstoliai, VMI ar SODRA. Kauno rajonas.', page_konsultacijos, '0.9'),
    ('projektai.html', 'projektai.html', 'Vykdomi projektai: sutartis Nr. S-596 ir AID2 | Social Hug',
     'VšĮ „Social Hug“ vykdomi projektai: finansavimo sutartis Nr. S-596 su Kauno rajono savivaldybe ir ES fondų projektas AID2.', page_projektai, '0.9'),
    ('jaunimas.html', 'jaunimas.html', 'Atviras jaunimo centras vaikams ir paaugliams, Kauno r. | Social Hug',
     'Edukacinės, kūrybinės ir sportinės veiklos vaikams ir paaugliams Kauno rajone. VšĮ „Social Hug“ atviras jaunimo centras.', page_jaunimas, '0.8'),
    ('socialinis-verslas.html', 'socialinis-verslas.html', 'Socialinis verslas | Social Hug',
     'Socialinis verslas: trečioji VšĮ „Social Hug“ veiklos kryptis, šiuo metu rengiama.', page_sv, '0.5'),
    ('404.html', None, 'Puslapis nerastas | Social Hug', 'Puslapis nerastas.', page_404, None),
]

ORG = {"@context": "https://schema.org", "@type": "NGO", "name": "VšĮ Social Hug", "alternateName": "Social Hug",
       "url": SITE + "/", "logo": SITE + "/assets/logo.png", "image": SITE + "/og.jpg", "email": MAIL,
       "telephone": TEL, "taxID": "306626238", "foundingDate": "2023-11-10",
       "address": {"@type": "PostalAddress", "streetAddress": "Miško g. 6, Šlienavos k.", "addressLocality": "Samylų sen., Kauno r. sav.",
                   "postalCode": "LT-53148", "addressRegion": "Kauno apskritis", "addressCountry": "LT"},
       "areaServed": {"@type": "AdministrativeArea", "name": "Kauno rajono savivaldybė"}, "knowsLanguage": "lt"}


def head(fn, path, title, desc):
    url = SITE + '/' + (path or '')
    robots = 'noindex' if path is None else 'index, follow, max-image-preview:large'
    canon = '' if path is None else f'<link rel="canonical" href="{url}">\n'
    ld = '' if path is None else f'<script type="application/ld+json">{json.dumps(ORG, ensure_ascii=False)}</script>\n'
    return f'''<!DOCTYPE html>
<html lang="lt">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#F3F1EB">
{canon}<meta property="og:type" content="website">
<meta property="og:locale" content="lt_LT">
<meta property="og:site_name" content="VšĮ „Social Hug“">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
{ld}<script>document.documentElement.classList.add('js')</script>
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
<a class="skip" href="#turinys">Pereiti prie turinio</a>
'''


def build():
    sm = []
    for fn, path, title, desc, fnc, prio in PAGES:
        html = head(fn, path, title, desc) + nav(fn) + '\n<main id="turinys">\n  ' + fnc() + '\n</main>\n' + footer() + '''
<script src="js/lenis.min.js" defer></script>
<script src="js/motion.js" defer></script>
<script src="js/site.js" defer></script>
</body>
</html>
'''
        if fn == '404.html':
            html = html.replace('href="#kontaktai"', 'href="index.html#kontaktai"')
        open(os.path.join(ROOT, fn), 'w').write(html)
        if path is not None:
            sm.append(f'  <url><loc>{SITE}/{path}</loc><lastmod>{date.today().isoformat()}</lastmod><priority>{prio}</priority></url>')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(sm) + '\n</urlset>\n')
    print('ok', len(PAGES), 'pages')


if __name__ == '__main__':
    build()
