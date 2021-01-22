import os
from PIL import Image, ImageFilter, ImageOps

def watermark(im, mark, position):
    layer = Image.new("RGBA", im.size, (0,0,0,0))
    layer.paste(mark, position)
    return Image.composite(layer, im, layer)

files = os.listdir('img')

for file in files:
    if file.lower().endswith(".jpg"):
        
        im = Image.open("img/" + file)
        #im.thumbnail((60, 90), Image.ANTIALIAS)
        mark = Image.open("img/watermark.png")
        mark = mark.resize((50,50))
        mark.putalpha(128)
        
        out = watermark(im, mark, (0,0))        
        out.save("watermark/" + file, "JPEG")
