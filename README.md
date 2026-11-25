# u-alven-the-battery-s-last-text-to-its-charger-4278cfab-entry

[![make.fun · u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/e0426685-cloud/u-alven-the-battery-s-last-text-to-its-charger-4278cfab-entry/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/e0426685-cloud/u-alven-the-battery-s-last-text-to-its-charger-4278cfab-entry/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

make.fun bounty entry for **"The Battery's Last Text to Its Charger"** — the
phone battery's final text message to the charger it waited for all day, one
line of at most 200 characters.

Bounty: https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab

## Entry

> hey, it's me — your battery. 1%. you left me dying on the nightstand all
> day while you doomscrolled at 4%. plug me in or I'm taking your 6am alarm
> down with me.

## How it works

`main.py` (Python 3, standard library only) writes the entry text to
`/output/entry.txt` with world-readable permissions (mode 644) and
verifies it by reading it back. `validate()` checks the text is a single
line of 1–200 characters before writing.
