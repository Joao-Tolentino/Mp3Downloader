# Mp3Downloader

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](LICENSE)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-0078D6.svg?logo=windows&logoColor=white)](#)

A fast, GUI-driven Python utility that pulls high-quality audio streams from YouTube (and other supported URLs) directly to your hard drive as formatted `.mp3` files using the powerful `yt_dlp` library.

---

## Features

- **yt_dlp Integration**: Replaces deprecated youtube-dl wrappers to reliably extract audio stream URLs bypassing modern throttling.
- **Automated FFmpeg Processing**: Seamlessly downloads the best available audio and automatically invokes an `FFmpegExtractAudio` post-processor to compress it to a crisp 192kbps MP3.
- **Tkinter Interface**: Offers a simple `tk.Entry` box for your URL and a native directory picker to define your output destination instantly.

---

## Quick Start

1. Clone or download the repository.
2. Ensure Python 3 is installed.
3. **CRITICAL**: Ensure the `ffmpeg` executable is installed and configured in your system PATH!
4. Install pip dependencies: `pip install yt-dlp`
5. Run the application: `python main.py`

---

## Configuration Details

No API keys are required. The script explicitly passes an `outtmpl` string directly to `yt_dlp` formatted as `%(title)s.%(ext)s` to ensure downloaded files are named elegantly based on the source video title.

---

## Usage Guidelines

- Run the application.
- Paste a URL (e.g., a YouTube video link) into the top text entry field.
- Click **Select Folder** and choose where the audio file should be saved.
- Click **Download**. The interface will pause while `yt_dlp` runs the fetch and ffmpeg conversion in the background. A success window will alert you when your `.mp3` is ready.

---

## Technical Documentation

For developers interested in directory structures, code architecture, or compilation guidelines, please refer to the **[Documentation.md](Documentation.md)** file.

---

## License

This project is licensed under the **GNU Affero General Public License Version 3 (AGPLv3)**. See the LICENSE file for details.
