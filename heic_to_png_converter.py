from glob import glob
from PIL import Image
import pillow_heif


SOURCE_FOLDER_PATH = "/home/zeeshan/Downloads/source_folder_name"
DESTINATION_FOLDER_PATH = "/home/zeeshan/Downloads/destination_folder_name"


files_list = glob(f"{SOURCE_FOLDER_PATH}/*.HEIC") + glob(f"{SOURCE_FOLDER_PATH}/*.heic")

for file in files_list:
    file_name = file.replace(f"{SOURCE_FOLDER_PATH}/", "").split(".")[0]
    print(file_name)

    pillow_heif.register_heif_opener()
    image = Image.open(file)

    image.save(f"{DESTINATION_FOLDER_PATH}/{file_name}.png", format="png")
