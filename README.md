# YouTube to MP3 Downloader - Complete Setup Guide

## Download & Setup (Follow in Order)

1. INSTALL PYTHON
   - Go to https://www.python.org/downloads/
   - Download Python 3.12 or newer
   - Run installer
   - ✅ CHECK "Add Python to PATH" box (Important!)
   - Click "Install Now"

2. INSTALL REQUIRED PACKAGES
   - Press Windows + R
   - Type "cmd" and press Enter
   - Copy/paste these commands:
     pip install yt-dlp
     pip install moviepy

3. INSTALL FFMPEG
   - Download from: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
   - Extract the zip file
   - Create folder: C:\ffmpeg
   - Go to extracted folder → bin folder
   - Copy these 3 files to C:\ffmpeg:
     * ffmpeg.exe
     * ffplay.exe
     * ffprobe.exe

4. GET THE SCRIPT
   - Save MP3.py to your computer
   - Double-click to run
   - If it opens in text editor:
     * Right-click → Open with → Python

## How to Use
1. Run MP3.py
2. Choose option:
   - 1 = Single song
   - 2 = Playlist
   - 3 = Exit
3. Select save location
4. Paste YouTube link
5. Wait for download

## Troubleshooting
If you get errors:
- "python not found" = Reinstall Python, check "Add to PATH"
- "yt-dlp not found" = Run: pip install yt-dlp
- "FFmpeg not found" = Check files in C:\ffmpeg
- Still not working? Run these in cmd:
  * python --version
  * pip --version
  If no version shows, reinstall Python

That's it! You can now download YouTube videos as MP3s! 🎵
