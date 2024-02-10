import subprocess
import instaloader
import re


class InstaScraper:
    def __init__(self):
        self.input_url = "https://www.instagram.com/reel/CnD1B3XjGyN/?utm_source=ig_web_copy_link"

    def download(self, url):
        # Extract mp4:
        trimmed_url = self.trim_url(url)
        directory_pattern = "E:\Reels"
        command = ["python", "-m", "instaloader", "--", "--dirname-pattern", directory_pattern, trimmed_url]

        # Run the command
        subprocess.run(command)

    def trim_url(self, url):
        # Define the start and end strings
        start_string = "/reel/"
        end_string = "/?"

        # Define the pattern using regular expression
        pattern = r'%s(.*?)%s' % (re.escape(start_string), re.escape(end_string))

        # Search for the pattern in the input string
        match = re.search(pattern, url)

        # If match found, extract the text between the start and end strings
        if match:
            text_between_strings = match.group(1)
            print("-" + text_between_strings)
            return "-" + text_between_strings
        else:
            print("Start or end strings not found.")
            return ""
