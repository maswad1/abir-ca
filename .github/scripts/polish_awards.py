from pathlib import Path
import re

p = Path('index.html')
s = p.read_text()

old_css = re.compile(r'''    \.awards\{padding:68px 0;background:#111113;border-top:1px solid var\(--line\)\}\n    \.awards-head\{.*?    \.awards-note\{margin-top:22px;color:#77716a;font-size:11px;line-height:1\.6\}\n''', re.S)
new_css = '''    .awards{padding:76px 0;background:#111113;border-top:1px solid var(--line)}
    .awards-layout{display:grid;grid-template-columns:.9fr 1.45fr;gap:24px;align-items:stretch}
    .awards-feature{position:relative;min-height:520px;padding:42px;border:1px solid #2d2923;background:linear-gradient(145deg,#181719,#0d0d0e);overflow:hidden;display:flex;flex-direction:column;justify-content:flex-end}
    .awards-watermark{position:absolute;width:72%;max-width:330px;right:-45px;top:38px;opacity:.085;filter:saturate(.9)}
    .awards-feature:after{content:"";position:absolute;inset:auto 0 0 0;height:58%;background:linear-gradient(180deg,transparent,rgba(0,0,0,.62));pointer-events:none}
    .awards-feature-copy{position:relative;z-index:2}
    .awards-big{font:600 clamp(84px,9vw,132px)/.78 var(--serif);letter-spacing:-.07em;color:var(--gold2);margin:24px 0 18px}
    .awards-years{font:600 28px/1.08 var(--serif);max-width:330px}
    .awards-feature p{max-width:380px;color:var(--muted);font-size:13px;line-height:1.65;margin:18px 0 0}
    .awards-list{border:1px solid #292622;background:#0d0d0e;display:grid;grid-template-rows:repeat(4,1fr)}
    .award-row{display:grid;grid-template-columns:150px 1fr;gap:26px;align-items:center;padding:28px 32px;border-bottom:1px solid #292622;position:relative}
    .award-row:last-child{border-bottom:0}
    .award-row:before{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--gold);opacity:0;transition:.2s}
    .award-row:hover:before{opacity:1}
    .award-rank{font:600 42px/1 var(--serif);color:var(--gold2);letter-spacing:-.035em}
    .award-row h3{font-size:21px;margin:0 0 7px}
    .award-row span{display:block;color:#d4cec6;font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase}
    .award-row small{display:block;color:#77716a;font-size:10px;line-height:1.5;margin-top:5px;letter-spacing:.035em;text-transform:uppercase}
    .awards-note{margin-top:18px;color:#6f6962;font-size:10px;line-height:1.6}
'''
s, n = old_css.subn(new_css, s, count=1)
if n != 1:
    raise SystemExit('Awards CSS block not found')

old_html = re.compile(r'''    <section class="awards" id="awards">.*?    </section>\n\n    <section class="testimonials"''', re.S)
new_html = '''    <section class="awards" id="awards">
      <div class="wrap">
        <div class="awards-layout">
          <div class="awards-feature">
            <img class="awards-watermark" src="pictures/abir_logo_ah.png" alt="" aria-hidden="true">
            <div class="awards-feature-copy">
              <div class="eyebrow">Awards &amp; Recognition</div>
              <div class="awards-big">15+</div>
              <div class="awards-years">Years of real estate service.</div>
              <p>Recognized for sales performance, consistency, and long-standing professional service.</p>
            </div>
          </div>
          <div class="awards-list">
            <article class="award-row">
              <div class="award-rank">Top 2%</div>
              <div><h3>Red Diamond Award</h3><span>2021 · National performance</span><small>Royal LePage network · 19,000+ REALTORS®</small></div>
            </article>
            <article class="award-row">
              <div class="award-rank">Top 10%</div>
              <div><h3>President's Gold Award</h3><span>2020 · Regional performance</span><small>Royal LePage network · 18,000+ REALTORS®</small></div>
            </article>
            <article class="award-row">
              <div class="award-rank">15 Years</div>
              <div><h3>Service Milestone</h3><span>Recognized 2022</span><small>Continuous professional service</small></div>
            </article>
            <article class="award-row">
              <div class="award-rank">Top 11%</div>
              <div><h3>TRREB Market Performance</h3><span>2022 · Market-wide ranking</span><small>TRREB performance statistics</small></div>
            </article>
          </div>
        </div>
        <div class="awards-note">Career recognition shown above reflects achievements earned across Abir Hlal's professional history and does not imply current affiliation with prior brokerages.</div>
      </div>
    </section>

    <section class="testimonials"'''
s, n = old_html.subn(new_html, s, count=1)
if n != 1:
    raise SystemExit('Awards HTML block not found')

s = s.replace('.awards-grid{grid-template-columns:1fr 1fr}', '.awards-layout{grid-template-columns:1fr}.awards-feature{min-height:390px}.awards-list{min-height:520px}')
s = s.replace('.awards-grid{grid-template-columns:1fr}.award-card{min-height:190px}', '.awards{padding:48px 0}.awards-layout{grid-template-columns:1fr}.awards-feature{min-height:360px;padding:30px 24px}.awards-watermark{width:68%;right:-38px;top:28px}.awards-list{display:block;min-height:0}.award-row{grid-template-columns:1fr;gap:10px;padding:24px}.award-rank{font-size:38px}')

p.write_text(s)
