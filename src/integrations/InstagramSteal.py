import instaloader
import os
import sys

def download_instagram_video(url):
    try:
        # Create instance of Instaloader class
        loader = instaloader.Instaloader()

        # Login (optional)
        # loader.interactive_login("your_username")

        # Get post details
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])

        # Create directory if not exists
        if not os.path.exists("Instagram_videos"):
            os.makedirs("Instagram_videos")

        # Download the video
        loader.download_post(post, target="Instagram_videos")

        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <Instagram_post_url>")
        sys.exit(1)
    
    post_url = sys.argv[1]
    download_instagram_video(post_url)
