from tiktokpy import TikTok
import requests
import os
import sys

def download_tiktok_video(url):
    try:
        # Initialize TikTok object
        tiktok = TikTok(url)

        # Get video URL
        video_url = tiktok.get_download_url()

        # Create directory if not exists
        if not os.path.exists("TikTok_videos"):
            os.makedirs("TikTok_videos")

        # Download the video
        with open(f"TikTok_videos/{tiktok.id}.mp4", "wb") as f:
            response = requests.get(video_url)
            f.write(response.content)

        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <TikTok_video_url>")
        sys.exit(1)
    
    video_url = sys.argv[1]
    download_tiktok_video(video_url)
