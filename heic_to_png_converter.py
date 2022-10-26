"""
    This code will convert the heic to png and then save the image.
"""
from glob import glob
from PIL import Image
import pillow_heif


# Set the path of your folder here
SOURCE_FOLDER_PATH = ""
DESTINATION_FOLDER_PATH = ""


files_list = glob(f"{SOURCE_FOLDER_PATH}/*.HEIC") + glob(f"{SOURCE_FOLDER_PATH}/*.heic")

for file in files_list:
    file_name = file.replace(f"{SOURCE_FOLDER_PATH}/", "").split(".")[0]

    pillow_heif.register_heif_opener()
    image = Image.open(file)

    image.save(f"{DESTINATION_FOLDER_PATH}/{file_name}.png", format="png")
