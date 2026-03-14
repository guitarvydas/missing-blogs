#!/usr/bin/env python3
"""
analyze_corpus.py — Book preparation analysis for a markdown blog corpus.

Usage:
    python3 analyze_corpus.py <directory> [options]

Options:
    --clusters N        Number of theme clusters (default: 12)
    --top-keywords N    Keywords per cluster to show (default: 15)
    --sim-threshold F   Cosine similarity threshold for near-duplicates (default: 0.75)
    --out FILE          Output report filename (default: corpus_analysis.md)

Example:
    python3 analyze_corpus.py ~/myblog --clusters 10 --out report.md

Requires: scikit-learn (pip install scikit-learn)
"""

import os
import re
import sys
import json
import math
import argparse
import hashlib
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

# ── sklearn is the only non-stdlib dependency ───────────────────────────────
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
except ImportError:
    sys.exit("ERROR: scikit-learn not found.\n  pip install scikit-learn")


# ── Stopwords (no nltk needed) ───────────────────────────────────────────────
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


# ── Helpers ──────────────────────────────────────────────────────────────────

def extract_frontmatter(text):
    """Extract YAML-style frontmatter if present. Returns (meta_dict, body)."""
    meta = {}
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            fm = text[3:end].strip()
            for line in fm.splitlines():
                if ':' in line:
                    k, _, v = line.partition(':')
                    meta[k.strip().lower()] = v.strip().strip('"\'')
            text = text[end + 4:].strip()
    return meta, text


def guess_date(filepath, meta):
    """Try to extract a date from frontmatter, filename, or file mtime."""
    # Frontmatter
    for key in ('date', 'published', 'created', 'updated'):
        val = meta.get(key, '')
        m = re.search(r'(\d{4})-(\d{2})-(\d{2})', val)
        if m:
            return m.group(0)
    # Filename  e.g. 2023-04-15-my-post.md  or  20230415-title.md
    fname = filepath.stem
    m = re.search(r'(\d{4}[-_]\d{2}[-_]\d{2})', fname)
    if m:
        return m.group(1).replace('_', '-')
    m = re.search(r'(\d{8})', fname)
    if m:
        d = m.group(1)
        return f"{d[:4]}-{d[4:6]}-{d[6:8]}"
    # Fallback: file modification time
    mtime = filepath.stat().st_mtime
    return datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')


def clean_markdown(text):
    """Strip markdown syntax for plain-text analysis."""
    text = re.sub(r'```.*?```', ' ', text, flags=re.DOTALL)   # code blocks
    text = re.sub(r'`[^`]+`', ' ', text)                       # inline code
    text = re.sub(r'!\[.*?\]\(.*?\)', ' ', text)               # images
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)       # links → label
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE) # headings
    text = re.sub(r'[*_~]{1,3}', '', text)                     # emphasis
    text = re.sub(r'^\s*[-*+>|]\s*', ' ', text, flags=re.MULTILINE)
    text = re.sub(r'\s+', ' ', text)
    return text.lower().strip()


def extract_title(meta, text, filepath):
    """Best-effort title: frontmatter → first H1 → filename."""
    if meta.get('title'):
        return meta['title']
    m = re.search(r'^#\s+(.+)', text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return filepath.stem.replace('-', ' ').replace('_', ' ')


# Directories that commonly contain generated/duplicated copies of source files.
# Add your own if needed (e.g. 'out', 'build', 'cache').
SKIP_DIRS = {
    '_site', 'public', 'dist', 'build', 'out', 'output',
    'node_modules', '.git', '.obsidian', '__pycache__',
    'vendor', 'cache', '.cache',
    'backup',
}

def load_corpus(directory):
    """Load all .md files from directory tree. Returns list of doc dicts."""
    docs = []
    seen_paths  = set()   # canonical paths - fast first check
    seen_hashes = set()   # content hashes - catches copies anywhere in the tree

    for path in sorted(Path(directory).rglob('*.md')):
        # Skip files inside known generated/backup directories
        if any(part in SKIP_DIRS for part in path.parts):
            continue

        # Deduplicate by canonical path (catches symlinks)
        canon = path.resolve()
        if canon in seen_paths:
            continue
        seen_paths.add(canon)

        try:
            raw = path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        if len(raw.strip()) < 100:          # skip near-empty files
            continue
        meta, body = extract_frontmatter(raw)
        clean = clean_markdown(body)
        word_count = len(clean.split())
        if word_count < 50:
            continue

        # Deduplicate by content hash - catches copies wherever they live
        content_hash = hashlib.md5(clean.encode()).hexdigest()
        if content_hash in seen_hashes:
            continue
        seen_hashes.add(content_hash)

        docs.append({
            'path':       path,
            'rel':        str(path),
            'title':      extract_title(meta, raw, path),
            'date':       guess_date(path, meta),
            'meta':       meta,
            'raw':        raw,
            'clean':      clean,
            'lines':      raw.count('\n'),
            'words':      word_count,
            'md5':        content_hash,
        })
    return docs

def exact_duplicates(docs):
    """Group docs with identical cleaned content."""
    groups = defaultdict(list)
    for d in docs:
        groups[d['md5']].append(d)
    return {k: v for k, v in groups.items() if len(v) > 1}


def near_duplicates(docs, tfidf_matrix, threshold=0.75):
    """Find pairs with cosine similarity above threshold (excluding exact dupes)."""
    pairs = []
    # Process in chunks to avoid O(n²) memory for large corpora
    CHUNK = 50
    n = len(docs)
    seen = set()
    for i in range(0, n, CHUNK):
        chunk = tfidf_matrix[i:i+CHUNK]
        sims = cosine_similarity(chunk, tfidf_matrix)
        for ci, row in enumerate(sims):
            gi = i + ci
            for gj, sim in enumerate(row):
                if gj <= gi:
                    continue
                key = (min(gi, gj), max(gi, gj))
                if key in seen:
                    continue
                if sim >= threshold and docs[gi]['md5'] != docs[gj]['md5']:
                    pairs.append((sim, docs[gi], docs[gj]))
                    seen.add(key)
    pairs.sort(key=lambda x: -x[0])
    return pairs


def cluster_documents(docs, tfidf_matrix, n_clusters=12):
    """K-means clustering. Returns cluster labels array."""
    n = min(n_clusters, len(docs))
    km = KMeans(n_clusters=n, random_state=42, n_init='auto', max_iter=300)
    labels = km.fit_predict(tfidf_matrix)
    return labels, km


def top_cluster_keywords(km, vectorizer, n_clusters, top_n=15):
    """Extract top TF-IDF keywords for each cluster centroid."""
    terms = vectorizer.get_feature_names_out()
    cluster_kws = {}
    for i, centroid in enumerate(km.cluster_centers_):
        top_idx = centroid.argsort()[-top_n:][::-1]
        cluster_kws[i] = [terms[j] for j in top_idx]
    return cluster_kws


def global_keywords(docs, vectorizer, tfidf_matrix, top_n=40):
    """Corpus-wide most significant terms."""
    mean_scores = np.asarray(tfidf_matrix.mean(axis=0)).flatten()
    top_idx = mean_scores.argsort()[-top_n:][::-1]
    terms = vectorizer.get_feature_names_out()
    return [(terms[i], float(mean_scores[i])) for i in top_idx]


def timeline_stats(docs):
    """Year-by-year article counts and word counts."""
    by_year = defaultdict(lambda: {'count': 0, 'words': 0, 'titles': []})
    for d in docs:
        year = d['date'][:4] if d['date'] else 'unknown'
        by_year[year]['count'] += 1
        by_year[year]['words'] += d['words']
        by_year[year]['titles'].append(d['title'])
    return dict(sorted(by_year.items()))


def suggest_cluster_name(keywords):
    """Heuristic: join top 3 keywords as a cluster label."""
    return ' / '.join(keywords[:3])


# ── Report generation ────────────────────────────────────────────────────────

def bar(value, max_value, width=30, char='█'):
    filled = int(round(width * value / max_value)) if max_value else 0
    return char * filled + '░' * (width - filled)


def write_report(docs, labels, km, vectorizer, tfidf_matrix,
                 n_clusters, top_n_kw, sim_threshold, outfile):

    cluster_kws  = top_cluster_keywords(km, vectorizer, n_clusters, top_n_kw)
    global_kws   = global_keywords(docs, vectorizer, tfidf_matrix)
    timeline     = timeline_stats(docs)
    exact_dupes  = exact_duplicates(docs)
    near_dupes   = near_duplicates(docs, tfidf_matrix, sim_threshold)

    # Attach cluster label to each doc
    for i, d in enumerate(docs):
        d['cluster'] = int(labels[i])

    # Group docs by cluster
    clusters = defaultdict(list)
    for d in docs:
        clusters[d['cluster']].append(d)

    total_words = sum(d['words'] for d in docs)
    total_lines = sum(d['lines'] for d in docs)

    lines = []
    w = lines.append

    w("# Corpus Analysis Report")
    w(f"\n_Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} · "
      f"{len(docs)} documents · {total_words:,} words · {total_lines:,} lines_\n")

    # ── 1. Overview ──────────────────────────────────────────────────────────
    w("---\n## 1. Overview\n")
    w(f"| Metric | Value |")
    w(f"|--------|-------|")
    w(f"| Documents analysed | {len(docs)} |")
    w(f"| Total words | {total_words:,} |")
    w(f"| Total lines | {total_lines:,} |")
    w(f"| Average article length | {total_words // len(docs):,} words |")
    w(f"| Longest article | {max(d['words'] for d in docs):,} words |")
    w(f"| Shortest article | {min(d['words'] for d in docs):,} words |")
    w(f"| Exact duplicate groups | {len(exact_dupes)} |")
    w(f"| Near-duplicate pairs (≥{sim_threshold}) | {len(near_dupes)} |")
    w(f"| Theme clusters | {n_clusters} |")

    # ── 2. Global Keywords ───────────────────────────────────────────────────
    w("\n---\n## 2. Corpus-Wide Keywords\n")
    w("_These are the concepts that define your entire body of work._\n")
    max_score = global_kws[0][1] if global_kws else 1
    for term, score in global_kws[:30]:
        pct = int(100 * score / max_score)
        w(f"- **{term}** `{bar(score, max_score, 20)}` {pct}%")

    # ── 3. Timeline ──────────────────────────────────────────────────────────
    w("\n---\n## 3. Timeline\n")
    max_count = max(v['count'] for v in timeline.values()) if timeline else 1
    w("| Year | Articles | Words | Output |")
    w("|------|----------|-------|--------|")
    for year, data in timeline.items():
        w(f"| {year} | {data['count']} | {data['words']:,} | "
          f"`{bar(data['count'], max_count, 20)}` |")

    # ── 4. Theme Clusters ────────────────────────────────────────────────────
    w("\n---\n## 4. Theme Clusters\n")
    w("_Each cluster is a natural chapter candidate. "
      "Keywords are the centroid's top TF-IDF terms._\n")

    cluster_sizes = {k: len(v) for k, v in clusters.items()}
    sorted_clusters = sorted(clusters.keys(),
                              key=lambda k: -cluster_sizes[k])

    for ci, cid in enumerate(sorted_clusters):
        cdocs = clusters[cid]
        kws = cluster_kws[cid]
        name = suggest_cluster_name(kws)
        word_total = sum(d['words'] for d in cdocs)
        cdocs_sorted = sorted(cdocs, key=lambda d: d['date'], reverse=True)

        w(f"\n### Cluster {ci+1}: _{name}_\n")
        w(f"**{len(cdocs)} articles · {word_total:,} words**\n")
        w(f"**Keywords:** {', '.join(f'`{k}`' for k in kws)}\n")
        w("**Articles:**\n")
        for d in cdocs_sorted[:25]:   # cap at 25 per cluster in report
            w(f"- [{d['title']}]({d['rel']}) _{d['date']}_ ({d['words']:,}w)")
        if len(cdocs) > 25:
            w(f"- _...and {len(cdocs) - 25} more_")

    # ── 5. Near-Duplicates ───────────────────────────────────────────────────
    w("\n---\n## 5. Near-Duplicate Pairs\n")
    if not near_dupes:
        w("_No near-duplicates found at the current threshold._\n")
    else:
        w(f"_{len(near_dupes)} pairs with similarity ≥ {sim_threshold}. "
          "These are merge/prune candidates._\n")
        w("| Similarity | Article A | Article B |")
        w("|-----------|-----------|-----------|")
        for sim, da, db in near_dupes[:50]:
            w(f"| {sim:.2f} | [{da['title']}]({da['rel']}) | "
              f"[{db['title']}]({db['rel']}) |")
        if len(near_dupes) > 50:
            w(f"\n_...and {len(near_dupes) - 50} more pairs. "
              "Increase --sim-threshold to reduce noise._")

    # ── 6. Exact Duplicates ──────────────────────────────────────────────────
    w("\n---\n## 6. Exact Duplicates\n")
    if not exact_dupes:
        w("_No exact duplicates found._\n")
    else:
        w(f"_{len(exact_dupes)} groups of files with identical content:_\n")
        for md5, group in exact_dupes.items():
            w(f"\n**Group** `{md5[:8]}`:")
            for d in group:
                w(f"  - {d['rel']}")

    # ── 7. Book Outline Scaffold ─────────────────────────────────────────────
    w("\n---\n## 7. Suggested Book Outline Scaffold\n")
    w("_Cluster names auto-generated from top keywords. "
      "Rename to match your vision._\n")
    for ci, cid in enumerate(sorted_clusters):
        cdocs = clusters[cid]
        kws = cluster_kws[cid]
        name = suggest_cluster_name(kws)
        word_total = sum(d['words'] for d in cdocs)
        w(f"\n### Part {ci+1}: {name.title()}")
        w(f"> {len(cdocs)} source articles · ~{word_total:,} raw words\n")
        w("**Possible chapter breakdown:**")
        # Suggest sub-chapters from the top-15 keywords beyond the first 3
        sub_kws = kws[3:9]
        for j, kw in enumerate(sub_kws, 1):
            w(f"  {j}. {kw.title()}")
        w(f"\n**Key source articles:**")
        for d in sorted(cdocs, key=lambda d: -d['words'])[:5]:
            w(f"  - {d['title']} ({d['words']:,}w)")

    # ── 8. JSON dump for further processing ──────────────────────────────────
    json_path = outfile.replace('.md', '.json')
    export = []
    for d in docs:
        export.append({
            'title':   d['title'],
            'path':    d['rel'],
            'date':    d['date'],
            'words':   d['words'],
            'lines':   d['lines'],
            'cluster': d['cluster'],
            'cluster_keywords': cluster_kws[d['cluster']],
        })
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(export, f, indent=2, ensure_ascii=False)

    w(f"\n---\n## 9. Machine-Readable Data\n")
    w(f"Full per-article cluster assignments exported to `{json_path}`.\n")
    w("Fields: `title`, `path`, `date`, `words`, `lines`, "
      "`cluster`, `cluster_keywords`\n")

    report = '\n'.join(lines)
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(report)

    return report, json_path


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('directory', help='Root directory containing .md files')
    ap.add_argument('--clusters',       type=int,   default=12,   metavar='N')
    ap.add_argument('--top-keywords',   type=int,   default=15,   metavar='N')
    ap.add_argument('--sim-threshold',  type=float, default=0.75, metavar='F')
    ap.add_argument('--out',            type=str,   default='corpus_analysis.md')
    args = ap.parse_args()

    directory = args.directory
    if not os.path.isdir(directory):
        sys.exit(f"ERROR: Directory not found: {directory}")

    print(f"[1/5] Scanning {directory} for .md files...")
    docs = load_corpus(directory)
    if not docs:
        sys.exit("No usable markdown files found.")
    print(f"      Found {len(docs)} documents ({sum(d['words'] for d in docs):,} words)")

    print("[2/5] Building TF-IDF matrix...")
    vectorizer = TfidfVectorizer(
        stop_words=list(STOPWORDS),
        max_features=8000,
        min_df=2,           # term must appear in ≥2 docs
        max_df=0.85,        # ignore terms in >85% of docs
        ngram_range=(1, 2), # unigrams + bigrams
        sublinear_tf=True,
    )
    texts = [d['clean'] for d in docs]
    tfidf_matrix = vectorizer.fit_transform(texts)
    print(f"      Matrix: {tfidf_matrix.shape[0]} docs × {tfidf_matrix.shape[1]} features")

    n_clusters = min(args.clusters, len(docs))
    print(f"[3/5] Clustering into {n_clusters} groups (K-Means)...")
    labels, km = cluster_documents(docs, tfidf_matrix, n_clusters)

    print(f"[4/5] Finding near-duplicates (threshold={args.sim_threshold})...")
    # Note: for 352 docs this is fast; >1000 docs may take a minute

    print(f"[5/5] Writing report to {args.out} ...")
    report, json_path = write_report(
        docs, labels, km, vectorizer, tfidf_matrix,
        n_clusters, args.top_keywords, args.sim_threshold, args.out
    )

    print(f"\n✓  Report:  {args.out}")
    print(f"✓  JSON:    {json_path}")
    print(f"\nTip: run with --clusters 8 or --clusters 16 to tune granularity.")
    print(f"Tip: lower --sim-threshold to 0.65 to find softer near-dupes.")


if __name__ == '__main__':
    main()
