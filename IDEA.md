# plaster

A scriptable CLI to manage, rotate, and apply wallpapers on Linux.

## Problem

Wallpaper management is either manual or bloated with features nobody uses.
plaster keeps it simple: fetch wallpapers, organize them, rotate weekly, apply via swww.

## Core Workflow

```
plaster fetch --min-res 1920x1080 --category general
plaster rotate
plaster set <id>
plaster list
plaster remove <id>
```

## Folder Structure

```
~/.plaster/
  plaster.db          # SQLite - tracks all wallpapers, metadata, download history
  current/            # Active wallpaper pool (desktop points here)
  archive/            # Previous weeks / removed from rotation
```

## Commands

### `plaster fetch`
Pull wallpapers from Wallhaven API.
- `--min-res 1920x1080` — minimum resolution filter
- `--category general|anime|people` — Wallhaven categories
- `--count 10` — how many to fetch
- `--query "nature"` — search term
- Skips already-downloaded wallpapers (tracked in SQLite)

### `plaster rotate`
Move current/ → archive/, fill current/ with fresh wallpapers from the DB.
- `--count 7` — how many wallpapers in the new rotation
- Designed to run weekly via cron/systemd timer

### `plaster set [id]`
Apply a wallpaper immediately using swww.
- No argument = random from current/
- With ID = set a specific one

### `plaster list`
Show wallpapers in current rotation. Columns: id, resolution, category, source.
- `--archive` — show archived wallpapers instead
- `--all` — show everything

### `plaster remove <id>`
Remove a wallpaper. Deletes the file and marks it in the DB so it won't be re-fetched.

### `plaster init`
First-time setup. Creates ~/.plaster/, initializes the DB, optionally sets Wallhaven API key.

## Tech Stack

- **Python 3.10+**
- **Typer** — CLI framework
- **SQLite** (via stdlib sqlite3) — wallpaper tracking, metadata, blacklist
- **httpx** or **requests** — Wallhaven API calls
- **swww** — wallpaper application (Hyprland)
- **Rich** — pretty terminal output (familiar from noidea)

## API

Wallhaven API: https://wallhaven.cc/help/api
- Search endpoint with filters for resolution, categories, purity
- No API key needed for SFW content
- API key unlocks NSFW + favorites/collections

## SQLite Schema (rough)

```sql
wallpapers (
    id            TEXT PRIMARY KEY,   -- wallhaven ID
    path          TEXT,               -- local file path
    url           TEXT,               -- source URL
    resolution    TEXT,               -- "1920x1080"
    category      TEXT,               -- general/anime/people
    status        TEXT,               -- current / archived / removed
    fetched_at    TIMESTAMP,
    rotated_at    TIMESTAMP           -- last time it was in current/
)
```

## What's New (compared to noidea)

- SQLite — local database, schema design, queries
- HTTP APIs — fetching from Wallhaven, pagination, rate limits
- File management — downloading images, organizing directories
- Subprocess calls — invoking swww to set wallpapers

## Non-Goals (for now)

- GUI
- Multi-monitor support (keep it simple first)
- Multiple wallpaper sources (start with Wallhaven only)
- Auto-scheduling (user sets up cron themselves)
