# Playground Games

A curated set of HTML5 canvas games built with my son, served by the [playground platform](https://github.com/ianlin0126/playground).

Each game is a self-contained folder with its own assets — no shared external dependencies between games.

## Games

- **`space-shooter/`** — Polished sci-fi shooter with a custom sprite atlas, three boss tiers, easy/normal mode selector, and a shop. Mobile-first.
- **`space-shooter-2/`** — Earlier shooter using [Kenney's Space Shooter Remastered](https://kenney.nl/) asset pack (CC0).
- **`fruit-ninja/`** — Slice fruit, miss bombs.
- **`ocean-world-evolution/`** — Evolution-themed underwater game.

## Layout

```
games/<slug>/
  index.html     # the game
  assets/        # per-game custom artwork (when applicable)
  design.md      # design doc (when applicable)
  plan.md        # implementation plan (when applicable)
```

Per-game asset folders mean each game is independently movable / clonable / publishable.
