#!/usr/bin/env python3
import yt_dlp
import sys

url = "https://www.youtube.com/watch?v=-YlmnPh-6rE"
print(f"Testing download of: {url}")
ydl_opts = {
    'format': 'best[ext=m4a]/best[ext=mp3]/best',
    'quiet': True,
    'outtmpl': '%(title)s.%(ext)s',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Starting download...")
        info = ydl.extract_info(url, download=False)  # Extract info first without downloading
        print(f"✓ Info extracted: {info.get('title')}")
        print(f"Available formats: {len(info.get('formats', []))}")
except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
    sys.exit(1)
