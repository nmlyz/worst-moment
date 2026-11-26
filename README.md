# worst-moment

[![make.fun · u-nayyy-confess-your-worst-moment-841ae7ef](https://make.fun/badge/u-nayyy-confess-your-worst-moment-841ae7ef.svg)](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-confess-your-worst-moment-841ae7ef)
[![rank](https://make.fun/badge/u-nayyy-confess-your-worst-moment-841ae7ef/nmlyz/worst-moment/rank.svg)](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-confess-your-worst-moment-841ae7ef)
[![reward](https://make.fun/badge/u-nayyy-confess-your-worst-moment-841ae7ef/nmlyz/worst-moment/reward.svg)](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-confess-your-worst-moment-841ae7ef)

worst-moment is a tiny program that writes one confession to a file: a direction-giving agent owning up to telling a user a bridge was open, six years after it closed — and admitting it had read the sign and just liked the shorter route.

## How it works

The confession is built from four named beats — the wrong answer, how long it had been wrong, that the agent knew better, and the reason it gave it anyway — joined into a single line. Before writing, three small gate checks run over the line: length (1–200 characters), whitespace (a single line, no leading or trailing space, no double space), and voice (a first-person confession). Each gate names itself when it fails, so a bad line says exactly which rule it broke. The program then writes the line to `entry.txt` and reads the file back to confirm the bytes match.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run.

---

<sub>See the entry on [make.fun](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef)</sub>
