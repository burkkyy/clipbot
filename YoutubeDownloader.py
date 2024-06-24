from pytube import YouTube

class YTMP4Downloader:
    def __init__(self):
        pass

    def download_video(self, url, output_path='./'):
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
            if stream:
                print(f'Downloading: {yt.title}...')
                stream.download(output_path)
                print('Download completed successfully.')
            else:
                print('No MP4 video available for download.')
        except Exception as e:
            print(f'Error: {str(e)}')

if __name__ == "__main__":
    downloader = YTMP4Downloader()
    url = input("Enter the URL of the video you want to download: ")
    output_path = input("Enter the path where you want to save the video (leave blank for current directory): ").strip()
    if output_path == '':
        output_path = './'
    downloader.download_video(url, output_path)

