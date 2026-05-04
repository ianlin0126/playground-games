# Robot Factory Rumble — Phase 1

A side-scrolling run-and-gun proof-of-concept for the playground platform. Player is a small repair-bot infiltrating a malfunctioning factory; manually walks left/right, fires foam-bolt projectiles, dodges three enemy types (Wonky Walker, Cupcake Copter, Bouncing Bolt), picks up power-ups (Spark Spread, Shield Bubble, Bonus Heart), mounts a Fork-Lift Mech mid-level, and defeats the two-phase Foreman-Bot 9000 boss to clear the sector.

## Controls
- ◄ / ▶ buttons (or ←/→, A/D keys): walk left or right.
- ▲ button (or Space, ↑, W): jump. Hold longer for a higher jump. Hold ◄ or ▶ in mid-air for jump arc air control.
- ↑ button (or Shift): aim up — fires diagonally up-right or up-left in the direction the kid is facing.

## Difficulty
Single difficulty tuning ("kid-comfortable"). 5 hearts, 1.2s post-hit invuln, 80ms coyote-time on jumps, generous hitboxes (smaller than visible sprites).

## Phase 1 visual treatment
Procedural canvas drawing — flat colors with black outlines, similar to Baldi Basics. Phase 2 (separate spec) replaces all visuals with a sprite atlas via the game-assets skill, plus multi-frame animations and parallax.

## Kid-safety
- Bullets → foam bolts and spark sparks (toy-like)
- Enemies → robots that get K.O.'d with a bolt-burst (no death vocabulary)
- Tank → Fork-Lift Mech (industrial, not military)
- Boss roar → "Phase 2!" banner with screen flash (energetic, not frightening)
- UI copy stays positive ("Sector Cleared!", "Try again, you've got this!", "+1 Heart!")

## Out of scope (Phase 2 candidates)
Sprite atlas, multi-frame animation, parallax background, sound, persisted save, multi-level, difficulty selector.

---

# Phase 2 — Sprite Atlas + Animation (this branch)

This phase swaps every procedural rectangle from Phase 1 for sprites from a single 1024×1024 PNG atlas, and adds multi-frame animations for player, enemies, and boss. Gameplay tuning is identical to Phase 1 — only visuals change.

**Style:** Friendly industrial cartoon — chunky black outlines (3-4px), bright saturated primaries, slight chrome highlight on metal. Saturday-morning Wall-E meets Cars.

**Atlas:** `assets/robot-factory-rumble-atlas.png` (1024×1024 transparent, 5×4 grid of 192px cells, 19 sprites + 1 throwaway gear).

**Sprite map:** `sprite-map.json` is the source of truth for sprite coordinates. If gpt-image-2 produces a different grid than prompted, the JSON is updated to match — the code never assumes grid math.

**Hard-replace:** No procedural fallback. Loading splash blocks the game until atlas + sprite-map load.

**Boss Phase 2 sensor:** orange overlay drawn via canvas `globalCompositeOperation = 'lighter'` on top of the existing 4 boss sprites — not a separate sprite.

**Out of scope:** parallax, sound, save state, difficulty selector, second level (deferred to Phase C).

Full design at `docs/superpowers/specs/2026-05-04-robot-factory-rumble-phase2-design.md` (in platform repo, gitignored).
