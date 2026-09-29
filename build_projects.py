# Generates the four project detail pages from one template so they stay consistent.
import os, io
HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(HERE, "projects")
os.makedirs(OUT, exist_ok=True)

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Frank Wang</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="../assets/site.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' fill='%231E4D5C'/><text x='16' y='23' font-family='monospace' font-size='19' font-weight='700' fill='%23EFEFEC' text-anchor='middle'>F</text></svg>">
</head>
<body>

<nav><div class="in">
  <a class="me" href="../index.html">FRANK WANG</a>
  <span class="lk">
    <a href="../index.html#work">Work</a>
    <a href="../index.html#background" class="opt">Background</a>
    <a href="mailto:frankwhn0227@outlook.com">Contact</a>
  </span>
</div></nav>

<div class="phead"><div class="col">
  <a class="back" href="../index.html#work"><span>&larr;</span> All work</a>
  <div class="tag">{tag}</div>
  <h1>{h1}</h1>
  <p class="lede">{lede}</p>
</div></div>
"""

FOOT = """
<section><div class="col">
  <div class="sk">Next</div>
  <div class="nextprev">
    {nav}
  </div>
</div></section>

<footer><div class="col">
  <div class="row">
    <a href="mailto:frankwhn0227@outlook.com">frankwhn0227@outlook.com</a>
    <a href="https://www.linkedin.com/in/frank-haonian-wang-465636354" target="_blank" rel="noopener">LinkedIn</a>
    <a href="https://github.com/Frankkk-Wang" target="_blank" rel="noopener">GitHub</a>
  </div>
  <div>Static page on GitHub Pages. No trackers, no cookies.</div>
</div></footer>

</body>
</html>
"""

PIPELINE_SVG = """
<div class="wide"><figure class="figure">
<svg viewBox="0 0 960 330" role="img" aria-label="One conversation turn: redaction and routing are deterministic, intent classification and reply composition are model calls, and a deterministic line check gates the reply before it is sent.">
  <defs>
    <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker>
    <marker id="arp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--pro)"/></marker>
  </defs>
  <style>
    .bx{fill:var(--surface);stroke:var(--det);stroke-width:1.5}
    .bxp{fill:var(--pro-w);stroke:var(--pro);stroke-width:1.5}
    .lbl{font-family:var(--mono);font-size:12.5px;fill:var(--ink);font-weight:500}
    .sub{font-family:var(--mono);font-size:10.5px;fill:var(--ink-3)}
    .ln{stroke:var(--det);stroke-width:1.4;fill:none;color:var(--det)}
    .lnp{stroke:var(--pro);stroke-width:1.4;fill:none;stroke-dasharray:4 3;color:var(--pro)}
    .step{font-family:var(--mono);font-size:10px;fill:var(--ink-3)}
  </style>
  <text class="step" x="12" y="26">01</text>
  <rect class="bx" x="12" y="36" width="140" height="52" rx="3"/>
  <text class="lbl" x="26" y="60">redact</text><text class="sub" x="26" y="76">before anything leaves</text>
  <line class="ln" x1="152" y1="62" x2="196" y2="62" marker-end="url(#ar)"/>
  <text class="step" x="204" y="26">02</text>
  <rect class="bxp" x="204" y="36" width="160" height="52" rx="3"/>
  <text class="lbl" x="218" y="60">classify + extract</text><text class="sub" x="218" y="76">two concurrent calls</text>
  <line class="ln" x1="364" y1="62" x2="408" y2="62" marker-end="url(#ar)"/>
  <text class="step" x="416" y="26">03</text>
  <rect class="bx" x="416" y="36" width="150" height="52" rx="3"/>
  <text class="lbl" x="430" y="60">floors</text><text class="sub" x="430" y="76">drop bad model output</text>
  <line class="ln" x1="566" y1="62" x2="610" y2="62" marker-end="url(#ar)"/>
  <text class="step" x="618" y="26">04</text>
  <rect class="bx" x="618" y="36" width="170" height="52" rx="3"/>
  <text class="lbl" x="632" y="60">routing ladder</text><text class="sub" x="632" y="76">15 guards, first hit wins</text>
  <path class="ln" d="M788 62 H 840 a10 10 0 0 1 10 10 V 128 a10 10 0 0 1 -10 10 H 120" marker-end="url(#ar)"/>
  <text class="step" x="12" y="128">05</text>
  <rect class="bx" x="12" y="138" width="190" height="52" rx="3"/>
  <text class="lbl" x="26" y="162">decision engine</text><text class="sub" x="26" y="178">score &middot; tier &middot; match &middot; checklist</text>
  <line class="ln" x1="202" y1="164" x2="246" y2="164" marker-end="url(#ar)"/>
  <text class="step" x="254" y="128">06</text>
  <rect class="bxp" x="254" y="138" width="170" height="52" rx="3"/>
  <text class="lbl" x="268" y="162">compose reply</text><text class="sub" x="268" y="178">from those facts only</text>
  <line class="ln" x1="424" y1="164" x2="468" y2="164" marker-end="url(#ar)"/>
  <text class="step" x="476" y="128">07</text>
  <rect class="bx" x="476" y="138" width="180" height="52" rx="3"/>
  <text class="lbl" x="490" y="162">line check</text><text class="sub" x="490" y="178">must / must-not contain</text>
  <path class="lnp" d="M566 190 V 224 H 340 V 194" marker-end="url(#arp)"/>
  <text class="sub" x="352" y="242" style="fill:var(--pro)">breach &rarr; regenerate once, then fall back to a template</text>
  <line class="ln" x1="656" y1="164" x2="700" y2="164" marker-end="url(#ar)"/>
  <rect class="bx" x="700" y="138" width="130" height="52" rx="3" style="fill:var(--det);stroke:var(--det)"/>
  <text class="lbl" x="714" y="168" style="fill:var(--surface)">send</text>
  <line x1="12" y1="286" x2="948" y2="286" stroke="var(--rule)" stroke-width="1"/>
  <text class="sub" x="12" y="308">Guardrails never depend on a retrieval hit. The knowledge base sits in context and is read by lookup, not search.</text>
</svg>
<figcaption>One turn, end to end. Two of the seven steps are model calls. Everything that produces a number is code.</figcaption>
</figure></div>
"""

PAGES = {
"hef": dict(
  title="HEF Funding Navigator",
  desc="A loan-navigation assistant for a Treasury-certified CDFI, live in production. Shipped in seven days.",
  tag="Naturalness.ai &middot; AI Solutions Engineer &middot; 2026",
  h1="HEF Funding Navigator",
  lede='An assistant for the <a href="https://www.hefnyc.org/" target="_blank" rel="noopener"><b>Harlem Entrepreneurial Fund</b></a>, a Treasury-certified CDFI that lends $2,500 to $350,000 to small businesses banks turn down. It matches people to a loan, tells them how loan-ready they are, and works out which licenses and permits their business needs.',
  body="""
<section><div class="col">
  <p>It is live on hefnyc.org. We shipped the first version in seven days, then rebuilt it once the evaluation results came back.</p>
  <div class="stats">
    <div><b>7 days</b><span>to first launch</span></div>
    <div><b>437</b><span>unit tests</span></div>
    <div><b>132</b><span>persona scenarios</span></div>
    <div><b>98%</b><span>scenario pass rate</span></div>
  </div>

  <h2>The decision the whole thing rests on</h2>
  <p>A language model asked to total five weighted factors and compare them against two thresholds gets it right most of the time, and <b>wrong quietly</b> the rest. Someone is told they are in the wrong tier, nobody notices, and the only trace is one bad conversation.</p>
  <p>So the model classifies intent, pulls entities out of free text, and writes the prose. <b>Every number is computed in code.</b> Scoring, tier selection, product matching, permit-checklist assembly, PII redaction &mdash; none of it goes near the model.</p>
  <div class="legend">
    <i class="d">deterministic &mdash; code decides</i>
    <i class="p">probabilistic &mdash; the model decides</i>
  </div>
</div>
""" + PIPELINE_SVG + """
<div class="col">
  <h2>What that bought, and what it cost</h2>
  <p>An earlier version put the compliance check in a second model call. It caught real problems, but at a round trip every turn for a <b>ten percent</b> hit rate, with false positives of its own: it rejected the free-advice referral the client requires, and read the lender's own $350,000 ceiling as an invented statistic. Its rules had grown to sixteen, which is the same accumulation it was brought in to stop, moved somewhere less visible.</p>
  <p>What replaced it is a deterministic must-contain and must-not-contain check over what the knowledge base can enumerate. Free, exact, and incapable of having an off day.</p>

  <div class="aside">
    <b>The failure that changed how I build.</b> Early on the whole flow ran on unredacted text. Someone typed an EIN partway through a conversation. The parser saw nine digits, read it as a dollar amount, and overwrote the funding number they had given two turns earlier. Nothing threw an error. The conversation just kept going, quietly wrong. Redaction moved to the first step of the turn and split into two passes: one scrubs everything and that is what gets stored, one keeps the credit score so the engine can still band it. The figure lives one step and is thrown away.
  </div>

  <h2>My part in it</h2>
  <p>The client supplied the specification, a reference engine and the knowledge base. I implemented the system against it and hardened it where production found the gaps: the fifteen-rung routing ladder, a second concurrent reader for user distress, a provider abstraction with an offline fallback, three salvage attempts before a question gives up and hands off, the two-pass redaction, and the deterministic line check. I owned the testing end to end, and the results are what drove the rebuild.</p>
  <ul class="clean">
    <li>Guardrails: no rates, no fees, no approvals, internal scores never shown to the user</li>
    <li>PII redacted in both directions before storage, with tiered retention on what remains</li>
    <li>A second client assistant for a student-housing operator, built and delivered on the same stack</li>
  </ul>
  <div class="stack"><b>Stack</b> &mdash; Python &middot; DeepSeek behind a swappable provider layer &middot; no vector store &middot; pytest</div>
</div></section>
"""),

"esg": dict(
  title="ESG signals from news and filings",
  desc="Classifying ESG events out of multilingual text and turning them into company-level signals validated against market outcomes.",
  tag="Global AI &middot; Data Scientist &middot; 2025&ndash;2026",
  h1="Turning news into signals that survive a check",
  lede="Five months at an alternative-data firm whose NLP pipeline reads news, filings and NGO reports across dozens of languages and turns them into <b>company-level signals</b> for quant researchers.",
  body="""
<section><div class="col">
  <div class="stats">
    <div><b>+15%</b><span>Macro F1 over baseline</span></div>
    <div><b>+20%</b><span>pipeline throughput</span></div>
    <div><b>50+</b><span>source languages</span></div>
  </div>

  <h2>Classifying the events</h2>
  <p>I benchmarked gradient boosting, embedding-based neural models and ensembles against a TF-IDF baseline, adding source type, industry and event-history features on top of the text.</p>
  <p>The metric choice mattered more than the model choice. The label set is badly imbalanced &mdash; a handful of ESG event types dominate &mdash; and accuracy would have let the frequent categories hide everything else. I used <b>Macro F1</b>, which averages per class before averaging across them. It went up roughly <b>15%</b> over the production baseline, and the gains sat in the low-frequency categories, which is where they were worth having.</p>
  <p>Error analysis is what drove the next round: articles naming several companies, events at a subsidiary that belong to the parent, articles that mention an ESG topic without an event having happened, and categories that genuinely overlap. Those findings went back into the preprocessing rules rather than into a bigger model.</p>

  <h2>Making the signals mean something</h2>
  <p>A classified article is not yet a signal. One event reported by ten outlets is still one event, so near-duplicate coverage gets clustered before anything is counted &mdash; otherwise a syndicated story inflates a company tenfold.</p>
  <p>Then exposure has to be normalised away. A company with hundreds of articles a day and one with almost none cannot be compared raw: five negative stories is noise for the first and a strong signal for the second. Each signal is normalised against the company's own media history and against its industry.</p>

  <div class="aside">
    The question was never whether ESG events move prices. It was whether the signal carried <b>information that was not already there</b>. That is why validation used cross-sectional information coefficient against forward returns and realized volatility, controlling for industry and market cap &mdash; and why the results were reported as evidence rather than as a causal claim.
  </div>

  <h2>Cost, not just accuracy</h2>
  <p>Embedding generation and duplicate detection were the expensive steps. Batching embedding generation, caching document embeddings, skipping documents that had not changed and vectorizing preprocessing raised throughput about <b>20%</b> on a fixed benchmark.</p>
  <p>I also compared machine translation into English against multilingual sentence embeddings on the original text. For the high-volume languages the embeddings held enough meaning to classify directly, which let translation be dropped for everything except low-confidence cases that a human would review anyway.</p>
  <div class="stack"><b>Stack</b> &mdash; Python &middot; sentence embeddings &middot; gradient boosting &middot; PyTorch &middot; pandas</div>
</div></section>
"""),

"agent": dict(
  title="Operations agent for local businesses",
  desc="An n8n and GPT API agent that reads reviews, email and bookings together and turns them into replies and staffing suggestions.",
  tag="Side project &middot; n8n + GPT API &middot; 2026",
  h1="An operations agent for appointment-driven businesses",
  lede="Salons, restaurants and small clinics run on appointments and reputation, and both arrive as a mess of notifications. This reads <b>reviews, inbox and bookings together</b> and turns them into something the owner can act on.",
  body="""
<section><div class="col">
  <h2>What it does</h2>
  <ul class="clean">
    <li>Watches Google reviews and drafts a reply in the owner's voice, with the tone set by the rating rather than by a single template</li>
    <li>Handles routine customer email &mdash; hours, availability, pricing questions &mdash; with the context of what is actually on the calendar</li>
    <li>Reads review, email and booking signals together to find the demand pattern, then suggests when to add or cut a shift</li>
  </ul>

  <h2>Why the three streams have to be read together</h2>
  <p>Any one of them on its own is misleading. Reviews tell you how last week felt but not how busy it was. Bookings tell you volume but not why Thursday collapsed. Email is where the cancellations and the special requests hide. The useful signal only appears when they are lined up on the same timeline.</p>
  <p>This is the same problem as the lending assistant in a smaller form: the model is good at reading unstructured text and terrible at being trusted with the arithmetic. It drafts and classifies; the scheduling suggestion comes from counting.</p>
  <div class="stack"><b>Stack</b> &mdash; n8n &middot; GPT API &middot; Google Business Profile &middot; scheduled workflows</div>
</div></section>
"""),

"ranking": dict(
  title="Retrieval and ranking for literature",
  desc="A two-stage retrieval and learning-to-rank pipeline that cuts how much a systematic reviewer has to read.",
  tag="Research project &middot; learning to rank &middot; 2024",
  h1="Retrieval and ranking for academic literature",
  lede="A two-stage pipeline: topic modelling and cosine similarity generate candidates, then <b>LambdaMART</b> reranks them. Built for systematic review, where the cost is measured in how much a human has to read.",
  body="""
<section><div class="col">
  <div class="stats">
    <div><b>15%</b><span>WSS@95 over baseline</span></div>
    <div><b>2</b><span>stage pipeline</span></div>
  </div>

  <h2>Two stages, two different jobs</h2>
  <p>Stage one is recall. LDA topic modelling and TF-IDF cosine similarity pull a candidate set wide enough that the relevant papers are almost certainly inside it. Precision at this stage does not matter much; missing something does.</p>
  <p>Stage two is order. LambdaMART reranks the candidates, trained against NDCG so that getting the top of the list right counts for more than getting the tail right. That is the correct shape for the objective, because nobody reads the tail.</p>

  <h2>Why WSS@95 is the metric that matters here</h2>
  <p>Accuracy and F1 both miss the point of a systematic review. The reviewer is not going to accept missing relevant papers, so recall is effectively fixed near the top. The real question is <b>how much reading it takes to get there</b>.</p>
  <p>Work Saved over Sampling at 95% recall measures exactly that: the fraction of the corpus a reviewer no longer has to screen while still finding 95% of what matters. A <b>15% improvement</b> over a logistic regression baseline is 15% of a reading pile that a person does not have to go through.</p>

  <div class="aside">
    Choosing the metric was most of the work. The same model looks unremarkable under accuracy and clearly useful under WSS@95, because only one of those two is measuring the thing the user actually pays for.
  </div>
  <div class="stack"><b>Stack</b> &mdash; Python &middot; LDA &middot; TF-IDF &middot; LambdaMART &middot; linear SVM with SGD</div>
</div></section>
"""),
}

ORDER = ["hef","esg","agent","ranking"]
LABEL = {"hef":"HEF Funding Navigator","esg":"ESG signals from news and filings",
         "agent":"Operations agent for local businesses","ranking":"Retrieval and ranking for literature"}

for i,key in enumerate(ORDER):
    p = PAGES[key]
    nxt = ORDER[(i+1) % len(ORDER)]
    prv = ORDER[(i-1) % len(ORDER)]
    nav = (f'<a href="{prv}.html"><span class="l">Previous</span><span class="t">{LABEL[prv]}</span></a>\n    '
           f'<a href="{nxt}.html"><span class="l">Next</span><span class="t">{LABEL[nxt]}</span></a>')
    html = HEAD.format(title=p["title"], desc=p["desc"], tag=p["tag"], h1=p["h1"], lede=p["lede"]) \
         + p["body"] + FOOT.format(nav=nav)
    with io.open(os.path.join(OUT, key+".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote projects/%s.html  %d bytes" % (key, len(html)))
