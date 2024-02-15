import shutil

class FolderRemover:
    def remove_folder(self, folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' successfully removed.")
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}.")

if __name__ == "__main__":
    folder_path = "E:\Clipbot\clipbot\config"  # Replace this with the path to the folder you want to remove
    remover = FolderRemover()
    remover.remove_folder(folder_path)