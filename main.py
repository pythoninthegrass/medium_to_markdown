#!/usr/bin/env python

import aiofiles
import asyncio
from markdownify import markdownify
from pathlib import Path

async def process_file(file_path):
    async with aiofiles.open(file_path, "r") as f:
        html_file = await f.read()
    md_text = markdownify(html_file)
    return "##" + md_text.split("###")[1]

async def write_results(fp, md_text_list):
    async with aiofiles.open(fp, "w") as f:
        for i, md_text in enumerate(md_text_list):
            await f.write(md_text)
            if i < len(md_text_list) - 1:
                await f.write("\n")

async def main():
    file_list = sorted(Path('./data/bookmarks').glob('*.html'))

    # Process all files in parallel
    tasks = [process_file(file_path) for file_path in file_list]
    md_text_list = await asyncio.gather(*tasks)

    # Write results
    fp = Path("data/bookmarks.md").resolve()
    fp.parent.mkdir(exist_ok=True)
    fp.touch()

    await write_results(fp, md_text_list)

if __name__ == "__main__":
    asyncio.run(main())
