import os
from tkinter import Tk, filedialog
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Set up your OAuth 2.0 credentials
CLIENT_SECRETS_FILE = "path_to_your_client_secrets.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


# Authenticate and create the service
def get_authenticated_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)


# Upload a video
def upload_video(service, video_file, title, description, category, tags):
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)

    request = service.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    response = request.execute()
    print(f"Video uploaded successfully: https://www.youtube.com/watch?v={response['id']}")


# Select a video file
def select_video_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    video_file = filedialog.askopenfilename(title="Select a Video File",
                                            filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
    return video_file


if __name__ == "__main__":
    # Set video metadata
    TITLE = "Your Video Title #Shorts"
    DESCRIPTION = "Your Video Description #Shorts"
    CATEGORY = "22"  # '22' is the category ID for 'People & Blogs'
    TAGS = ["shorts", "tag1", "tag2"]

    # Step 1: Select the video file
    video_file = select_video_file()
    if not video_file:
        print("No video file selected.")
        exit()

    print(f"Video selected: {video_file}")

    # Step 2: Authenticate and upload the video
    service = get_authenticated_service()
    upload_video(service, video_file, TITLE, DESCRIPTION, CATEGORY, TAGS)
