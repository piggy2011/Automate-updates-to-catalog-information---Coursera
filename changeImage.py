#!/usr/bin/env python3

import os
from PIL import Image

# Directory path
img_dir = os.path.expanduser("~/supplier-data/images/")

# Iterate over all files in the directory
for filename in os.listdir(img_dir):
    if filename.lower().endswith(".tiff"):
        # Construct full file path
        tiff_path = os.path.join(img_dir, filename)
        
        # Open the image and convert to RGB (to remove alpha channel if present)
        with Image.open(tiff_path) as im:
            rgb_im = im.convert("RGB")
            # Resize the image to 600x400
            rgb_im = rgb_im.resize((600, 400))
            
            # Change the file extension to .jpeg
            jpeg_filename = os.path.splitext(filename)[0] + ".jpeg"
            jpeg_path = os.path.join(img_dir, jpeg_filename)
            
            # Save the image in JPEG format
            rgb_im.save(jpeg_path, "JPEG")

print("Conversion completed!")
