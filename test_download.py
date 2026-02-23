import yt_dlp

url = "https://www.youtube.com/watch?v=-YlmnPh-6rE"

ydl_opts = {
    'format': 'best[ext=m4a]/best[ext=mp3]/best',
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Referer': 'https://www.youtube.com/',
    },
    'socket_timeout': 60,
    'outtmpl': '%(title)s.%(ext)s',
    'quiet': False,
}

print(f"Downloading from: {url}")
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.download([url])
    print("✓ Download complete!")
except Exception as e:
    print(f"✗ Error: {e}")
