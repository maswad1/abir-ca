from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
old_css='''    .testimonials{padding:64px 0;background:#0b0b0c;border-top:1px solid var(--line)}
    .testimonials-head{text-align:center;max-width:760px;margin:0 auto 30px}
    .testimonials-head h2{margin:10px 0 14px}
    .testimonials-head p{margin:0;color:var(--muted);font-size:14px;line-height:1.7}
    .testimonial-shell{max-width:900px;margin:0 auto;padding:42px;border:1px solid #2b2925;background:linear-gradient(145deg,#171719,#101011);position:relative}
    .testimonial-shell:before{content:"“";position:absolute;top:10px;left:24px;font:80px/1 var(--serif);color:rgba(201,166,107,.18)}
    .testimonial-placeholder{text-align:center;padding:18px 10px}
    .testimonial-placeholder strong{display:block;font:600 27px/1.2 var(--serif);color:var(--ink);margin-bottom:12px}
    .testimonial-placeholder span{display:block;color:var(--muted);font-size:14px;line-height:1.7;max-width:600px;margin:0 auto}
    .testimonial-placeholder .btn{margin-top:24px}
'''
new_css='''    .testimonials{padding:72px 0;background:#0b0b0c;border-top:1px solid var(--line)}
    .testimonial-stage{display:grid;grid-template-columns:.92fr 1.08fr;min-height:430px;border:1px solid #2b2925;background:#121214;overflow:hidden}
    .testimonial-photo{position:relative;min-height:430px;overflow:hidden}
    .testimonial-photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 22%}
    .testimonial-photo:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.05),rgba(0,0,0,.64))}
    .testimonial-quote-mark{position:absolute;z-index:2;left:28px;bottom:16px;font:120px/1 var(--serif);color:rgba(223,191,134,.76)}
    .testimonial-copy{padding:48px;display:flex;flex-direction:column;justify-content:center}
    .testimonial-copy h2{margin:10px 0 18px}
    .testimonial-lead{margin:0;color:#d4cec7;font:500 21px/1.45 var(--serif);max-width:520px}
    .testimonial-note{margin:18px 0 0;color:var(--muted);font-size:13px;line-height:1.7;max-width:520px}
    .testimonial-tags{display:flex;gap:10px;flex-wrap:wrap;margin:26px 0 28px}
    .testimonial-tags span{padding:8px 12px;border:1px solid #3a342d;color:var(--gold2);font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
    .testimonial-copy .btn{align-self:flex-start}
    .testimonial-integrity{margin-top:18px;color:#77716a;font-size:10px;line-height:1.55;letter-spacing:.03em;text-transform:uppercase}
'''
old_html='''    <section class="testimonials" id="testimonials">
      <div class="wrap">
        <div class="testimonials-head">
          <div class="eyebrow">Client Testimonials</div>
          <h2>What clients say.</h2>
          <p>Real experiences matter. This section is reserved for verified feedback from Abir's buyers and sellers.</p>
        </div>
        <div class="testimonial-shell">
          <div class="testimonial-placeholder">
            <strong>Client stories are being gathered.</strong>
            <span>Verified testimonials will be added here as they are collected, so every quote shown on Abir.ca reflects an authentic client experience.</span>
            <a class="btn dark" href="mailto:abir.realtor@abir.ca?subject=Client%20Testimonial%20for%20Abir.ca">Share your experience</a>
          </div>
        </div>
      </div>
    </section>
'''
new_html='''    <section class="testimonials" id="testimonials">
      <div class="wrap">
        <div class="testimonial-stage">
          <div class="testimonial-photo">
            <img src="pictures/abir_photo_7.png" alt="Portrait of Abir Hlal">
            <div class="testimonial-quote-mark">“</div>
          </div>
          <div class="testimonial-copy">
            <div class="eyebrow">Client Testimonials</div>
            <h2>Real stories.<br>Verified only.</h2>
            <p class="testimonial-lead">Every testimonial shown on Abir.ca will come from an authentic buyer or seller experience.</p>
            <p class="testimonial-note">As verified feedback is collected, client quotes will appear here without edited or invented endorsements.</p>
            <div class="testimonial-tags"><span>Buyers</span><span>Sellers</span><span>Referrals</span></div>
            <a class="btn gold" href="mailto:abir.realtor@abir.ca?subject=Client%20Testimonial%20for%20Abir.ca">Share your experience</a>
            <div class="testimonial-integrity">Authenticity over filler. No placeholder reviews.</div>
          </div>
        </div>
      </div>
    </section>
'''
if old_css not in s: raise SystemExit('old testimonials css not found')
if old_html not in s: raise SystemExit('old testimonials html not found')
s=s.replace(old_css,new_css,1).replace(old_html,new_html,1)
s=s.replace('.testimonials{padding:48px 0}.testimonial-shell{padding:32px 22px}.testimonial-placeholder .btn{width:100%}', '.testimonials{padding:48px 0}.testimonial-stage{grid-template-columns:1fr}.testimonial-photo{min-height:340px}.testimonial-copy{padding:32px 24px}.testimonial-copy .btn{width:100%}',1)
s=s.replace('.awards-grid{grid-template-columns:1fr 1fr}.events-grid', '.awards-grid{grid-template-columns:1fr 1fr}.testimonial-stage{grid-template-columns:1fr 1fr}.events-grid',1)
p.write_text(s,encoding='utf-8')
