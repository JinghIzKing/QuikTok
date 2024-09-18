import os
import dropbox
import dropbox.files
import hashlib

# https://www.dropbox.com/oauth2/authorize?client_id=MY_CLIENT_ID&redirect_uri=MY_REDIRECT_URI&response_type=code

with open("DBTOKEN.txt", "r") as f:
    TOKEN = f.read()

dbx = dropbox.Dropbox(TOKEN)

def upload_local_files():
    for file in os.listdir("local_files"):
        with open(os.path.join("local_files", file), "rb") as f:
            data = f.read()
            dbx.files_upload(data, f"/{file}")


def download_cloud_files():
    for entry in dbx.files_list_folder("").entries:
        dbx.files_download_to_file(os.path.join("local_files", entry.name), f"/{entry.name}")

print(type(os.listdir("local_files")))