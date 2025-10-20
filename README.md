# 🎨 GitHub Contribution Pattern Maker

Automate your GitHub contribution graph to create beautiful custom patterns!

## How It Works

GitHub's contribution graph is a 52-week × 7-day grid. This script creates **backdated commits** on specific dates to "paint" patterns on your graph.

## Quick Start

1. **Edit the pattern** in `contribute.py` — choose a preset or draw your own
2. **Run the script**: `python3 contribute.py`
3. **Push to GitHub**: `git push origin main`
4. **Check your profile**: Visit [github.com/Itz-Mridul](https://github.com/Itz-Mridul)

## Available Patterns

| Pattern | Description |
|---------|-------------|
| `HEART` | ❤️ Heart shape |
| `STAR` | 🌟 Star shape |
| `ZIGZAG` | ⚡ Zigzag waves |
| `DIAGONAL` | 📊 Diagonal stripes |
| `HI` | 🔤 Writes "HI" |
| `MRIDUL` | 🔤 Writes "MRIDUL" |
| `WAVE` | 🌊 Sine wave |
| `MOUNTAIN` | 🏔️ Mountain peaks |

## Custom Patterns

Create your own pattern using the grid system:
```
'.' = empty (no commits)
'1' = light green  (1-3 commits)
'2' = medium green (4-6 commits)
'3' = dark green   (7-9 commits)
'4' = darkest green (10+ commits)
```

Each row = day of week (Sunday → Saturday)  
Each column = 1 week

## Settings

- `PATTERN` — Which pattern to draw
- `START_WEEKS_AGO` — Position on the graph (higher = further left)
- `COMMITS_PER_LEVEL` — Fine-tune commit counts per intensity
