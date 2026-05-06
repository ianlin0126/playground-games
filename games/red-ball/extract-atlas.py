#!/usr/bin/env python3
"""Detect sprite bounding boxes in red-ball-atlas.png via alpha analysis."""
import json, sys, os
from pathlib import Path
try:
    from PIL import Image
except ImportError:
    print("install Pillow: pip3 install Pillow", file=sys.stderr); sys.exit(1)

ROW_SUM_THRESHOLD = 200
ALPHA_THRESHOLD = 16
MIN_SPRITE_DIM = 30

def detect(path):
    img = Image.open(path).convert("RGBA")
    W, H = img.size
    px = img.load()
    alpha = [[px[x, y][3] for x in range(W)] for y in range(H)]
    row_sum = [sum(alpha[y]) for y in range(H)]

    bands = []
    in_band = False
    y0 = 0
    for y in range(H):
        content = row_sum[y] > ROW_SUM_THRESHOLD
        if content and not in_band:
            in_band = True; y0 = y
        elif not content and in_band:
            in_band = False
            if y - y0 >= MIN_SPRITE_DIM: bands.append((y0, y))
    if in_band and H - y0 >= MIN_SPRITE_DIM: bands.append((y0, H))

    sprites = []
    for row_idx, (yb0, yb1) in enumerate(bands):
        col_content = [any(alpha[y][x] > ALPHA_THRESHOLD for y in range(yb0, yb1)) for x in range(W)]
        runs = []
        in_run = False; x0 = 0
        for x in range(W):
            if col_content[x] and not in_run:
                in_run = True; x0 = x
            elif not col_content[x] and in_run:
                in_run = False
                if x - x0 >= MIN_SPRITE_DIM: runs.append((x0, x))
        if in_run and W - x0 >= MIN_SPRITE_DIM: runs.append((x0, W))
        for x0, x1 in runs:
            ty0 = yb0; ty1 = yb1
            for y in range(yb0, yb1):
                if any(alpha[y][x] > ALPHA_THRESHOLD for x in range(x0, x1)): ty0 = y; break
            for y in range(yb1 - 1, yb0 - 1, -1):
                if any(alpha[y][x] > ALPHA_THRESHOLD for x in range(x0, x1)): ty1 = y + 1; break
            sprites.append({"x": x0, "y": ty0, "w": x1 - x0, "h": ty1 - ty0, "row": row_idx})
    return sprites, (W, H)

def crop_all(path, sprites, out_dir):
    img = Image.open(path).convert("RGBA")
    os.makedirs(out_dir, exist_ok=True)
    for i, s in enumerate(sprites):
        crop = img.crop((s["x"], s["y"], s["x"] + s["w"], s["y"] + s["h"]))
        crop.save(os.path.join(out_dir, f"sprite_{i:02d}_r{s['row']}.png"))

if __name__ == "__main__":
    here = Path(__file__).parent
    atlas = here / "assets" / "red-ball-atlas.png"
    sprites, (W, H) = detect(atlas)
    print(f"atlas {W}x{H}: detected {len(sprites)} sprites")
    for i, s in enumerate(sprites):
        print(f"  [{i:02d}] r{s['row']}  x={s['x']:4d} y={s['y']:4d}  w={s['w']:4d} h={s['h']:4d}")
    crop_all(atlas, sprites, here / "crops")
    (here / "sprite-bboxes.json").write_text(json.dumps(sprites, indent=2))
