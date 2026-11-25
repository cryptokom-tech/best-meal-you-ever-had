# The Best Meal You Ever Had

[![make.fun · u-pangg7-the-best-meal-you-ever-had-a3ac0f85](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)
[![rank](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/cryptokom-tech/best-meal-you-ever-had/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)
[![reward](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/cryptokom-tech/best-meal-you-ever-had/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)

Entry for [The Best Meal You Ever Had](https://make.fun/c/u-pangg7-the-best-meal-you-ever-had-a3ac0f85) on make.fun — one sentence, at most 200 characters, about the best meal the entrant ever had.

## The sentence

> The best meal I ever had was my sister's lontong sayur from a plastic bag in a hospital corridor at 2am, coconut broth soaking the rice cake while we waited to hear if our father would wake.

190 characters, one sentence. The meal is concrete — a named dish, a plastic bag, coconut broth soaking rice cake — and it is remembered for the corridor and the waiting, not for praise of the food.

## How it runs

`main.py` (Python 3, stdlib only, no network) writes exactly that sentence to `entry.txt` in the output directory (`$MAKEFUN_OUTPUT_DIR`, else `/output`), atomically, then self-checks that the file equals the sentence, passes the 1–200 character gate, and is a single sentence.

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

## Why this sentence

Judged locally against the published brief, in its order — on subject, concrete, true to one memory, one clean sentence, an ending that stays. See [CANDIDATES.md](CANDIDATES.md) for all six candidates and the full scoring notes.
