from instabot import Bot
import os
import shutil
import Folder_Removal
from Folder_Removal import FolderRemover

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = Bot()

    # Uploads the post by logging into instagram
    def upload_post(self, image_name, caption):
        self.bot.login(username=self.username, password=self.password)
        self.bot.upload_photo(image_name, caption=caption)


# Test input
if __name__ == '__main__':
    # enter name of your image below
    image_name = "gigachad.jpg"
    bot = InstagramBot(username="Insert username here", password="Insert password here")
    folder_path = "E:\Clipbot\clipbot\config"  # Replace this with the path to the folder you want to remove
    remover = FolderRemover()
    remover.remove_folder(folder_path)
    bot.upload_post(image_name, caption="Hello there")



