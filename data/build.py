import csv
K="https://select.keenable.ai/r/lean-ai-products-at-1m-arr-2025-sep-2026/WwKmTVPhPPZWlOclJqrBSg"
T="https://tinyteams.xyz/"; S="https://shippedandpaid.com/"
TS="historical snapshot on tinyteams.xyz; milestone date not stated"
# name,url,team,rev_usd_annual,revenue_text,funding,bv,category,source,as_of,conf,notes
R=[
("Cal AI","https://www.calai.app",15,24e6,"$24M ARR","","","Consumer health app",T,"","self-reported","Re-check 2026-10-21: earlier 2-person/$21M claim (Indie Hackers) could not be re-verified; using tinyteams.xyz listing of 15 people / $24M ARR, undated"),
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
("CHAI","https://www.chai-research.com",12,30e6,"$30M+ ARR","","","Consumer social AI","https://aijourn.com/chai-reaches-over-30m-in-arr-with-only-12-employees/","2025-03-28","self-reported","PR Newswire release; matches"),
("Lovable","https://lovable.dev",18,30e6,"$30M ARR","","vc","AI app builder","https://www.growthunhinged.com/p/lovable-growth-story","2025-04-02","self-reported","Team grew to 45 by Jul 2025; now well above 20"),
("Recall.ai","https://www.recall.ai",19,10e6,"$10M+ ARR","","vc","Meeting bot API","https://www.heysam.ai/blog/one-table-companies","2025-01","estimate","Third-party blog"),
("RB2B","https://www.rb2b.com",7,4e6,"$4M (first 9 months)","","bootstrapped","B2B visitor identification","https://www.heysam.ai/blog/one-table-companies","2024","self-reported",""),
("Floqer","https://www.floqer.com",9,None,"Seven-figure ARR","$2M pre-seed (Sep 2025)","vc","Sales data / AI agents","https://thelogic.co/news/analysis/ai-startups-millions-tiny-teams/","2026-08","self-reported","Exact ARR not disclosed"),
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
("Vapi","https://vapi.ai",20,8e6,"$8M ARR","","vc","Voice AI platform",T,"","self-reported",TS),
("Jenni AI","https://jenni.ai",20,10e6,"$10M ARR","","","AI writing / research",T,"","self-reported",TS),
("Icon","https://icon.com",8,5e6,"$5M ARR","","vc","AI ad maker",T,"","self-reported",TS),
("Chatbase","https://www.chatbase.co",11,5e6,"$5M ARR","","bootstrapped","AI chatbots",T,"","self-reported",TS),
("Oleve","https://oleve.com",5,6e6,"$6M ARR","","","Consumer AI apps",T,"","self-reported",TS),
("HeadshotPro","https://www.headshotpro.com",1,3e6,"$3M ARR","","bootstrapped","AI headshots",T,"","self-reported",TS),
("Photo AI / levelsio products","https://levels.io",1,3e6,"$3M ARR (portfolio)","","bootstrapped","AI photo + indie portfolio",T,"","self-reported",TS),
("Interview Coder","https://www.interviewcoder.co",2,2e6,"$2M ARR","","","AI interview tool",T,"","self-reported",TS),
("Kleo","https://www.kleo.so",None,61910*12,"$61,910 MRR",  "","","AI LinkedIn writing",S,"2025-12","self-reported","Polar dashboard shared on X; team size not stated"),
("Dropmagic","https://www.dropmagic.ai",None,120000*12,"$120K MRR","","","AI e-commerce store builder",S,"2026-10","self-reported","Co-founder on X; team size not stated"),
("Revid","https://www.revid.ai",None,600000*12,"~$600K/month","","","AI short video",S,"2026-04","self-reported","Interview; currency not stated"),
("Post Bridge","https://www.post-bridge.com",None,48821*12,"$48,821 MRR","","","Social media scheduling",S,"2026-10","verified","TrustMRR Stripe-verified"),
("SuperX","https://superx.so",None,22281*12,"$22,281 MRR","","","X growth tool",S,"2026-10","verified","TrustMRR Stripe-verified"),
("GETebook.ai","https://getebook.ai",None,35469*12,"$35,469 (last 30 days)","","","AI ebook writer",S,"2026-10-21","verified","TrustMRR Stripe-verified; annualized from 30 days"),
("SocialCrawl","https://socialcrawl.dev",None,35135*12,"$35,135 (last 30 days)","","","Social data API for AI agents",S,"2026-10-20","verified","TrustMRR Stripe-verified; annualized from 30 days"),
("ChartDetector AI","",2,56000*12,"$56K/month","","","AI trading chart analysis",S,"2026-07","self-reported","Two brothers per Starter Story"),
("Coherence","",2,None,"~85,000 total in 8 months (currency not stated)","","","Breathwork app",S,"2025-11","self-reported","Two brothers"),
("Cat on Chair","",2,18000*12,"~$18K/month","","","Focus timer app",S,"2026-07","self-reported","Founder and partner"),
("AppAlchemy","https://www.appalchemy.ai",1,17000*12,"~$17K MRR","","","AI app design",S,"2025-07","self-reported","Run by one founder"),
("ContextBolt","",1,653*12,"$653/month","","","SEO MCP server",S,"2026-09","self-reported","Solo founder"),
("TrustMRR","https://trustmrr.com",1,None,"~$300K revenue in first 9 months","","bootstrapped","Revenue verification marketplace",S,"2026-09-01","self-reported","Marc Lou, solo"),
]
GRAD={"Cursor (Anysphere)","Midjourney","Lovable","bolt.new","Base44","Magnific"}
cols="status,name,url,team_size,revenue,revenue_annualized_usd,revenue_per_employee,funding_raised,bootstrapped_or_vc,category,source_url,as_of_date,confidence,notes".split(",")
with open("data/companies.csv","w",newline="") as f:
  w=csv.writer(f);w.writerow(cols)
  for n,u,t,ra,rt,fu,bv,c,s,a,cf,no in R:
    rpe=round(ra/t) if (ra and t) else ""
    w.writerow(["graduated" if n in GRAD else "active",n,u,t if t else "",rt,int(ra) if ra else "",rpe,fu,bv,c,s,a,cf,no])
print(len(R))
