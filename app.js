const COLS=[["name","Company"],["team_size","Team"],["revenue","Revenue (as stated)"],["revenue_annualized_usd","Annualized $"],["revenue_per_employee","Rev / employee"],["funding_raised","Funding"],["bootstrapped_or_vc","Raised?"],["category","Category"],["as_of_date","As of"],["confidence","Confidence"],["source_url","Source"]];
const NUM=new Set(["team_size","revenue_annualized_usd","revenue_per_employee"]);
const TALLY_URL="TALLY_URL"; // TODO: replace with the Tally form URL, e.g. https://tally.so/r/xxxxxx
let rows=[],sk="revenue_per_employee",dir=-1;
function parse(t){const out=[];let r=[],f="",q=false;for(let i=0;i<t.length;i++){const c=t[i];if(q){if(c=='"'&&t[i+1]=='"'){f+='"';i++}else if(c=='"')q=false;else f+=c}else if(c=='"')q=true;else if(c==','){r.push(f);f=""}else if(c=='\n'){r.push(f);out.push(r);r=[];f=""}else if(c!='\r')f+=c}if(f||r.length){r.push(f);out.push(r)}const h=out.shift();return out.filter(x=>x.length>1).map(x=>Object.fromEntries(h.map((k,i)=>[k,x[i]||""])))}
const money=v=>v?"$"+(+v>=1e6?(+v/1e6).toFixed(1)+"M":Math.round(+v/1e3)+"K"):"";
function render(){const q=document.getElementById("q").value.toLowerCase(),fu=fund.value,cf=conf.value,tm=team.value;
let v=rows.filter(r=>(grad.checked||r.status!="graduated")&&(!q||(r.name+r.category).toLowerCase().includes(q))&&(!fu||(fu=="unknown"?!r.bootstrapped_or_vc:r.bootstrapped_or_vc==fu))&&(!cf||r.confidence==cf)&&(tm=="any"||(r.team_size&&+r.team_size<=+tm)));
v.sort((a,b)=>{let x=a[sk],y=b[sk];if(NUM.has(sk)){x=x===""?null:+x;y=y===""?null:+y;if(x==null)return 1;if(y==null)return -1;return (x-y)*dir}return x.localeCompare(y)*dir});
document.getElementById("count").textContent=v.length+" companies";
hd.innerHTML=COLS.map(([k,l])=>`<th data-k="${k}" class="${NUM.has(k)?'num':''}">${l}${k==sk?(dir>0?" ▲":" ▼"):""}</th>`).join("");
tb.innerHTML=v.map(r=>`<tr>${COLS.map(([k])=>{let x=r[k];if(k=="name"){x=r.url?`<a href="${r.url}" target="_blank" rel="noopener">${x}</a>`:x;if(r.status=="graduated")x+=` <span class="tag grad" title="Now over 20 people or part of a larger company; historical snapshot, excluded from rankings">graduated</span>`}if(k=="revenue_annualized_usd"||k=="revenue_per_employee")x=money(x);if(k=="confidence")x=`<span class="tag ${x}">${x}</span>`;if(k=="source_url")x=`<a href="${x}" target="_blank" rel="noopener" title="${r.notes}">link</a>`;if(k=="bootstrapped_or_vc")x=x=="vc"?"Raised":x=="bootstrapped"?"Bootstrapped":"";return `<td class="${NUM.has(k)?'num':''}">${x}</td>`}).join("")}</tr>`).join("");
hd.querySelectorAll("th").forEach(th=>th.onclick=()=>{const k=th.dataset.k;dir=k==sk?-dir:(NUM.has(k)?-1:1);sk=k;render()});}
fetch("data/companies.csv").then(r=>r.text()).then(t=>{rows=parse(t);
document.getElementById("rank").innerHTML=rows.filter(r=>r.status!="graduated"&&r.revenue_per_employee&&r.team_size&&+r.team_size<=20).sort((a,b)=>b.revenue_per_employee-a.revenue_per_employee).slice(0,10).map(r=>`<li>${r.name} (${money(r.revenue_per_employee)}/person, team ${r.team_size}, <span class="tag ${r.confidence}">${r.confidence}</span>)</li>`).join("");
const sl=document.getElementById("submit");if(TALLY_URL.startsWith("http"))sl.href=TALLY_URL;else sl.onclick=()=>{alert("Submission form coming soon.");return false};
["q","fund","conf","team","grad"].forEach(i=>document.getElementById(i).oninput=render);render()});
