# Imports
import yt_dlp
from pathlib import Path

def download(url, output_path):
    # Utilizes the ffmpeg for the mp3 compression
    # Defines the output path, independent of platform
    path = Path(output_path)
    file_template = str(path/"%(title)s.%(ext)s")

    # Defines the parameters of the download
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': file_template,
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Attempts to download from the URL passed
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get the resulting filename and pass to the window, without extension and directory
            info = ydl.extract_info(url, download=True)
            filename = Path(ydl.prepare_filename(info)).stem

            # Download the file and print success in terminal
            ydl.download([url])
            print(f"Successfully downloaded {url} \nFile: {filename} as mp3.")

            return filename
    except Exception as e:
        print(f"Error: {e}")
        return