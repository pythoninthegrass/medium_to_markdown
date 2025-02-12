#!/usr/bin/env python

from markdownify import markdownify
from pathlib import Path

file_list = sorted(Path('./data/bookmarks').glob('*.html'))

md_text_list = []

for file_path in file_list:
    html_file = open(file_path, "r").read()
    md_text = markdownify(html_file)
    md_text_list.append("##" + md_text.split("###")[1])

fp = Path("data/bookmarks.md").resolve()
fp.parent.mkdir(exist_ok=True)
fp.touch()

with open(fp, "w") as f:
    for i, md_text in enumerate(md_text_list):
        f.write(md_text)
        if i < len(md_text_list) - 1:
            f.write("\n")
