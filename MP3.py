import sys



import os







# Add FFmpeg to PATH if it exists in C:\ffmpeg



ffmpeg_path = "C:\\ffmpeg"



if os.path.exists(ffmpeg_path):



    os.environ["PATH"] = os.environ["PATH"] + ";" + ffmpeg_path







# Print Python information



print("\n=== Python System Information ===")



print(f"Python Version: {sys.version}")



print(f"Python Location: {sys.executable}")



print(f"FFmpeg Path: {ffmpeg_path}")



print("================================\n")







# Check if FFmpeg exists



if not os.path.exists(os.path.join(ffmpeg_path, "ffmpeg.exe")):



    print("ERROR: FFmpeg not found!")



    print(f"Please put ffmpeg.exe, ffplay.exe, and ffprobe.exe in: {ffmpeg_path}")



    print("You can download FFmpeg from: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")



    input("Press Enter to exit...")



    sys.exit(1)







try:



    import yt_dlp



except ImportError:



    print("Error: yt-dlp is not installed. Please install it using:")



    print("pip install yt-dlp")



    sys.exit(1)







import re



import tkinter as tk



from tkinter import filedialog, messagebox



import time







def sanitize_filename(title):



    """Remove invalid characters from filename"""



    return re.sub(r'[<>:"/\\|?*]', '', title)







def select_output_directory():



    """Open dialog to select output directory"""



    root = tk.Tk()



    root.withdraw()



    folder_path = filedialog.askdirectory(title="Select where to save MP3s (e.g., USB drive)")



    return folder_path if folder_path else "downloads"







def check_url_safety(url):



    """Verify URL is from YouTube"""



    if not url.startswith(('https://www.youtube.com/', 'https://youtu.be/')):



        print("Error: Only YouTube URLs are allowed")



        return False



    return True







def download_audio(url, output_dir):



    """Download single video as MP3"""



    try:



        if not os.path.exists(output_dir):



            os.makedirs(output_dir)







        ydl_opts = {



            'format': 'bestaudio/best',



            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),



            'postprocessors': [{



                'key': 'FFmpegExtractAudio',



                'preferredcodec': 'mp3',



                'preferredquality': '192',



            }],



            'quiet': True,



            'no_warnings': True



        }







        with yt_dlp.YoutubeDL(ydl_opts) as ydl:



            print("\nGetting video information...")



            info = ydl.extract_info(url, download=False)



            if info is None:



                print("⚠️ Skipping unavailable video...")



                return False



                



            title = info.get('title', 'video')



            print(f"Downloading: {title}")



            ydl.download([url])



            print(f"✓ Successfully downloaded: {title}")



            return True







    except Exception as e:



        if "Private video" in str(e):



            print("⚠️ Skipping private video...")



        elif "Video unavailable" in str(e):



            print("⚠️ Skipping unavailable video...")



        else:



            print(f"⚠️ Skipping video due to error: {str(e)}")



        return False







def download_playlist(playlist_url, output_dir):



    """Download all videos from a playlist as MP3"""



    try:



        ydl_opts = {



            'quiet': True,



            'no_warnings': True,



            'extract_flat': True,



        }







        with yt_dlp.YoutubeDL(ydl_opts) as ydl:



            print("\nGetting playlist information...")



            result = ydl.extract_info(playlist_url, download=False)



            



            if 'entries' not in result:



                print("Error: Could not find any videos in playlist")



                return







            total_videos = len(result['entries'])



            print(f"\nDownloading playlist: {result.get('title', 'Unknown Playlist')}")



            print(f"Number of songs in playlist: {total_videos}")



            print("This might take a while...\n")







            successful = 0



            failed = 0







            for i, entry in enumerate(result['entries'], 1):



                if entry:



                    print(f"\nDownloading song {i} of {total_videos}")



                    video_url = entry['url']



                    if check_url_safety(video_url) and download_audio(video_url, output_dir):



                        successful += 1



                    else:



                        failed += 1







            print(f"\nDownload complete!")



            print(f"Successfully downloaded: {successful} songs")



            print(f"Failed to download: {failed} songs")







    except Exception as e:



        print(f"Error processing playlist: {str(e)}")







def main():



    print("\n=== YouTube to MP3 Downloader ===")



    print("This program will help you download music from YouTube to your computer or USB drive.")



    



    while True:



        print("\nWhat would you like to do?")



        print("1. Download a single song")



        print("2. Download entire playlist")



        print("3. Exit")



        



        choice = input("\nType a number (1-3) and press Enter: ")



        



        if choice == "1" or choice == "2":



            output_dir = select_output_directory()



            if not output_dir:



                continue



                



            if choice == "1":



                print("\nTo download a song, copy-paste the YouTube video link below.")



                url = input("YouTube link: ").strip()



                download_audio(url, output_dir)



            else:



                print("\nTo download a playlist, copy-paste the YouTube playlist link below.")



                url = input("YouTube playlist link: ").strip()



                download_playlist(url, output_dir)



                



            input("\nPress Enter to continue...")



            



        elif choice == "3":



            print("\nThank you for using YouTube to MP3 Downloader!")



            print("Goodbye!")



            break



        else:



            print("\nPlease choose 1, 2, or 3")







if __name__ == "__main__":



    main()














