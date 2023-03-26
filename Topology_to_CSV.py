from PIL import Image

im = Image.open ('topology.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())

