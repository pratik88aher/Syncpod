# Syncpod

Syncpod is a YouTube audio downloader that extracts audio from any YouTube video or playlist and saves it as a high-quality MP3. It's built around two modes: a **web interface** powered by Flask, and a **terminal CLI** for quick command-line use.

Both modes use the same core download engine under the hood (`yt-dlp` + `ffmpeg`), so you get the same 192kbps MP3 output either way.

---

## Web UI

![Syncpod Web UI](assets/main_sc.png)

---

## How it works

Syncpod accepts a YouTube URL, downloads the best available audio stream, and converts it to MP3 using ffmpeg. Files are saved to `~/Desktop/IPOD_SONGS` by default, or to any path you specify.

---

## Two Modes

### Mode 1 — Web Interface (Flask)

Start Syncpod as a local web server. A simple browser UI lets you paste a URL and kick off a download with a button click. Good for one-off downloads when you don't want to type in a terminal.

**Start the server:**
```bash
syncpod --server
```

Or just run it with no arguments:
```bash
syncpod
```

Then open your browser to:
```
http://localhost:5000
```

Paste a YouTube URL into the input field, optionally set a custom save path, and hit Download. The page shows success or error feedback when the download completes.

---

### Mode 2 — Terminal (CLI)

Pass a YouTube URL directly as an argument. Syncpod downloads and converts in the terminal, then exits. Good for scripting, batch work, or when you just want something fast without opening a browser.

**Download a single video to the default folder (`~/Desktop/IPOD_SONGS`):**
```bash
syncpod "https://www.youtube.com/watch?v=9ZYjf3TC2LU"
```

**Download to a custom folder:**
```bash
syncpod "https://www.youtube.com/watch?v=9ZYjf3TC2LU" --path ~/Music
syncpod "https://www.youtube.com/watch?v=9ZYjf3TC2LU" -p ~/Music
```

**Download a full playlist:**
```bash
syncpod "https://www.youtube.com/playlist?list=RDEs4NrOnoNb4"
```

**Show all options:**
```bash
syncpod --help
```

---

## Installation

The `syncpod` command is installed globally via the `bin/` entry point. To set it up from scratch:

```bash
cd /Users/pratikaher/Syncpod
uv sync
brew install ffmpeg
```

---

## Requirements

- Python 3.9+
- ffmpeg (audio conversion)
- yt-dlp (YouTube extraction)
- Flask (web server mode)
