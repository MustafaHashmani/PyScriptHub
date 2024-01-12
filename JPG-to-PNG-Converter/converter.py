import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists and if it does not then create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through folder and convert images to PNG
for file in os.listdir(image_folder):
    image = Image.open(f"{image_folder}{file}")
    filename = os.path.splitext(file)[0]
    # save to the new folder
    image.save(f"{output_folder}{filename}.png", "png")
