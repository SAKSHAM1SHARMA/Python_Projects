import yt_dlp

def download_youtube_video(url, output_path="."):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',  # Best quality
        'merge_output_format': 'mp4',
        'noplaylist': True,  # Only download single video
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    path = input("Enter output path (press Enter for current directory): ").strip()
    if not path:
        path = "."
    download_youtube_video(video_url, path)
