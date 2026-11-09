import csv
K="https://select.keenable.ai/r/lean-ai-products-at-1m-arr-2025-sep-2026/WwKmTVPhPPZWlOclJqrBSg"
T="https://tinyteams.xyz/"; S="https://shippedandpaid.com/"
TS="historical snapshot on tinyteams.xyz; milestone date not stated"
# name,url,team,rev_usd_annual,revenue_text,funding,bv,category,source,as_of,conf,notes
R=[
("Cal AI","https://www.calai.app",15,24e6,"$24M ARR","","","Consumer health app",T,"","self-reported","Acquired by MyFitnessPal (closed Dec 2025, announced 2026-03-02 per TechCrunch/MFP). Inc. (Mar 2026): ~30 employees, $40M sales in 12 months. Listing figure 15 people / $24M ARR is tinyteams.xyz, undated. Checked 2026-10-23"),
("Rosebud AI Journal","https://www.rosebud.app",5,1e6,"$1M ARR","","","Consumer wellness","https://montethakkar.com/resume.pdf","2025","self-reported","Source is a founder resume"),
("SeoBot","https://seobotai.com",1,1e6,"$1M ARR","","","Marketing / SEO agent","https://www.vccafe.com/nano-unicorns-in-the-making/","2025","self-reported","tinyteams.xyz lists 2 people / $1.2M ARR"),
("Base44","https://base44.com",1,3.5e6,"$3.5M ARR","","bootstrapped","AI app builder","https://wearefounders.uk/from-solo-builder-to-80m-exit-the-base44-story","2025-06-18","self-reported","Matches source. Acquired by Wix (~$80M) Jun 2025; tinyteams.xyz lists $2M ARR"),
("Swan AI","https://www.swan.ai",3,1e6,"$1M ARR","","","Sales / GTM agents","https://ryan-estes.beehiiv.com/p/6m-in-9-months-1m-in-8-weeks-and-why-billionaires-want-to-live-forever","2025","self-reported",""),
("Arcads","https://www.arcads.ai",4,5e6,"$5M ARR","","","AI video ads",T,"","self-reported","Re-check 2026-10-21: replaced secondary Medium claim (5 people/$10M) with tinyteams.xyz listing (4 people/$5M), undated; a Mar 2026 Substack says ~10 people"),
("Magic Patterns","https://www.magicpatterns.com",2,1e6,"$1M ARR","","vc","AI UI design","https://rosetta.to/u/ycrootaccess","2025","self-reported","YC company"),
("Magnific","https://magnific.ai",2,6e6,"$6M ARR","","bootstrapped","AI image upscaling","https://chalsarboleya.substack.com/p/europes-ai-champions-and-the-gtm","pre-2025","self-reported","Source (Mar 2026): $6M ARR with 2 people before Freepik acquisition; now ~$30M ARR inside Freepik. tinyteams.xyz says $10M"),
("Polsia","https://polsia.com",1,1e6,"$1M ARR (reported within 30 days)","","","AI agents for businesses","https://contextstudios.ai/blog/polsia-how-a-solo-founder-hit-1m-arr-in-30-days-with-ai-agents","2026","self-reported",""),
("Maggi AI","",1,1e6,"$1M ARR","","bootstrapped","AI assistant","https://kblip.com/news/solo-founder-builds-maggi-ai-to-1m-arr-in-12-months-without-5qJxBRl","2026","self-reported","Reported as built without VC"),
("Gauge","",5,2e6,"$2M ARR","","","AI search visibility","https://insights.tryspecter.com/specter-monitor-241","2026","estimate","Secondary newsletter"),
("Loman","https://loman.ai",2,1.5e6,"$1.5M ARR","","","AI phone agent (restaurants)",K,"2025-08","estimate","Keenable row had incomplete source"),
("CHAI","https://www.chai-research.com",12,30e6,"$30M+ ARR","","","Consumer social AI","https://aijourn.com/chai-reaches-over-30m-in-arr-with-only-12-employees/","2025-03-28","self-reported","Company press release (PR Newswire) covered by AI Journal 2025-03-28; confirmed live 2026-10-23"),
("Lovable","https://lovable.dev",18,30e6,"$30M ARR","","vc","AI app builder","https://www.growthunhinged.com/p/lovable-growth-story","2025-04-02","self-reported","Team grew to 45 by Jul 2025; now well above 20"),
('Recall.ai', 'https://www.recall.ai', 19, 10000000, '$10M+ ARR', '', 'vc', 'Meeting bot API', 'https://www.heysam.ai/blog/one-table-companies', '2025-01', 'estimate', 'Research correction observed 2026-11-08; Editor correction pass 2026-11-08: Historical team 19 (Jan 2025 source) cannot establish current eligibility. No current headcount established in captured evidence; current <=20 eligibility UNKNOWN. No uncaptured LinkedIn range or search-index count is asserted. Original historical notes (NOT a current assertion): Third-party blog'),
('RB2B', 'https://www.rb2b.com', 7, None, '$4M (first 9 months)', '', 'bootstrapped', 'B2B visitor identification', 'https://www.heysam.ai/blog/one-table-companies', '2024', 'self-reported', 'Research correction observed 2026-11-08: $4M in first nine months is cumulative period revenue, not $4M ARR or a comparable recurring annual metric. No new revenue source read. Original historical notes (NOT a current assertion): '),
("Floqer","https://www.floqer.com",8,1.2e6,"$1.2M+ ARR","$2M pre-seed (Sep 2025)","vc","Sales data / AI agents","https://www.webpronews.com/floqers-fleet-of-ai-agents-takes-over-the-tedious-work-of-b2b-customer-research/","2026-10-15","self-reported","Company says passed $1.2M ARR with 8 employees (WebProNews, TechCrunch Disrupt 2026 coverage). Earlier: 9 people, seven-figure ARR (The Logic, 2026-08). Checked 2026-10-26"),
("Hivelighter","",9,None,"","","","AI","https://thelogic.co/news/analysis/ai-startups-millions-tiny-teams/","2026-08","self-reported","Targeting $13M ARR by 2028 (goal, not revenue)"),
("bolt.new","https://bolt.new",15,40e6,"$40M ARR",  "","vc","AI app builder",T,"","self-reported",TS),
("Midjourney","https://www.midjourney.com",10,200e6,"$200M ARR","","bootstrapped","AI image generation",T,"","estimate",TS+"; team now far larger"),
("Cursor (Anysphere)","https://cursor.com",20,200e6,"$200M ARR","","vc","AI coding",T,"","estimate",TS+"; team now far larger"),
("Twofold","https://www.trytwofold.com",3,5e6,"$5M ARR","","","AI medical scribe",T,"","self-reported",TS),
("VSTRAT.ai","https://vstrat.ai",3,1.8e6,"$1.8M ARR","","","AI management tools",T,"","self-reported",TS),
("DittoDub","https://dittodub.com",4,3.8e6,"$3.8M ARR","","","AI dubbing",T,"","self-reported",TS),
("Submagic","https://www.submagic.co",14,7e6,"$7M ARR","","","AI captions",T,"","self-reported",TS),
("sync.so","https://sync.so",19,4e6,"$4M ARR","","vc","AI lipsync",T,"","self-reported",TS),
("Develop Health","https://www.develophealth.ai",5,7e6,"$7M ARR","","vc","Healthcare AI",T,"","self-reported",TS),
("Anara","https://anara.com",6,3.5e6,"$3.5M ARR","","","AI for researchers",T,"","self-reported",TS),
("Samplead","https://www.samplead.co",9,1.7e6,"$1.7M ARR","","","AI SDR agents",T,"","self-reported",TS),
("Aragon.ai","https://www.aragon.ai",9,10e6,"$10M ARR","","","AI headshots",T,"","self-reported",TS),
("Rendernet AI","https://rendernet.ai",10,5e6,"$5M ARR","","","AI image generation",T,"","self-reported",TS),
("Vapi","https://vapi.ai",20,8e6,"$8M ARR","","vc","Voice AI platform",T,"","self-reported","20 people was a historical tinyteams.xyz snapshot. Tracxn: 150 employees as of 2026-09-30; TechCrunch 2026-05-12: ~100. Checked 2026-10-23"),
("Jenni AI","https://jenni.ai",20,10e6,"$10M ARR","","","AI writing / research",T,"","self-reported",TS),
("Icon","https://icon.com",8,5e6,"$5M ARR","","vc","AI ad maker",T,"","self-reported",TS),
("Chatbase","https://www.chatbase.co",11,5e6,"$5M ARR","","bootstrapped","AI chatbots",T,"","self-reported",TS),
("Oleve","https://oleve.com",5,6e6,"$6M ARR","","","Consumer AI apps",T,"","self-reported",TS),
('HeadshotPro', 'https://www.headshotpro.com', 1, None, 'Historical $3M source-labelled ARR; recurring nature unvalidated; current pricing one-time', '', 'bootstrapped', 'AI headshots', 'https://tinyteams.xyz/', '', 'self-reported', 'Research correction observed 2026-11-08: Current primary pricing explicitly nonrecurring; historical third-party ARR label is not validated. Exclude from comparable recurring set; keep historical claim. Original historical notes (NOT a current assertion): historical snapshot on tinyteams.xyz; milestone date not stated'),
("Photo AI / levelsio products","https://levels.io",1,3.1e6,"~$3.1M/yr (portfolio)","","bootstrapped","AI photo + indie portfolio","https://www.operatorbook.dev/stories/pieter-levels-revenue-never-sell-solo-portfolio","2025-07","self-reported","Whole portfolio (Photo AI, Nomad List, Remote OK, etc.), not Photo AI alone: Levels on Stripe Cheeky Pint, Jul 2025, ~$3.1M/yr solo; Photo AI alone ~$600K ARR. tinyteams.xyz lists $3M. Checked 2026-10-23"),
('Interview Coder', 'https://www.interviewcoder.co', 2, 2000000, '$2M ARR', '', '', 'AI interview tool', 'https://tinyteams.xyz/', '', 'self-reported', 'Research correction observed 2026-11-08: Already-recorded Apr 2025 merger into Cluely means not a current standalone two-person business; do not count twice. Carry-forward provenance, not a newly checked merger. Original historical notes (NOT a current assertion): Historical tinyteams.xyz snapshot, undated. Interview Coder was folded into Cluely (Apr 2025, TechCrunch); founder Roy Lee now runs Cluely (16+ staff by Jul 2025). Checked 2026-10-23'),
("Kleo","https://www.kleo.so",None,61910*12,"$61,910 MRR",  "","","AI LinkedIn writing",S,"2025-12","self-reported","Polar dashboard shared on X; team size not stated"),
("Dropmagic","https://www.dropmagic.ai",None,120000*12,"$120K MRR","","","AI e-commerce store builder",S,"2026-10","self-reported","Co-founder on X; team size not stated"),
('Revid', 'https://www.revid.ai', 'about 4', None, 'More than 600,000/month; currency not stated', '', '', 'AI short video', 'https://shippedandpaid.com/cases/revid-ai-short-video-generator-600k-month-cursor/', '2026-04-26', 'self-reported', 'Research correction observed 2026-11-08; Editor correction pass 2026-11-08: Founder interview says team about four, not exactly four; team field is about 4. Currency unspecified, so USD annualized and per-employee conversions remain cleared. Acquired Typeframe then pivoted; not AI-built from zero. Original historical notes (NOT a current assertion): Interview; currency not stated'),
('Post Bridge', 'https://www.post-bridge.com', None, 596796, '$49,733 MRR', '', '', 'Social media scheduling', 'https://trustmrr.com/startup/post-bridge', '2026-11-08', 'verified', 'Research correction observed 2026-11-08: Fresh Stripe MRR; distinguish receipts; build method documented, product itself not AI-centric. Original historical notes (NOT a current assertion): TrustMRR Stripe-verified'),
('SuperX', 'https://superx.so', None, 228996, '$19,083 MRR', '', '', 'X growth tool', 'https://trustmrr.com/startup/superx', '2026-11-08', 'verified', 'Research correction observed 2026-11-08: Fresh Stripe MRR below stored $22,281; no inference about category failure. Original historical notes (NOT a current assertion): TrustMRR Stripe-verified'),
('GETebook.ai', 'https://getebook.ai', 1, 132216, '$32,970 last 30 days; $11,018 MRR', '', '', 'AI ebook writer', 'https://trustmrr.com/startup/getebook-ai', '2026-11-08', 'verified', 'Research correction observed 2026-11-08; Editor correction pass 2026-11-08: Separate $32,970 rolling 30-day receipts from $11,018 MRR. Annualized field is $132,216 MRR-based recurring run rate (11,018 x12), not receipts x12 or recognized annual revenue. Team self-reported one; no profit disclosure. Original historical notes (NOT a current assertion): TrustMRR Stripe-verified; annualized from 30 days'),
('SocialCrawl', 'https://socialcrawl.dev', None, 12972, '$43,950 last 30 days; $1,081 MRR', '', '', 'Social data API for AI agents', 'https://trustmrr.com/startup/socialcrawl', '2026-11-08', 'verified', 'Research correction observed 2026-11-08; Editor correction pass 2026-11-08: Separate $43,950 rolling 30-day receipts from $1,081 MRR. Annualized field is $12,972 MRR-based recurring run rate (1,081 x12), not receipts x12 or recognized annual revenue. Pricing GBP, dashboard USD. Original historical notes (NOT a current assertion): TrustMRR Stripe-verified; annualized from 30 days'),
("ChartDetector AI","",2,56000*12,"$56K/month","","","AI trading chart analysis",S,"2026-07","self-reported","Two brothers per Starter Story"),
("Coherence","",2,None,"~85,000 total in 8 months (currency not stated)","","","Breathwork app",S,"2025-11","self-reported","Two brothers"),
("Cat on Chair","",2,18000*12,"~$18K/month","","","Focus timer app",S,"2026-07","self-reported","Founder and partner"),
("AppAlchemy","https://www.appalchemy.ai",1,17000*12,"~$17K MRR","","","AI app design",S,"2025-07","self-reported","Run by one founder"),
("ContextBolt","",1,653*12,"$653/month","","","SEO MCP server",S,"2026-09","self-reported","Solo founder"),
("TrustMRR","https://trustmrr.com",1,None,"~$300K revenue in first 9 months","","bootstrapped","Revenue verification marketplace",S,"2026-09-01","self-reported","Marc Lou, solo"),
("BoldVoice","https://www.boldvoice.com",10,10e6,"~$10M ARR","$21M Series A (Jan 2026)","vc","AI speech / accent coaching","https://startupeable.com/en/boldvoice-audio-ai-lab/","2026-07-25","self-reported","CEO interview: team of 10 at ~$10M ARR (7 people at the Jan 2026 Series A, per PR Newswire). Plans 20-25 people by end of 2026; Graduated 2026-11-02: LinkedIn and TipRanks show 27 employees (Oct 26 2026), Tracxn 22 (May 2026). Checked 2026-11-02"),
('Halluminate', 'https://halluminate.ai', 9, None, 'Mid-eight-figure annualized run rate', '$38.5M total ($30M Series A, Oct 2026)', 'vc', 'AI training environments (finance)', 'https://fortune.com/2026/10/01/halluminate-raises-30-million-series-a-oakhc-ft/', '2026-10-01', 'self-reported', 'Research correction observed 2026-11-08; Editor correction pass 2026-11-08: Retain the nine-person Oct 1, 2026 Fortune historical snapshot. No current headcount established in captured evidence; current <=20 eligibility UNKNOWN. Do not assert unsubstantiated later profile counts. Original historical notes (NOT a current assertion): Nine people; CEO told Fortune run rate passed mid-eight figures and it is profitable. Exact figure not disclosed, so no per-employee number. Checked 2026-10-26'),
("Shipper","https://shipper.now",3,25600*12,"$25.6K MRR (~$307K ARR)","","bootstrapped","AI app builder","https://www.starterstory.com/shipper","2026-05-29","estimate","Stripe dashboard shown on Starter Story: $25.6K MRR, $307K ARR. Team size estimated: two founder brothers plus one developer at the start. Checked 2026-10-26"),
("Lancer","https://lancer.app",2,10000*12,"~$10K MRR","","bootstrapped","AI agent for Upwork bidding","https://www.starterstory.com/stories/lancer","2026-01-10","self-reported","Starter Story profile: 2 founders, 0 employees, ~$10K MRR for several months. Checked 2026-10-26"),
('Postiz', 'https://postiz.com', 4, 4652772, '$387,731 MRR', '', 'bootstrapped', 'Agentic social media scheduling', 'https://trustmrr.com/startup/postiz', '2026-11-08', 'verified', 'Research correction observed 2026-11-08: Fresh Stripe MRR; not $424,355 30-day receipts. Historical team 4 not reverified. Original historical notes (NOT a current assertion): TrustMRR Stripe-verified MRR (10,324 active subscriptions). Founder Nevo David reported $348,430 for Oct 2026 and said he hired 3 people; LinkedIn lists 4. Checked 2026-11-02'),
('GojiberryAI', 'https://gojiberry.ai', 11, 5092416, '$424,368 MRR', 'YC', 'vc', 'AI sales signals / outbound', 'https://trustmrr.com/startup/superfruits', '2026-08-14', 'provider-verified historical; stale', 'Research correction observed 2026-11-08: Provider explicitly says API key expired; last sync Aug 14. Nov 2 was observation, not financial fact date. Retain amount as stale. Original historical notes (NOT a current assertion): TrustMRR leaderboard shows Stripe-verified MRR of $424,368 (2026-11-02); CMO Romàn Czerny said $4.5M ARR on 2026-10-05. Team of 11, profitable and bootstrapped before YC, per a Sep 2026 podcast (earlier reports said 8). Checked 2026-11-02'),
("InstaAgent","https://instaagent.com",6,1e6,"$1M ARR","YC","vc","AI ad creative (persona variants)","https://www.founderland.ai/articles/ycs-instaagent-hits-1m-arr-in-10-months-with-ai-marketing-pi-mpqr8b7q","2026-05-29","self-reported","$1M ARR 10 months after founding; YC profile lists 6 people (LinkedIn shows 9 profiles). Now an AI-enabled agency model. Checked 2026-11-02"),
]
GRAD={"Interview Coder","Cursor (Anysphere)","Midjourney","Lovable","bolt.new","Base44","Magnific","Cal AI","Vapi","BoldVoice"}
cols="status,name,url,team_size,revenue,revenue_annualized_usd,revenue_per_employee,funding_raised,bootstrapped_or_vc,category,source_url,as_of_date,confidence,notes".split(",")
with open("data/companies.csv","w",newline="") as f:
  w=csv.writer(f);w.writerow(cols)
  for n,u,t,ra,rt,fu,bv,c,s,a,cf,no in R:
    rpe=round(ra/t) if (ra and isinstance(t, (int, float)) and t and n not in ['GETebook.ai', 'Postiz', 'GojiberryAI']) else ""
    w.writerow(["graduated" if n in GRAD else "active",n,u,t if t else "",rt,int(ra) if ra else "",rpe,fu,bv,c,s,a,cf,no])
print(len(R))

# ---- per-company pages, sitemap, robots ----
import re,os,html,datetime
SITE="https://leanledger.co";TALLY="https://tally.so/r/Ar7GEN";SUB="https://rationalreturns.substack.com/subscribe"
def slug(n): return re.sub(r"[^a-z0-9]+","-",n.lower()).strip("-")
def money(x): return f"${int(x):,}" if x not in ("",None) else "not disclosed"
rows=list(csv.DictReader(open("data/companies.csv")))
# add slug column
for r in rows: r["slug"]=slug(r["name"])
with open("data/companies.csv","w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=cols+["slug"]);w.writeheader();w.writerows(rows)
e=html.escape;today=datetime.date.today().isoformat();urls=[SITE+"/"]
for r in rows:
  n=e(r["name"]);d=f"c/{r['slug']}";os.makedirs(d,exist_ok=True)
  t=f"{r['name']} revenue per employee, team size & funding | Lean Ledger"
  desc=f"{r['name']}: team of {r['team_size'] or 'undisclosed size'}, revenue {r['revenue'] or 'not disclosed'}, revenue per employee {money(r['revenue_per_employee'])}. Label: {r['confidence']}. Sourced."
  grad='<p class="g"><b>Graduated:</b> now over 20 people or part of a larger company. Kept as a historical snapshot and left out of the ranking.</p>' if r["status"]=="graduated" else ""
  site=f'<a href="{e(r["url"])}" rel="noopener">{e(r["url"])}</a>' if r["url"] else "not listed"
  rowsh="".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k,v in [("Website",site),("Category",e(r["category"])),("Team size",e(r["team_size"] or "not stated")),("Revenue (as stated)",e(r["revenue"] or "not disclosed")),("Annualized revenue",money(r["revenue_annualized_usd"])),("Revenue per employee",money(r["revenue_per_employee"])),("Funding",e(r["funding_raised"] or "not disclosed")),("Bootstrapped or raised",{"vc":"Raised","bootstrapped":"Bootstrapped"}.get(r["bootstrapped_or_vc"],"unknown")),("Data label",f'<span class="tag {e(r["confidence"])}">{e(r["confidence"])}</span>'),("As of",e(r["as_of_date"] or "undated in source")),("Source",f'<a href="{e(r["source_url"])}" rel="noopener">{e(r["source_url"])}</a>'),("Notes",e(r["notes"]))])
  open(f"{d}/index.html","w").write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(t)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{SITE}/{d}/">
<meta property="og:type" content="article"><meta property="og:title" content="{e(t)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{SITE}/{d}/"><meta property="og:site_name" content="Lean Ledger"><meta name="twitter:card" content="summary">
<style>body{{font-family:system-ui,sans-serif;max-width:720px;margin:2rem auto;padding:0 1rem;color:#111}}table{{border-collapse:collapse;width:100%}}th,td{{text-align:left;padding:.45rem;border-bottom:1px solid #eee;vertical-align:top;word-break:break-word}}th{{width:35%;color:#555;font-weight:500}}.tag{{padding:2px 6px;border-radius:4px;background:#eee}}.verified{{background:#d4f5dc}}.self-reported{{background:#fff3c4}}.estimate{{background:#fde0e0}}.g{{background:#f3f0ff;padding:.6rem}}nav a{{margin-right:1rem}}</style></head><body>
<nav><a href="/">← All companies</a><a href="{TALLY}">Submit a company</a><a href="{SUB}">Subscribe</a></nav>
<h1>{n}</h1><p>{e(r["category"])}. Part of <a href="/">Lean Ledger</a>, a sortable database of AI companies with 20 or fewer people.</p>{grad}
<table>{rowsh}</table>
<p><small>"Verified" means revenue checked against a payment provider (e.g. Stripe via TrustMRR). "Self-reported" means a founder or company claim. "Estimate" means a third-party figure. Know a correction? <a href="{TALLY}">Send it with a source</a>.</small></p>
<p>Get new tiny AI companies weekly in the Lean Ledger section of Rational Returns.</p><iframe src="https://rationalreturns.substack.com/embed" title="Subscribe to Rational Returns" style="width:100%;max-width:480px;height:130px;border:1px solid #e5e7eb;border-radius:8px;background:#fff" frameborder="0" scrolling="no" loading="lazy"></iframe><script data-goatcounter="https://leanledger.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script></body></html>''')
  urls.append(f"{SITE}/{d}/")
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("pages",len(rows))
