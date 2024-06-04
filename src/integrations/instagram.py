import subprocess
import os
import shutil
import re

class InstagramManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = Bot()

    # Uploads the post by logging into instagram
    def upload_post(self, image_name, caption):
        self.bot.login(username=self.username, password=self.password)
        self.bot.upload_photo(image_name, caption=caption)

    def login(self):
        self.bot.login(username=self.username, password=self.password)

    def fetch_pending_direct_messages(self):
        dm_list = self.bot.get_pending_direct()
        return dm_list

    def extract_links_from_messages(self, dm_list):
        links = []
        for dm in dm_list:
            message_text = dm['text']
            # Use regular expression to find links
            urls = re.findall(r'(https?://\S+)', message_text)
            links.extend(urls)
        return links

    def process_links(self, links):
        for link in links:
            print(link)
    
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


if __name__ == '__main__':
    # Testing code goes here

    image_name = "gigachad.jpg"
    #bot = InstagramBot(username="py_test_bot", password="X58k2vda6KMs")
    #folder_path = "E:\Clipbot\clipbot\config"  # Replace this with the path to the folder you want to remove
    #remover = FolderRemover()
    #remover.remove_folder(folder_path)
    #bot.upload_post(image_name, caption="Hello there")

