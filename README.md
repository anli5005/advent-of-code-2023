# Advent of Code 2023

My Advent of Code 2023 solutions!

Days so far have been written in Python[^1], and take their input from stdin, without trailing newlines.

[^1]: The sole exception is Day 8, which includes a Rust-based brute force solution in the hopes that it would be faster. It was, but not enough

I've been optimizing for speed of implementation, so most of this code is kinda messy lol

I do use GitHub Copilot, but I refrain from feeding the problem statement directly to it for leaderboard solves.

## Scripts

Sourcing `scripts/aoc.zsh` will expose the following commands:

* `setup` creates files for the next day, downloads the current day's input, and opens both VS Code and the problem statement on https://adventofcode.com
    * Note that `setup` naively truncates the last byte of the input in an attempt to remove the newline. This works on my Mac, but YMMV.
* `setuptimer` waits until midnight EST (more specifically, 1 ms after midnight), then runs `setup`. It's intended to be run at times close to midnight like 23:59 - its reliability over longer time periods (or across time zones) has not been tested.
* `a` and `b` run the current `##a.py` or `##b.py` files, piping in `##.txt` as input.
* `as` and `bs` do the same thing as `a` and `b`, but with the current day's `s.txt` (intended to be a sample/test input).

To use `setup`, be sure to paste your Advent of Code session cookie into a file at the root named `.aocsession`. For added convenience, you may want to something like https://github.com/Tarrasch/zsh-autoenv and set up this script to run when you enter the repo:

```zsh
source "$(dirname "$(realpath "$0")")/scripts/aoc.zsh"
```

## Bragging Rights

| Day | Rank |
| --- | --- |
| Day 2 (Part A) | 28 |
| Day 2 (Part B) | 58 |
| Day 4 (Part B) | 46 |
| Day 7 (Part B) | 99 |
| Day 8 (Part A) | 72 |
| Day 10 (Part A) | 9 |
| Day 13 (Part A) | 68 |
| Day 14 (Part A) | 42 |
| Day 14 (Part B) | 69 |
| Day 15 (Part A) | 42 |
| Day 15 (Part B) | 17 |
| Day 16 (Part A) | 26 |
| Day 16 (Part B) | 33 |
| Day 17 (Part A) | 57 |
| Day 17 (Part B) | 23 |
| Day 18 (Part A) | 67 |