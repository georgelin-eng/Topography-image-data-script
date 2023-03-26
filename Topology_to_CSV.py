from PIL import Image

im = Image.open ('topology.png')
width, height = im.size

pgh_values = [[0] *3 for i in range (width * height)]


for x in range (width):
    for y in range (height):
        R,G,B, A = im.getpixel ((x,y))
        



