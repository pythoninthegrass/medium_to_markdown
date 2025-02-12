# medium_to_markdown

## Benchmark

### Naive approach

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
