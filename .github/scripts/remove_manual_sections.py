from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Remove navigation items that require ongoing manual content.
s=s.replace('<a href="#testimonials">Testimonials</a><a href="#events">Events</a>', '')

# Turn the activity section into evergreen service/process content.
s=s.replace('<div><div class="eyebrow">Real Estate, In Motion</div><h2>Hands-on from start to finish.</h2></div>', '<div><div class="eyebrow">How Abir Works</div><h2>Personal. Prepared. Strategic.</h2></div>')
s=s.replace('<p>Property presentation, market preparation, and personal guidance — with Abir involved at every stage.</p>', '<p>A clear, hands-on approach to presenting, preparing, and guiding every real-estate move.</p>')
s=s.replace('<div class="activity-copy"><div class="activity-status">Property Showcase</div><h3>Presenting homes with purpose.</h3></div>', '<div class="activity-copy"><div class="activity-status">Property Presentation</div><h3>Present every home with purpose.</h3></div>')
s=s.replace('<div class="activity-copy"><div class="activity-status">Preparation</div><h3>Details matter before launch.</h3></div>', '<div class="activity-copy"><div class="activity-status">Market Preparation</div><h3>Prepare every detail before launch.</h3></div>')
s=s.replace('<div class="activity-copy"><div class="activity-status">Personal Guidance</div><h3>One advisor. Every step.</h3></div>', '<div class="activity-copy"><div class="activity-status">Personal Guidance</div><h3>Guidance from first conversation to closing.</h3></div>')

# Remove Testimonials / Client Stories completely.
s, n1 = re.subn(r'\n\s*<section class="testimonials" id="testimonials">.*?</section>\s*', '\n', s, count=1, flags=re.S)
# Remove Events & Community completely.
s, n2 = re.subn(r'\n\s*<section class="events" id="events">.*?</section>\s*', '\n', s, count=1, flags=re.S)

if n1 != 1:
    raise SystemExit('Testimonials section not found')
if n2 != 1:
    raise SystemExit('Events section not found')

# Remove their top-level CSS blocks to keep the page clean.
s = re.sub(r'\n\s*\.testimonials\{.*?(?=\n\s*\.events\{)', '\n', s, count=1, flags=re.S)
s = re.sub(r'\n\s*\.events\{.*?(?=\n\s*\.cta\{)', '\n', s, count=1, flags=re.S)

# Remove unused responsive references to these deleted sections.
s=s.replace('.events-grid{grid-template-columns:1fr 1fr}.event-card:last-child{grid-column:1/-1}', '')
s=s.replace('.testimonials{padding:48px 0}.testimonial-stage{grid-template-columns:1fr}.testimonial-photo{min-height:340px}.testimonial-copy{padding:32px 24px}.testimonial-copy .btn{width:100%}', '')
s=s.replace('.events{padding:48px 0}.events-head{display:block}.events-head p{margin-top:14px}.events-grid{grid-template-columns:1fr}.event-card:last-child{grid-column:auto}.event-card{min-height:225px}', '')
s=s.replace('.testimonial-stage{grid-template-columns:1fr 1fr}', '')

p.write_text(s, encoding='utf-8')
