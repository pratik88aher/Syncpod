# Syncpod - YouTube Audio Downloader

Download audio from YouTube videos and convert them to MP3 format.

## Features

- 🎵 Download audio from YouTube videos
- 🔄 Automatic MP3 conversion
- 🌐 Web interface for easy use
- 💻 Command-line interface for automation

## Installation

The `syncpod` command is already installed globally. You can use it from any terminal.

## Usage

### CLI Mode (Command Line)

**Download to default folder** (~/Desktop/IPOD_SONGS):
```bash
syncpod "https://www.youtube.com/watch?v=9ZYjf3TC2LU"
```

**Download to custom folder**:
```bash
syncpod "https://www.youtube.com/watch?v=9ZYjf3TC2LU" --path ~/Music
syncpod "https://www.youtube.com/watch?v=9ZYjf3TC2LU" -p ~/Music
```

**Show help**:
```bash
syncpod --help
```

### Web Server Mode

Start the web server:
```bash
syncpod --server
```

Or simply:
```bash
syncpod
```

Then open http://localhost:5000 in your browser.

## Examples

```bash
# Download a song
syncpod "https://www.youtube.com/watch?v=9ZYjf3TC2LU"

# Download to Music folder
syncpod "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --path ~/Music

# Download playlist (use playlist URL)
syncpod "https://www.youtube.com/playlist?list=RDEs4NrOnoNb4"
```

## Requirements

- Python 3.9+
- ffmpeg (for MP3 conversion)
- yt-dlp
- Flask

## Installation of Dependencies

```bash
cd /Users/pratikaher/Syncpod
uv sync
brew install ffmpeg
```
