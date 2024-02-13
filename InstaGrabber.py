from instabot import Bot
import re
import shutil
import Folder_Removal
from Folder_Removal import FolderRemover


class InstagramDM:
    def __init__(self, username, password):
        self.bot = Bot()
        self.username = username
        self.password = password

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


if __name__ == '__main__':
    instagram_bot = InstagramDM(username="insert username ", password="Insert password")
    folder_path = "E:\Clipbot\clipbot\config"  # Replace this with the path to the folder you want to remove
    remover = FolderRemover()
    remover.remove_folder(folder_path)
    instagram_bot.login()
    dm_list = instagram_bot.fetch_pending_direct_messages()
    links = instagram_bot.extract_links_from_messages(dm_list)
    instagram_bot.process_links(links)
