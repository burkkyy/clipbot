'''
@file util/fileio.py
@author Josh Campinile
@date 2024-02-15

Miscellaneous helper functions
'''

import shutil

def remove_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' successfully removed.")
    except OSError as e:
        print(f"Error: {e.filename} - {e.strerror}.")

