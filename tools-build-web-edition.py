#!/usr/bin/env python3
"""Build a single-page browsable web edition of the growth-fundamentals pack."""
import html
import os
import re

import markdown

ROOT = os.path.expanduser("~/Desktop/Projects/growth-fundamentals")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "growth-fundamentals.html")

GROUPS = [
    ("Start", "Orientation and the handoff", [
        ("README.md", "00", "What this pack is"),
        ("00-START-HERE.md", "01", "Start here \u2014 the operating manual"),
        ("HANDOFF.md", "02", "Handoff \u2014 brief a new machine"),
    ]),
    ("Brand", "What you stand for, before any pixel", [
        ("brand/01-positioning-and-category.md", "03"),
        ("brand/02-identity-archetype-and-naming.md", "04"),
        ("brand/03-voice-messaging-and-copywriting.md", "05"),
    ]),
    ("Psychology", "Why people choose, and the ethics line", [
        ("psychology/04-persuasion-core.md", "06"),
        ("psychology/05-visual-attention-and-layout.md", "07"),
        ("psychology/06-color-and-typography.md", "08"),
        ("psychology/07-pricing-psychology.md", "09"),
    ]),
    ("Build", "Turning the decisions into a site", [
        ("build/08-page-architecture-and-section-recipes.md", "10"),
        ("build/09-design-system-and-tokens.md", "11"),
        ("build/10-conversion-audit-checklist.md", "12"),
    ]),
    ("Search", "Being found, and being cited", [
        ("search/11-seo-fundamentals.md", "13"),
        ("search/12-geo-ai-search.md", "14"),
        ("search/13-schema-and-technical-wiring.md", "15"),
    ]),
    ("Ops", "Measuring, launching, and driving an agent", [
        ("ops/14-measurement-and-experimentation.md", "16"),
        ("ops/15-launch-checklist-and-build-order.md", "17"),
        ("ops/16-prompt-pack.md", "18"),
    ]),
    ("Templates", "Fill these in; they become the source of truth", [
        ("templates/brand-brief.md", "19", "Brand brief"),
        ("templates/page-brief.md", "20", "Page brief"),
        ("templates/llms.txt.example", "21"),
        ("templates/robots.txt.example", "22"),
        ("templates/wordpress/README.md", "23", "WordPress: the mechanics"),
        ("templates/wordpress/llms.txt.example", "24", "WordPress: llms.txt"),
        ("templates/wordpress/sitemap.xml.example", "25", "WordPress: sitemap.xml"),
    ]),
    ("Agent skills", "Drop-in procedures for a coding agent", [
        ("skills/README.md", "26", "Installing the skills"),
        ("skills/brand-web-design.skill.md", "27", "Skill: brand web design"),
        ("skills/growth-search.skill.md", "28", "Skill: growth search"),
    ]),
    ("Reference", "What this draws on, and what it does not bundle", [
        ("reference/README.md", "29", "Sources and honesty note"),
    ]),
]


def slug(path):
    return "doc-" + re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")


ANCHORS = {}
for _g, _d, items in GROUPS:
    for item in items:
        ANCHORS[os.path.basename(item[0])] = slug(item[0])


def strip_front_matter(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            fm = text[4:end]
            body = text[end + 5:]
            desc = ""
            m = re.search(r'^description:\s*"?(.*?)"?\s*$', fm, re.M)
            if m:
                desc = m.group(1)
            return body, desc
    return text, ""


def rewrite_links(md_text):
    def repl(m):
        label, target = m.group(1), m.group(2)
        base = os.path.basename(target.split("#")[0])
        if base in ANCHORS:
            return "[%s](#%s)" % (label, ANCHORS[base])
        return m.group(0)
    return re.sub(r"\[([^\]]+)\]\(((?:\.\./|\./)?[^)\s]+\.(?:md|example))\)", repl, md_text)


def convert(md_text):
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    out = md.convert(md_text)
    out = re.sub(r"<li>\s*\[ \]\s*", '<li class="task"><span class="box" aria-hidden="true"></span>', out)
    out = re.sub(r"<li>\s*\[x\]\s*", '<li class="task done"><span class="box" aria-hidden="true"></span>', out, flags=re.I)
    out = re.sub(r"<table>", '<div class="tw"><table>', out)
    out = re.sub(r"</table>", "</table></div>", out)
    return out


sections = []
nav = []
total_words = 0

for group, gdesc, items in GROUPS:
    nav.append('<div class="navgroup"><div class="navhead">%s</div><div class="navdesc">%s</div><ul>'
               % (html.escape(group), html.escape(gdesc)))
    for item in items:
        path, num = item[0], item[1]
        override = item[2] if len(item) > 2 else None
        full = os.path.join(ROOT, path)
        raw = open(full, encoding="utf-8").read()
        total_words += len(raw.split())
        sid = slug(path)

        if path.endswith(".example"):
            title = os.path.basename(path)
            sub = "Starter file — copy it, fill the placeholders."
            body = '<pre><code>%s</code></pre>' % html.escape(raw)
        else:
            body_md, _desc = strip_front_matter(raw)
            m = re.search(r"^#\s+(.+)$", body_md, re.M)
            title = m.group(1).strip() if m else os.path.basename(path)
            body_md = re.sub(r"^#\s+.+$", "", body_md, count=1, flags=re.M)
            lead = re.match(r"\s*((?:[^\n]+\n)+)", body_md)
            sub = ""
            if lead:
                cand = lead.group(1).strip()
                if not cand.startswith(("#", "-", "|", ">", "```")):
                    sub = re.sub(r"\s+", " ", cand)
                    body_md = body_md[lead.end():]
            body = convert(rewrite_links(body_md))
            if sub:
                sub = convert(sub).replace("<p>", "").replace("</p>", "")

        lines = len(raw.splitlines())
        navtitle = override or title
        nav.append('<li><a href="#%s" data-doc="%s"><span class="n">%s</span><span class="t">%s</span></a></li>'
                   % (sid, sid, num, html.escape(navtitle)))
        sections.append(
            '<section class="doc" id="%s" data-title="%s" data-group="%s">'
            '<div class="dochead"><div class="eyebrow"><span class="num">%s</span>'
            '<span class="grp">%s</span><span class="src">%s</span><span class="len">%d lines</span></div>'
            '<h1>%s</h1><div class="lead">%s</div></div>'
            '<div class="docbody">%s</div></section>'
            % (sid, html.escape(title.lower()), html.escape(group.lower()), num,
               html.escape(group), html.escape(path), lines,
               html.escape(title), sub, body)
        )
    nav.append("</ul></div>")

NAV = "\n".join(nav)
BODY = "\n".join(sections)
WORDS = "{:,}".format(total_words)
DOCS = sum(len(i) for _g, _d, i in GROUPS)

CSS = """
:root{
  --field:#D5D9D2; --paper:#F3F5F0; --sunk:#E4E8E1;
  --ink:#171A16; --ink-2:#3C4139; --muted:#6B6F68; --faint:#9AA096;
  --rule:rgba(23,26,22,.14); --rule-2:rgba(23,26,22,.07);
  --accent:#2B4C8C; --accent-soft:rgba(43,76,140,.10);
  --hot:#B8431C; --hot-soft:rgba(184,67,28,.10);
  --shadow:0 1px 2px rgba(23,26,22,.05),0 12px 32px -18px rgba(23,26,22,.25);
}
@media (prefers-color-scheme:dark){
  :root{
    --field:#0D0F0D; --paper:#171A17; --sunk:#121512;
    --ink:#E8E9E3; --ink-2:#C3C7BE; --muted:#8E948B; --faint:#6C726A;
    --rule:rgba(232,233,227,.16); --rule-2:rgba(232,233,227,.08);
    --accent:#8FACE4; --accent-soft:rgba(143,172,228,.13);
    --hot:#E1804F; --hot-soft:rgba(225,128,79,.13);
    --shadow:0 1px 2px rgba(0,0,0,.4),0 14px 34px -20px rgba(0,0,0,.7);
  }
}
:root[data-theme="light"]{
  --field:#D5D9D2; --paper:#F3F5F0; --sunk:#E4E8E1;
  --ink:#171A16; --ink-2:#3C4139; --muted:#6B6F68; --faint:#9AA096;
  --rule:rgba(23,26,22,.14); --rule-2:rgba(23,26,22,.07);
  --accent:#2B4C8C; --accent-soft:rgba(43,76,140,.10);
  --hot:#B8431C; --hot-soft:rgba(184,67,28,.10);
  --shadow:0 1px 2px rgba(23,26,22,.05),0 12px 32px -18px rgba(23,26,22,.25);
}
:root[data-theme="dark"]{
  --field:#0D0F0D; --paper:#171A17; --sunk:#121512;
  --ink:#E8E9E3; --ink-2:#C3C7BE; --muted:#8E948B; --faint:#6C726A;
  --rule:rgba(232,233,227,.16); --rule-2:rgba(232,233,227,.08);
  --accent:#8FACE4; --accent-soft:rgba(143,172,228,.13);
  --hot:#E1804F; --hot-soft:rgba(225,128,79,.13);
  --shadow:0 1px 2px rgba(0,0,0,.4),0 14px 34px -20px rgba(0,0,0,.7);
}

*{box-sizing:border-box}
body{
  margin:0; background:var(--field); color:var(--ink);
  font-family:"Avenir Next","Avenir","Segoe UI Variable Text","Segoe UI",Roboto,system-ui,sans-serif;
  font-size:16px; line-height:1.62; -webkit-font-smoothing:antialiased;
}
.serif{font-family:Charter,"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif}
.mono,code,pre,kbd{font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:2px}

/* ---------- shell ---------- */
.shell{display:grid;grid-template-columns:300px minmax(0,1fr);gap:0;min-height:100vh}

/* ---------- rail ---------- */
.rail{
  position:sticky;top:0;height:100vh;overflow-y:auto;
  border-right:1px solid var(--rule);background:var(--sunk);
  padding:26px 20px 48px;
}
.brandmark{display:block;text-decoration:none;color:inherit;margin-bottom:22px}
.brandmark .kicker{
  font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--faint);
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;
}
.brandmark h2{
  font-family:Charter,"Iowan Old Style",Palatino,Georgia,serif;
  font-size:23px;line-height:1.15;margin:6px 0 0;font-weight:600;letter-spacing:-.01em;
}
.railstat{
  font-size:11px;color:var(--muted);margin-top:8px;
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;
}
.search{
  width:100%;margin:0 0 20px;padding:9px 11px;border:1px solid var(--rule);
  background:var(--paper);color:var(--ink);border-radius:3px;font:inherit;font-size:13px;
}
.search::placeholder{color:var(--faint)}
.navgroup{margin-bottom:20px}
.navhead{
  font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-2);font-weight:600;
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;
}
.navdesc{font-size:11.5px;color:var(--faint);line-height:1.4;margin:2px 0 7px}
.rail ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:1px}
.rail li a{
  display:flex;gap:9px;align-items:baseline;text-decoration:none;color:var(--ink-2);
  padding:5px 8px;border-radius:3px;font-size:13.5px;line-height:1.35;
}
.rail li a:hover{background:var(--accent-soft);color:var(--ink)}
.rail li a.active{background:var(--accent);color:#fff}
.rail li a.active .n{color:rgba(255,255,255,.7)}
.rail li a .t{flex:1;min-width:0;overflow-wrap:anywhere}
.rail li a .n{
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;
  font-size:10.5px;color:var(--faint);flex:none;padding-top:2px;
}
.rail li.hide,.navgroup.hide{display:none}

/* ---------- main ---------- */
.main{padding:0 0 120px;min-width:0}
.masthead{
  border-bottom:1px solid var(--rule);padding:52px 8vw 0;
  background:linear-gradient(var(--sunk),var(--field));
}
.masthead .inner{max-width:940px;margin:0 auto}
.masthead .kicker{
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;
  font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);
}
.masthead h1{
  font-family:Charter,"Iowan Old Style",Palatino,Georgia,serif;
  font-size:clamp(32px,5.2vw,50px);line-height:1.06;letter-spacing:-.022em;
  margin:14px 0 0;font-weight:600;text-wrap:balance;max-width:16ch;
}
.masthead .sub{max-width:56ch;color:var(--ink-2);margin:16px 0 0;font-size:17px}
.metrics{display:flex;flex-wrap:wrap;gap:0;margin:30px 0 0;border-top:1px solid var(--rule-2)}
.metric{padding:14px 26px 16px 0;margin-right:26px;border-right:1px solid var(--rule-2)}
.metric:last-child{border-right:0}
.metric b{
  display:block;font-family:Charter,"Iowan Old Style",Palatino,Georgia,serif;
  font-size:26px;font-weight:600;line-height:1;font-variant-numeric:tabular-nums;
}
.metric span{
  display:block;margin-top:5px;font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;
}

/* ---------- the dial ---------- */
.dial{
  max-width:940px;margin:34px auto 0;border:1px solid var(--rule);border-bottom:0;
  border-radius:4px 4px 0 0;background:var(--paper);padding:22px 24px 24px;box-shadow:var(--shadow);
}
.dial .lbl{
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;
  font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);
}
.dial h3{font-family:Charter,"Iowan Old Style",Palatino,Georgia,serif;font-size:19px;margin:7px 0 3px;font-weight:600}
.dial p.why{color:var(--muted);font-size:13.5px;margin:0 0 16px;max-width:62ch}
.switch{display:inline-flex;border:1px solid var(--rule);border-radius:3px;overflow:hidden;margin-bottom:18px}
.switch button{
  font:inherit;font-size:12.5px;padding:7px 15px;border:0;cursor:pointer;
  background:transparent;color:var(--muted);
}
.switch button[aria-pressed="true"]{background:var(--pole);color:#fff}
.dialgrid{display:grid;grid-template-columns:150px minmax(0,1fr);gap:16px 22px;align-items:start}
.swatchwrap{display:flex;flex-direction:column;gap:8px}
.swatch{height:56px;border-radius:3px;background:var(--pole);transition:background .45s ease}
.swatchcode{
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:11px;color:var(--muted);
}
.demo{border-left:2px solid var(--pole);padding-left:16px;transition:border-color .45s ease}
.demo .h{
  font-family:Charter,"Iowan Old Style",Palatino,Georgia,serif;font-size:21px;line-height:1.2;
  margin:0 0 6px;font-weight:600;text-wrap:balance;
}
.demo .b{color:var(--ink-2);font-size:14px;margin:0 0 13px;max-width:46ch}
.demo .cta{
  display:inline-block;background:var(--pole);color:#fff;border-radius:3px;
  padding:9px 17px;font-size:13.5px;font-weight:600;transition:background .45s ease;
}
.demo .micro{font-size:11.5px;color:var(--muted);margin:8px 0 0}
.rules{list-style:none;margin:16px 0 0;padding:16px 0 0;border-top:1px solid var(--rule-2);
  display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:8px 22px}
.rules li{font-size:12.5px;color:var(--ink-2);display:flex;gap:8px;align-items:baseline}
.rules li::before{content:"";flex:none;width:5px;height:5px;border-radius:50%;background:var(--pole);transform:translateY(-2px)}

/* ---------- document ---------- */
.paper{
  max-width:940px;margin:0 auto;background:var(--paper);border:1px solid var(--rule);
  border-radius:0 0 4px 4px;box-shadow:var(--shadow);padding:44px 6vw 64px;
}
.doc{display:none}
.doc.on{display:block}
.dochead{border-bottom:1px solid var(--rule);padding-bottom:22px;margin-bottom:30px}
.eyebrow{
  display:flex;flex-wrap:wrap;gap:12px;align-items:center;
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;
  font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);
}
.eyebrow .num{background:var(--accent);color:#fff;padding:2px 7px;border-radius:2px;letter-spacing:.08em}
.eyebrow .grp{color:var(--accent);font-weight:600}
.dochead h1{
  font-family:Charter,"Iowan Old Style",Palatino,Georgia,serif;
  font-size:clamp(27px,3.6vw,38px);line-height:1.12;letter-spacing:-.018em;
  margin:14px 0 0;font-weight:600;text-wrap:balance;
}
.lead{color:var(--ink-2);font-size:17px;margin-top:12px;max-width:62ch}

.docbody{max-width:70ch}
.docbody h2{
  font-family:Charter,"Iowan Old Style",Palatino,Georgia,serif;
  font-size:25px;line-height:1.2;margin:48px 0 12px;font-weight:600;letter-spacing:-.012em;
  padding-top:16px;border-top:1px solid var(--rule-2);text-wrap:balance;
}
.docbody>hr:first-child{display:none}
.docbody h2:first-child{margin-top:0;border-top:0;padding-top:0}
.docbody hr+h2{border-top:0;padding-top:0;margin-top:26px}
.docbody hr+h3{margin-top:24px}
.docbody h3{font-size:16.5px;margin:30px 0 8px;font-weight:700;letter-spacing:-.005em}
.docbody h4{
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;
  font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin:24px 0 6px;
}
.docbody p{margin:0 0 15px}
.docbody ul,.docbody ol{margin:0 0 16px;padding-left:20px}
.docbody li{margin-bottom:6px}
.docbody li>ul,.docbody li>ol{margin-top:6px}
.docbody li.task{list-style:none;margin-left:-20px;padding-left:0;display:flex;gap:9px;align-items:flex-start}
.docbody li.task .box{
  flex:none;width:13px;height:13px;border:1.5px solid var(--faint);border-radius:2px;margin-top:5px;
}
.docbody li.task.done .box{background:var(--accent);border-color:var(--accent)}
.docbody blockquote{
  margin:18px 0;padding:2px 0 2px 18px;border-left:2px solid var(--accent);
  color:var(--ink-2);
}
.docbody blockquote p:last-child{margin-bottom:0}
.docbody hr{border:0;border-top:1px solid var(--rule);margin:34px 0}
.docbody strong{font-weight:700;color:var(--ink)}
.docbody code{
  overflow-wrap:anywhere;
  background:var(--sunk);border:1px solid var(--rule-2);padding:1px 5px;border-radius:3px;
  font-size:.86em;color:var(--ink);
}
.docbody pre{
  background:var(--sunk);border:1px solid var(--rule);border-radius:3px;
  padding:14px 16px;overflow-x:auto;margin:0 0 18px;font-size:12.5px;line-height:1.55;
}
.docbody pre code{background:none;border:0;padding:0;font-size:inherit}
.tw{overflow-x:auto;margin:0 0 20px;border:1px solid var(--rule);border-radius:3px}
.docbody table{border-collapse:collapse;width:100%;font-size:13.5px}
.docbody th{
  text-align:left;background:var(--sunk);padding:9px 12px;border-bottom:1px solid var(--rule);
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;
  font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);white-space:nowrap;
}
.docbody td{padding:9px 12px;border-bottom:1px solid var(--rule-2);vertical-align:top;
  font-variant-numeric:tabular-nums}
.docbody tr:last-child td{border-bottom:0}

.footnav{
  max-width:940px;margin:26px auto 0;display:flex;justify-content:space-between;gap:16px;
  font-size:13px;color:var(--muted);flex-wrap:wrap;
}
.footnav a{text-decoration:none}
.footnav .repo{
  font-family:"SF Mono","IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:11.5px;
}

.railtoggle{display:none}
@media (max-width:900px){
  .shell{grid-template-columns:1fr}
  .rail{position:sticky;top:0;z-index:20;height:auto;overflow:visible;
    border-right:0;border-bottom:1px solid var(--rule);padding:12px 5vw}
  .brandmark{margin-bottom:12px}
  .brandmark h2{font-size:19px}
  .brandmark h2 br{display:none}
  .railtoggle{
    display:flex;width:100%;justify-content:space-between;align-items:center;
    font:inherit;font-size:13px;padding:9px 12px;cursor:pointer;color:var(--ink-2);
    background:var(--paper);border:1px solid var(--rule);border-radius:3px;
  }
  .railtoggle .chev{transition:transform .2s ease;color:var(--faint)}
  .railtoggle[aria-expanded="true"] .chev{transform:rotate(180deg)}
  .navwrap{display:none;max-height:65vh;overflow-y:auto;padding-top:14px}
  .navwrap.open{display:block}
  .masthead{padding:36px 5vw 0}
  .paper{padding:32px 5vw 48px;border-left:0;border-right:0;border-radius:0}
  .dial{margin-left:0;margin-right:0;border-radius:0}
  .dialgrid{grid-template-columns:1fr}
  .docbody{max-width:none}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""

JS = """
(function(){
  var links=[].slice.call(document.querySelectorAll('.rail a[data-doc]'));
  var docs=[].slice.call(document.querySelectorAll('.doc'));
  function show(id,push){
    var found=false;
    docs.forEach(function(d){var on=d.id===id;d.classList.toggle('on',on);if(on)found=true;});
    if(!found){docs[0].classList.add('on');id=docs[0].id;}
    links.forEach(function(a){a.classList.toggle('active',a.getAttribute('data-doc')===id);});
    if(push&&location.hash!=='#'+id){history.replaceState(null,'','#'+id);}
    window.scrollTo({top:0,behavior:'instant'});
  }
  var wrap=document.getElementById('navwrap'),tog=document.getElementById('railtoggle');
  function closeRail(){wrap.classList.remove('open');tog.setAttribute('aria-expanded','false');}
  tog.addEventListener('click',function(){
    var open=wrap.classList.toggle('open');tog.setAttribute('aria-expanded',String(open));
  });
  links.forEach(function(a){
    a.addEventListener('click',function(e){
      e.preventDefault();show(a.getAttribute('data-doc'),true);
      if(window.matchMedia('(max-width:900px)').matches)closeRail();
    });
  });
  document.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="#doc-"]');
    if(a&&!a.hasAttribute('data-doc')){e.preventDefault();show(a.getAttribute('href').slice(1),true);}
  });
  window.addEventListener('hashchange',function(){show(location.hash.slice(1),false);});
  show(location.hash?location.hash.slice(1):docs[0].id,false);

  var q=document.getElementById('q');
  q.addEventListener('input',function(){
    var v=q.value.trim().toLowerCase();
    document.querySelectorAll('.navgroup').forEach(function(g){
      var any=false;
      g.querySelectorAll('li').forEach(function(li){
        var t=li.textContent.toLowerCase()+' '+g.querySelector('.navhead').textContent.toLowerCase();
        var hit=!v||t.indexOf(v)>-1;
        li.classList.toggle('hide',!hit); if(hit)any=true;
      });
      g.classList.toggle('hide',!any);
    });
  });

  var POLES={
    calm:{c:'#2B4C8C',cd:'#8FACE4',code:'Cool · low saturation · slow · spacious',
      h:'A quieter way to run your billing.',
      b:'Invoices go out on the day you agreed, chased automatically, in your words. You approve; it sends.',
      cta:'See how it works',micro:'No card. Cancel in one click.',
      r:['Hoard saturation for one element','Generous whitespace reads premium','Slow eased motion, 400\\u2013600ms','Round prices, value before price','Name one honest drawback','No countdowns, ever']},
    hot:{c:'#B8431C',cd:'#E1804F',code:'Warm · high saturation · fast · tight',
      h:'Get paid today. Not in thirty days.',
      b:'Send it, chase it, bank it. Set up in four minutes and watch the first invoice clear before lunch.',
      cta:'Start now',micro:'Free while we are in early access.',
      r:['Saturate the field, not just the CTA','Tight grids raise perceived energy','Fast onsets, looming reveals','Precise prices read as calculated','Lead with the sharpest benefit','Honest scarcity only \\u2014 real cohorts']}
  };
  var dial=document.getElementById('dial');
  function isDark(){
    var t=document.documentElement.getAttribute('data-theme');
    if(t)return t==='dark';
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function setPole(k){
    var p=POLES[k];
    dial.style.setProperty('--pole',isDark()?p.cd:p.c);
    dial.querySelector('.swatchcode').textContent=p.code;
    dial.querySelector('.demo .h').textContent=p.h;
    dial.querySelector('.demo .b').textContent=p.b;
    dial.querySelector('.demo .cta').textContent=p.cta;
    dial.querySelector('.demo .micro').textContent=p.micro;
    dial.querySelector('.rules').innerHTML=p.r.map(function(x){return '<li>'+x+'</li>';}).join('');
    dial.querySelectorAll('.switch button').forEach(function(b){
      b.setAttribute('aria-pressed',String(b.getAttribute('data-pole')===k));
    });
    dial.setAttribute('data-current',k);
  }
  dial.querySelectorAll('.switch button').forEach(function(b){
    b.addEventListener('click',function(){setPole(b.getAttribute('data-pole'));});
  });
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change',function(){
    setPole(dial.getAttribute('data-current')||'calm');
  });
  new MutationObserver(function(){setPole(dial.getAttribute('data-current')||'calm');})
    .observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
  setPole('calm');
})();
"""

PAGE = """<title>Growth &amp; Brand Fundamentals</title>
<style>%(css)s</style>
<div class="shell">
  <nav class="rail" aria-label="Contents">
    <a class="brandmark" href="#doc-readme-md">
      <div class="kicker">Field manual</div>
      <h2>Growth &amp; Brand <br>Fundamentals</h2>
      <div class="railstat">%(docs)d documents · %(words)s words</div>
    </a>
    <button class="railtoggle" id="railtoggle" type="button" aria-expanded="false" aria-controls="navwrap">
      <span>Contents</span><span class="chev" aria-hidden="true">&darr;</span>
    </button>
    <div class="navwrap" id="navwrap">
      <input id="q" class="search" type="search" placeholder="Filter contents…" aria-label="Filter contents">
      %(nav)s
    </div>
  </nav>

  <main class="main">
    <header class="masthead">
      <div class="inner">
        <div class="kicker">Build a brand from zero</div>
        <h1>The fundamentals, not somebody else&rsquo;s answers.</h1>
        <p class="sub">Positioning, behavioural design, pricing, page architecture, search and AI
        visibility &mdash; written as rules you can act on, for a brand that does not exist yet.</p>
        <div class="metrics">
          <div class="metric"><b>%(docs)d</b><span>Documents</span></div>
          <div class="metric"><b>%(words)s</b><span>Words</span></div>
          <div class="metric"><b>5</b><span>Decisions before any pixel</span></div>
          <div class="metric"><b>2</b><span>Drop-in agent skills</span></div>
        </div>
      </div>
    </header>

    <section class="dial" id="dial" data-current="calm">
      <div class="lbl">The master dial</div>
      <h3>One decision inverts half of this pack.</h3>
      <p class="why">Most persuasion tactics push arousal. Arousal is a dial, not a virtue. Set it before
      you choose a colour, a word, or a price &mdash; then read every rule through it.</p>
      <div class="switch" role="group" aria-label="Arousal target">
        <button type="button" data-pole="calm" aria-pressed="true">Calm &middot; premium &middot; trusted</button>
        <button type="button" data-pole="hot" aria-pressed="false">Energetic &middot; urgent &middot; playful</button>
      </div>
      <div class="dialgrid">
        <div class="swatchwrap">
          <div class="swatch"></div>
          <div class="swatchcode"></div>
        </div>
        <div class="demo">
          <p class="h"></p>
          <p class="b"></p>
          <span class="cta"></span>
          <p class="micro"></p>
        </div>
      </div>
      <ul class="rules"></ul>
    </section>

    <div class="paper">%(body)s</div>

    <div class="footnav">
      <span>An original synthesis. No third-party paid material is reproduced here.</span>
      <span class="repo">github.com/TheCryptoSimon/growth-fundamentals</span>
    </div>
  </main>
</div>
<script>%(js)s</script>
""" % {"css": CSS, "js": JS, "nav": NAV, "body": BODY, "words": WORDS, "docs": DOCS}

open(OUT, "w", encoding="utf-8").write(PAGE)
print("wrote", OUT, os.path.getsize(OUT), "bytes;", DOCS, "docs;", WORDS, "words")
