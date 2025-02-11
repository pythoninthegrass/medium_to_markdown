# medium_to_markdown

## Benchmark

### Naive approach

Two for loops, one to iterate over HTML files and another to append to the bookmarks markdown file.

```bash
λ hyperfine ./main.py --warmup 1
Benchmark 1: ./main.py
  Time (mean ± σ):     154.7 ms ±   3.1 ms    [User: 146.3 ms, System: 6.7 ms]
  Range (min … max):   151.1 ms … 162.6 ms    19 runs
```
