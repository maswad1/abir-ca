from pathlib import Path
import re

p=Path('index.html')
s=p.read_text()

old_css=re.compile(r'''    \.activity\{padding:68px 0;background:#0b0b0c;border-top:1px solid var\(--line\)\}\n    \.activity-head\{display:flex;justify-content:space-between;align-items:end;gap:28px;margin-bottom:30px\}\n    \.activity-head h2\{margin:10px 0 0\}\n    \.activity-head p\{max-width:480px;color:var\(--muted\);font-size:14px;line-height:1\.7;margin:0\}\n    \.activity-grid\{display:grid;grid-template-columns:repeat\(3,1fr\);gap:20px\}\n    \.activity-card\{min-height:270px;padding:30px;border:1px solid #2b2925;background:linear-gradient\(145deg,#18181a,#101011\);display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden\}\n    \.activity-card:before\{content:"";position:absolute;left:0;top:0;width:100%;height:2px;background:linear-gradient\(90deg,var\(--gold\),transparent\)\}\n    \.activity-status\{color:var\(--gold2\);font-size:11px;font-weight:700;letter-spacing:\.08em;text-transform:uppercase\}\n    \.activity-mark\{font:500 54px/1 var\(--serif\);color:rgba\(223,191,134,\.82\);margin:34px 0\}\n    \.activity-card h3\{font-size:27px;margin:0 0 9px\}\n    \.activity-card p\{margin:0;color:var\(--muted\);font-size:13px;line-height:1\.6\}\n    \.activity-note\{margin-top:18px;color:#817b75;font-size:11px;line-height:1\.6\}''')
new_css='''    .activity{padding:68px 0;background:#0b0b0c;border-top:1px solid var(--line)}
    .activity-head{display:flex;justify-content:space-between;align-items:end;gap:28px;margin-bottom:30px}
    .activity-head h2{margin:10px 0 0}
    .activity-head p{max-width:430px;color:var(--muted);font-size:14px;line-height:1.65;margin:0}
    .activity-grid{display:grid;grid-template-columns:1.12fr .88fr .88fr;gap:18px}
    .activity-photo{position:relative;min-height:360px;overflow:hidden;border:1px solid #2b2925;background:#141416}
    .activity-photo:first-child{min-height:430px}
    .activity-photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
    .activity-photo:first-child img{object-position:center 38%}
    .activity-photo:nth-child(2) img{object-position:center 34%}
    .activity-photo:nth-child(3) img{object-position:center 30%}
    .activity-photo:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.02) 25%,rgba(0,0,0,.82) 100%)}
    .activity-copy{position:absolute;z-index:2;left:24px;right:24px;bottom:22px}
    .activity-status{color:var(--gold2);font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}
    .activity-copy h3{font-size:clamp(24px,2.4vw,34px);margin:8px 0 0;line-height:1.05}
    .activity-copy p{margin:9px 0 0;color:#d0cbc5;font-size:12px;line-height:1.55;max-width:340px}
'''
s,n=old_css.subn(new_css,s,count=1)
if n!=1: raise SystemExit(f'activity css replacement count={n}')

old_html=re.compile(r'''    <section class="activity" id="activity">.*?    </section>\n    <section class="awards"''',re.S)
new_html='''    <section class="activity" id="activity">
      <div class="wrap">
        <div class="activity-head">
          <div><div class="eyebrow">Real Estate, In Motion</div><h2>Hands-on from start to finish.</h2></div>
          <p>Property presentation, market preparation, and personal guidance — with Abir involved at every stage.</p>
        </div>
        <div class="activity-grid">
          <article class="activity-photo">
            <img src="pictures/abir_photo_5.png" alt="Abir Hlal outside a modern home">
            <div class="activity-copy"><div class="activity-status">Property Showcase</div><h3>Presenting homes with purpose.</h3></div>
          </article>
          <article class="activity-photo">
            <img src="pictures/abir_photo_2.png" alt="Abir Hlal inside a bright luxury property">
            <div class="activity-copy"><div class="activity-status">Preparation</div><h3>Details matter before launch.</h3></div>
          </article>
          <article class="activity-photo">
            <img src="pictures/abir_photo_7.png" alt="Portrait of Abir Hlal">
            <div class="activity-copy"><div class="activity-status">Personal Guidance</div><h3>One advisor. Every step.</h3></div>
          </article>
        </div>
      </div>
    </section>
    <section class="awards"'''
s,n=old_html.subn(new_html,s,count=1)
if n!=1: raise SystemExit(f'activity html replacement count={n}')

s=s.replace('.activity-grid{grid-template-columns:1fr 1fr}.activity-card:last-child{grid-column:1/-1}', '.activity-grid{grid-template-columns:1fr 1fr}.activity-photo:first-child{grid-column:1/-1;min-height:460px}')
s=s.replace('.activity-grid{grid-template-columns:1fr}.activity-card:last-child{grid-column:auto}.activity-card{min-height:220px}', '.activity-grid{grid-template-columns:1fr}.activity-photo:first-child{grid-column:auto;min-height:360px}.activity-photo{min-height:330px}')

p.write_text(s)
