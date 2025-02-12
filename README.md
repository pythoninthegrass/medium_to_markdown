# medium_to_markdown

Inspiration from [A simple way to export your Medium’s reading list to a Markdown file by Eryk Lewinson](https://medium.com/geekculture/a-simple-way-to-export-your-mediums-reading-list-to-a-markdown-file-139e9861bf2)

## Minimum Requirements

* [Python 3.11+](https://www.python.org/downloads/)

## Setup

### Repo

```bash
# clone the repo
git clone https://github.com/pythoninthegrass/medium_to_markdown.git

# setup the virtual environment
python -m venv .venv

# activate the virtual environment
source .venv/bin/activate

# install the dependencies
python -m pip install -r requirements.txt
```

### Medium

Export your bookmarks from Medium. They're in your [account](https://medium.com/me/settings#account) settings under **Security and apps**.

Extract the zip file into the `data` directory.

## Usage

```bash
# run the script
python main.py

# deactivate the virtual environment
deactivate
```

## Benchmark

Two for loops, one to iterate over HTML files and another to append to the bookmarks markdown file.

```bash
# sync
λ hyperfine ./main.py --warmup 1
Benchmark 1: ./main.py
  Time (mean ± σ):     154.7 ms ±   3.1 ms    [User: 146.3 ms, System: 6.7 ms]
  Range (min … max):   151.1 ms … 162.6 ms    19 runs

# async
λ hyperfine ./main.py --warmup 1
Benchmark 1: ./main.py
  Time (mean ± σ):     172.2 ms ±   3.0 ms    [User: 159.1 ms, System: 11.7 ms]
  Range (min … max):   168.6 ms … 179.3 ms    17 runs

# multiprocessing
λ hyperfine ./main.py --warmup 1
Benchmark 1: ./main.py
  Time (mean ± σ):     157.0 ms ±   4.9 ms    [User: 994.9 ms, System: 186.5 ms]
  Range (min … max):   149.1 ms … 168.1 ms    19 runs
```

Turns out, the async version is slower than the sync version. The multiprocessing version is slightly faster than the sync version, but slower than the async version and uses more CPU resources.

The sync version is the fastest.

## TODO

* Scrape the Medium links and generate a PDF or EPUB file.
* Build a website
