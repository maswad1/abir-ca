from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
old='''          <div class="testimonial-copy">
            <div class="eyebrow">Client Testimonials</div>
            <h2>Real stories.<br>Verified only.</h2>
            <p class="testimonial-lead">Every testimonial shown on Abir.ca will come from an authentic buyer or seller experience.</p>
            <p class="testimonial-note">As verified feedback is collected, client quotes will appear here without edited or invented endorsements.</p>
            <div class="testimonial-tags"><span>Buyers</span><span>Sellers</span><span>Referrals</span></div>
            <a class="btn gold" href="mailto:abir.realtor@abir.ca?subject=Client%20Testimonial%20for%20Abir.ca">Share your experience</a>
            <div class="testimonial-integrity">Authenticity over filler. No placeholder reviews.</div>
          </div>'''
new='''          <div class="testimonial-copy">
            <div class="eyebrow">Client Stories</div>
            <h2>Coming soon.</h2>
            <p class="testimonial-lead">A collection of real client experiences will live here as Abir gathers stories from buyers and sellers.</p>
            <p class="testimonial-note">For now, this space stays simple, elegant, and ready for the first story.</p>
            <a class="btn gold" href="mailto:abir.realtor@abir.ca?subject=Client%20Story%20for%20Abir.ca">Share your experience</a>
          </div>'''
if old not in s:
    raise SystemExit('testimonial block not found')
s=s.replace(old,new,1)
s=s.replace('    .testimonial-tags{display:flex;gap:10px;flex-wrap:wrap;margin:26px 0 28px}\n    .testimonial-tags span{padding:8px 12px;border:1px solid #3a342d;color:var(--gold2);font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}\n','')
s=s.replace('    .testimonial-integrity{margin-top:18px;color:#77716a;font-size:10px;line-height:1.55;letter-spacing:.03em;text-transform:uppercase}\n','')
s=s.replace('    .testimonial-copy .btn{align-self:flex-start}\n','    .testimonial-copy .btn{align-self:flex-start;margin-top:28px}\n',1)
p.write_text(s,encoding='utf-8')
