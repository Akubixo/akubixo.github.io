"""Rubric self-check. Run from the site folder:  python check_site.py
Checks: local links/images exist, name + brand on every page, every
figure has a caption, no in-page bookmark links, and lists TO-FILL boxes."""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = [f for f in os.listdir(ROOT) if f.endswith(".html")]
problems, todos = [], []


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.refs = []; s.figs = 0; s.caps = 0; s.text = []; s.in_todo = 0; s.todo_buf = []

    def handle_starttag(s, tag, a):
        a = dict(a)
        for k in ("href", "src"):
            if a.get(k): s.refs.append(a[k])
        if tag == "figure": s.figs += 1
        if tag == "figcaption": s.caps += 1
        if "todo" in (a.get("class") or "").split(): s.in_todo = 1

    def handle_endtag(s, tag):
        if s.in_todo and tag == "p":
            todos.append((s.page, " ".join(s.todo_buf).strip())); s.in_todo = 0; s.todo_buf = []

    def handle_data(s, d):
        s.text.append(d)
        if s.in_todo: s.todo_buf.append(d.strip())


for page in sorted(PAGES):
    html = open(os.path.join(ROOT, page), encoding="utf-8").read()
    p = P(); p.page = page; p.feed(html)
    header = html.split("</header>")[0]
    if "Anthony Ranzola" not in header: problems.append(f"{page}: name missing from header")
    if "Level Designer" not in header: problems.append(f"{page}: brand missing from header")
    if p.figs != p.caps: problems.append(f"{page}: {p.figs} figures but {p.caps} captions")
    for r in p.refs:
        if r.startswith(("http", "mailto:", "tel:")): continue
        if r.startswith("#") and r != "#main": problems.append(f"{page}: in-page bookmark link {r}")
        if r.startswith("#"): continue
        if not os.path.exists(os.path.join(ROOT, r.split("#")[0])): problems.append(f"{page}: broken link -> {r}")

print(f"Checked {len(PAGES)} pages.")
print("Problems:" if problems else "No problems found.")
for x in problems: print("  -", x)
print(f"\nTO FILL IN boxes remaining: {len(todos)}")
for pg, t in todos: print(f"  - {pg}: {t[:110]}")
sys.exit(1 if problems or todos else 0)
