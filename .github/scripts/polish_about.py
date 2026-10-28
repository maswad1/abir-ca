from pathlib import Path
import re

p = Path('index.html')
s = p.read_text()

old_about = re.compile(r'    <section class="about" id="about">.*?    </section>\n\n    <section class="showcase" id="listings">', re.S)
new_about = '''    <section class="about about-editorial" id="about">
      <div class="wrap about-editorial-grid">
        <div class="about-visual">
          <img src="pictures/abir_photo_3.png" alt="Abir Hlal standing in front of a luxury home">
          <div class="about-badge"><span>ABIR HLAL</span><strong>Real estate with clarity.</strong></div>
        </div>
        <div class="about-story">
          <div class="eyebrow">About Abir</div>
          <h2>Personal service.<br>Serious strategy.</h2>
          <p class="about-short">Clear advice, careful preparation and calm guidance from first conversation to closing.</p>
          <div class="about-values"><span>Buy</span><span>Sell</span><span>Invest</span></div>
          <button class="btn gold" type="button" onclick="openIntroVideo()">Watch Abir's intro</button>
        </div>
        <div class="about-mini-photo"><img src="pictures/abir_photo_7.png" alt="Portrait of Abir Hlal"></div>
      </div>
    </section>

    <section class="showcase" id="listings">'''

if not old_about.search(s):
    raise SystemExit('About section not found')
s = old_about.sub(new_about, s, count=1)

css = '''
    .about-editorial{padding:58px 0;background:#101012}
    .about-editorial-grid{display:grid;grid-template-columns:1.15fr .9fr .48fr;gap:24px;align-items:stretch}
    .about-visual{position:relative;min-height:430px;overflow:hidden;border:1px solid #262629}
    .about-visual img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 32%}
    .about-visual:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 45%,rgba(0,0,0,.72))}
    .about-badge{position:absolute;z-index:2;left:28px;right:28px;bottom:24px;display:flex;align-items:end;justify-content:space-between;gap:20px;border-top:1px solid rgba(255,255,255,.35);padding-top:16px}
    .about-badge span{color:var(--gold2);font-size:10px;font-weight:700;letter-spacing:.12em}
    .about-badge strong{font:600 24px/1.1 var(--serif);max-width:220px;text-align:right}
    .about-story{padding:40px 28px;background:#171719;border:1px solid #262629;display:flex;flex-direction:column;justify-content:center}
    .about-story h2{margin:12px 0 20px}
    .about-short{margin:0 0 24px;color:var(--muted);font-size:14px;line-height:1.7;max-width:430px}
    .about-values{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:28px}
    .about-values span{border:1px solid #3a342d;color:var(--gold2);padding:8px 12px;font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
    .about-story .btn{align-self:flex-start}
    .about-mini-photo{min-height:430px;overflow:hidden;border:1px solid #262629}
    .about-mini-photo img{width:100%;height:100%;object-fit:cover;object-position:center 20%}

    @media(max-width:980px){
      .about-editorial-grid{grid-template-columns:1fr 1fr}.about-mini-photo{display:none}.about-visual{min-height:410px}
    }
    @media(max-width:620px){
      .about-editorial{padding:42px 0}.about-editorial-grid{grid-template-columns:1fr}.about-visual{min-height:390px}.about-story{padding:30px 24px}.about-badge{left:20px;right:20px}.about-badge strong{font-size:20px}.about-story .btn{width:100%}
    }
'''
if '.about-editorial-grid{' not in s:
    s = s.replace('  </style>', css + '  </style>')

old_js = "    document.getElementById('playVideo').addEventListener('click',()=>{dialog.showModal();video.currentTime=0;video.play().catch(()=>{})});"
new_js = "    function openIntroVideo(){dialog.showModal();video.currentTime=0;video.play().catch(()=>{})}"
if old_js in s:
    s = s.replace(old_js, new_js)
elif 'function openIntroVideo()' not in s:
    raise SystemExit('Video trigger JS not found')

p.write_text(s)
