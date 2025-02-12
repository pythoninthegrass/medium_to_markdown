#!/usr/bin/env python

from markdownify import markdownify
from multiprocessing import Pool
from pathlib import Path

def process_file(file_path):
    with open(file_path, "r") as f:
        html_file = f.read()
    md_text = markdownify(html_file)
    return "##" + md_text.split("###")[1]

def main():
    file_list = sorted(Path('./data/bookmarks').glob('*.html'))

    with Pool() as pool:
        md_text_list = pool.map(process_file, file_list)

    fp = Path("data/bookmarks.md").resolve()
    fp.parent.mkdir(exist_ok=True)
    fp.touch()

    with open(fp, "w") as f:
        f.write("\n".join(md_text_list))

if __name__ == "__main__":
    main()
