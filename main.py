import yt_dlp
import time
from flask import Flask, render_template, request, jsonify
import os
from pathlib import Path
import sys
import argparse

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024  # 16GB max

def download_best_audio(url, download_path=None, max_retries=3):
    """Download audio from URL and convert to MP3"""
    
    # Determine the download folder
    if download_path:
        # Use the provided path
        ipod_folder = os.path.expanduser(download_path)
    else:
        # Use default IPOD_SONGS folder
        ipod_folder = os.path.expanduser('/Users/pratikaher/Desktop/IPOD_SONGS')
    
    # Create folder if it doesn't exist
    os.makedirs(ipod_folder, exist_ok=True)
    
    for attempt in range(max_retries):
        try:
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                    'Referer': 'https://www.youtube.com/',
                    'Accept-Language': 'en-US,en;q=0.9',
                },
                'quiet': False,
                'no_warnings': False,
                'socket_timeout': 60,
                'retries': 10,
                'skip_unavailable_fragments': True,
                'extractor_args': {
                    'youtube': {
                        'player_client': ['web_embedded', 'web', 'android', 'tv'],
                        'player_skip_js_prefetch': True,
                    }
                },
                'outtmpl': os.path.join(ipod_folder, '%(title)s.%(ext)s'),
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            location_text = download_path if download_path else "IPOD_SONGS folder"
            return True, f"✓ Download successful! MP3 file saved to {location_text}."
        except Exception as e:
            error_str = str(e)
            if attempt < max_retries - 1:
                wait_time = 5 * (attempt + 1)
                error_msg = f"Attempt {attempt + 1} failed. Retrying in {wait_time} seconds..."
                time.sleep(wait_time)
            else:
                error_msg = f"Failed after {max_retries} attempts. The video may not be downloadable or YouTube is blocking the request."
                return False, error_msg
    return False, "Unknown error occurred"

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    """Handle download request"""
    try:
        data = request.json
        url = data.get('url', '').strip()
        download_path = data.get('download_path', '').strip() or None
        
        # For YouTube URLs, keep only the watch?v=... part
        if 'youtube.com' in url and 'watch?v=' in url:
            base_url = url.split('watch?v=')[0]
            video_id = url.split('watch?v=')[1].split('&')[0]
            url = f"{base_url}watch?v={video_id}"
        
        if not url:
            return jsonify({'success': False, 'error': 'Please enter a URL'}), 400
        
        success, message = download_best_audio(url, download_path)
        
        if success:
            return jsonify({'success': True, 'message': message}), 200
        else:
            return jsonify({'success': False, 'error': message}), 400
    
    except Exception as e:
        return jsonify({'success': False, 'error': f"Error: {str(e)}"}), 500

def main():
    """Main entry point that supports both CLI and web server modes"""
    parser = argparse.ArgumentParser(
        description='Syncpod - Download audio from YouTube videos'
    )
    parser.add_argument(
        'url',
        nargs='?',
        default=None,
        help='YouTube URL to download'
    )
    parser.add_argument(
        '-p', '--path',
        default=None,
        help='Download path (default: ~/Desktop/IPOD_SONGS)'
    )
    parser.add_argument(
        '--server',
        action='store_true',
        help='Run as web server (default behavior if no URL provided)'
    )
    
    args = parser.parse_args()
    
    # If URL is provided, run in CLI mode
    if args.url:
        print(f"🎵 Downloading from: {args.url}")
        success, message = download_best_audio(args.url, args.path)
        print(message)
        sys.exit(0 if success else 1)
    
    # Otherwise run web server
    print("Starting Syncpod web server on http://127.0.0.1:5000")
    app.run(debug=True, host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()