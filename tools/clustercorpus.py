#!/usr/bin/env python3
"""
cluster_corpus.py — Theme-cluster a markdown blog corpus for book preparation.

Usage:
    python3 cluster_corpus.py <directory> [options]

Options:
    --clusters N        Number of theme clusters / book parts (default: 12)
    --top-keywords N    Keywords shown per cluster (default: 15)
    --out FILE          Output report filename (default: clusters.md)

Example:
    python3 cluster_corpus.py ~/myblog --clusters 10 --out clusters.md

Requires:  pip install scikit-learn
"""

import os
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans
    import numpy as np
except ImportError:
    sys.exit("ERROR: scikit-learn not found.\n  pip install scikit-learn")

# ── Stopwords (no nltk needed) ────────────────────────────────────────────────
STOPWORDS = set("""
a about above after again against all also am an and any are aren't as at
be because been before being below between both but by can't cannot could
couldn't did didn't do does doesn't doing don't down during each even ever
every few for from further get go got had hadn't has hasn't have haven't
having he he'd he'll he's her here here's hers herself him himself his
how how's i i'd i'll i'm i've if in into is isn't it it's its itself
just know let's like ll me more most mustn't my myself need no nor not
now of off on once only or other ought our ours ourselves out over own
re same say shan't she she'd she'll she's should shouldn't so some such
than that that's the their theirs them themselves then there there's
these they they'd they'll they're they've this those through to too
under until up use very ve was wasn't we we'd we'll we're we've were
weren't what what's when when's where where's which while who who's
whom why why's will with won't would wouldn't you you'd you'll you're
you've your yours yourself yourselves
also get can one way may make made used using use want need many
much still well even though already now see think know look
""".split())

# ── Helpers ───────────────────────────────────────────────────────────────────

def extract_frontmatter(text):
    meta = {}
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            for line in text[3:end].splitlines():
                if ':' in line:
                    k, _, v = line.partition(':')
                    meta[k.strip().lower()] = v.strip().strip('"\'')
            text = text[end + 4:].strip()
    return meta, text

def guess_date(path, meta):
    for key in ('date', 'published', 'created'):
        m = re.search(r'(\d{4}-\d{2}-\d{2})', meta.get(key, ''))
        if m:
            return m.group(1)
    m = re.search(r'(\d{4}[-_]\d{2}[-_]\d{2})', path.stem)
    if m:
        return m.group(1).replace('_', '-')
    return datetime.fromtimestamp(path.stat().st_mtime).strftime('%Y-%m-%d')

def extract_title(meta, raw, path):
    if meta.get('title'):
        return meta['title']
    m = re.search(r'^#\s+(.+)', raw, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return path.stem.replace('-', ' ').replace('_', ' ')

def clean_markdown(text):
    text = re.sub(r'```.*?```', ' ', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', ' ', text)
    text = re.sub(r'!\[.*?\]\(.*?\)', ' ', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[*_~]{1,3}', '', text)
    text = re.sub(r'^\s*[-*+>|]\s*', ' ', text, flags=re.MULTILINE)
    text = re.sub(r'\s+', ' ', text)
    return text.lower().strip()

def load_corpus(directory):
    docs = []
    for path in sorted(Path(directory).rglob('*.md')):
        try:
            raw = path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        if len(raw.strip()) < 100:
            continue
        meta, body = extract_frontmatter(raw)
        clean = clean_markdown(body)
        words = len(clean.split())
        if words < 50:
            continue
        docs.append({
            'path':   path,
            'rel':    str(path),
            'title':  extract_title(meta, raw, path),
            'date':   guess_date(path, meta),
            'clean':  clean,
            'words':  words,
            'lines':  raw.count('\n'),
        })
    return docs

# ── Clustering ────────────────────────────────────────────────────────────────

def build_tfidf(docs):
    vectorizer = TfidfVectorizer(
        stop_words=list(STOPWORDS),
        max_features=8000,
        min_df=2,
        max_df=0.85,
        ngram_range=(1, 2),
        sublinear_tf=True,
    )
    matrix = vectorizer.fit_transform([d['clean'] for d in docs])
    return vectorizer, matrix

def cluster(docs, matrix, n_clusters):
    n = min(n_clusters, len(docs))
    km = KMeans(n_clusters=n, random_state=42, n_init='auto', max_iter=300)
    labels = km.fit_predict(matrix)
    for i, d in enumerate(docs):
        d['cluster'] = int(labels[i])
    return km

def top_keywords(km, vectorizer, top_n):
    terms = vectorizer.get_feature_names_out()
    return {
        i: [terms[j] for j in centroid.argsort()[-top_n:][::-1]]
        for i, centroid in enumerate(km.cluster_centers_)
    }

# ── Report ────────────────────────────────────────────────────────────────────

def write_report(docs, km, vectorizer, top_n, outfile):
    kws     = top_keywords(km, vectorizer, top_n)
    by_cluster = defaultdict(list)
    for d in docs:
        by_cluster[d['cluster']].append(d)

    # Sort clusters largest → smallest
    ordered = sorted(by_cluster.keys(), key=lambda k: -len(by_cluster[k]))

    total_words = sum(d['words'] for d in docs)
    lines = []
    w = lines.append

    w("# Theme Clusters — Book Preparation Report")
    w(f"\n_Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} · "
      f"{len(docs)} articles · {total_words:,} words · "
      f"{len(ordered)} clusters_\n")

    # ── Summary table ─────────────────────────────────────────────────────────
    w("## Summary\n")
    w("| # | Theme (auto-named) | Articles | Words | Top keywords |")
    w("|---|-------------------|----------|-------|--------------|")
    for rank, cid in enumerate(ordered, 1):
        cdocs = by_cluster[cid]
        ckws  = kws[cid]
        name  = ' / '.join(ckws[:3])
        wds   = sum(d['words'] for d in cdocs)
        kw_str = ', '.join(f'`{k}`' for k in ckws[:5])
        w(f"| {rank} | {name} | {len(cdocs)} | {wds:,} | {kw_str} |")

    # ── Per-cluster detail ────────────────────────────────────────────────────
    w("\n---\n## Clusters (detail)\n")
    w("> **How to use this:** Each cluster is a chapter/part candidate.\n"
      "> Rename the heading, pick the articles that belong, discard the rest.\n")

    for rank, cid in enumerate(ordered, 1):
        cdocs = sorted(by_cluster[cid], key=lambda d: d['date'], reverse=True)
        ckws  = kws[cid]
        name  = ' / '.join(ckws[:3])
        wds   = sum(d['words'] for d in cdocs)

        w(f"\n### Part {rank}: _{name.title()}_")
        w(f"\n**{len(cdocs)} articles · {wds:,} words**\n")
        w(f"**Keywords:** {', '.join(f'`{k}`' for k in ckws)}\n")

        # Year spread
        years = sorted(set(d['date'][:4] for d in cdocs if d['date']))
        if years:
            w(f"**Date range:** {years[0]} – {years[-1]}\n")

        w("**Articles** _(newest first)_:\n")
        for d in cdocs:
            w(f"- {d['title']}  \n"
              f"  `{d['rel']}` · {d['date']} · {d['words']:,} words")

    # ── Suggested book scaffold ───────────────────────────────────────────────
    w("\n---\n## Suggested Book Scaffold\n")
    w("_Paste this into your outline doc and rename the parts._\n")
    for rank, cid in enumerate(ordered, 1):
        cdocs = by_cluster[cid]
        ckws  = kws[cid]
        name  = ' / '.join(ckws[:3]).title()
        wds   = sum(d['words'] for d in cdocs)
        w(f"\n**Part {rank}: {name}**  _{len(cdocs)} source articles, ~{wds:,} raw words_")
        # Suggest chapter stubs from keywords 4-9
        for j, kw in enumerate(ckws[3:9], 1):
            w(f"  - Chapter {rank}.{j}: {kw.title()}")

    report = '\n'.join(lines)
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(report)

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('directory')
    ap.add_argument('--clusters',      type=int, default=12, metavar='N')
    ap.add_argument('--top-keywords',  type=int, default=15, metavar='N')
    ap.add_argument('--out',           type=str, default='clusters.md')
    args = ap.parse_args()

    if not os.path.isdir(args.directory):
        sys.exit(f"ERROR: not a directory: {args.directory}")

    print(f"[1/4] Scanning {args.directory}...")
    docs = load_corpus(args.directory)
    if not docs:
        sys.exit("No usable .md files found.")
    print(f"      {len(docs)} documents · {sum(d['words'] for d in docs):,} words")

    print("[2/4] Building TF-IDF matrix...")
    vectorizer, matrix = build_tfidf(docs)
    print(f"      {matrix.shape[0]} docs × {matrix.shape[1]} features")

    n = min(args.clusters, len(docs))
    print(f"[3/4] K-Means clustering → {n} clusters...")
    km = cluster(docs, matrix, n)

    print(f"[4/4] Writing {args.out}...")
    write_report(docs, km, vectorizer, args.top_keywords, args.out)

    print(f"\n✓  {args.out}")
    print(f"\nTips:")
    print(f"  --clusters 8     fewer, broader parts")
    print(f"  --clusters 16    more granular chapters")
    print(f"  --top-keywords 20  see more keywords per cluster")

if __name__ == '__main__':
    main()
