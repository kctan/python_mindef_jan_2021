import os
from PIL import Image, ImageFilter, ImageOps

files = os.listdir('img')
#size = 60, 90

for file in files:
    if file.lower().endswith(".jpg"):
        im = Image.open("img/" + file)
        width, height = im.size 
        half_width = int(width*0.5)
        half_height = int(height*0.5)
        
        im.thumbnail((half_width, half_height), Image.ANTIALIAS)
        im.save("resized/" + file, "JPEG")

