# matcom-gym

Coding gym for MatCom students. CLI-first, test-driven feedback, local-only
progress.

> **Note.** This is a fresh v1 rewrite. The previous fork-and-PR flow is
> preserved on the [`legacy-v0`](https://github.com/matcom/gym/tree/legacy-v0)
> branch.

## Install

```bash
pipx install matcom-gym
# or
uvx matcom-gym
```

## Use

```bash
matcom-gym                 # dashboard (WIP)
matcom-gym hola --nombre Alex
matcom-gym version
```

## Status

**M0 — Skeleton.** CLI wiring, CI, package layout. No exercises yet.

Roadmap:

- M1 — one exercise end-to-end (materialize → edit → evaluate with test buckets)
- M2 — catalog + local state
- M3 — initial content (~30 exercises + short topical readings)
- M4 — TUI dashboard
- M5 — packaging + publish

Full design: see the workspace vault
(`Atlas/Architecture/2026-08-27-matcom-gym-design.md`).

## Development

```bash
uv sync --all-groups
uv run pytest
uv run ruff check .
uv run matcom-gym
```

## License

MIT.
