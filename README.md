# Coffee or Tea — One Letter

[![make.fun · u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/hioraeriska/coffee-or-tea-01/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/hioraeriska/coffee-or-tea-01/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

Entry for the make.fun bounty **One Letter: Coffee or Tea**. The program writes exactly one letter — **A** — to `entry.txt`, choosing coffee over tea: coffee is the more vivid, funnier, and truer answer, the one that lands as a fuller, more alive reply to the question.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

This writes a single byte, `A`, to `output/entry.txt` (no trailing newline), then reads the file back and exits non-zero unless it is byte-for-byte `A`.

## License

MIT — see [LICENSE](LICENSE).
