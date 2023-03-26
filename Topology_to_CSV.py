# get image data
from PIL import Image
im = Image.open ('topology.png')
width, height = im.size

# iterate through topologyData to find the pgh value that corresponds to the R value of the x-y position
def match(R, topologyData):
    for i in range (9):
        if R == topologyData[i][0]:
            return topologyData [i][3]


# initialization of arrays
x_y_pgh = [[0] *3 for i in range (width)]
topologyData = [[209, 250, 254, -2.5], #format [R,G,B, pgh]
                [194, 241, 195, 0],
                [176, 230, 119, 2.5],
                [145, 204, 110, 5.0],
                [112, 180, 103, 7.5],
                [79, 158, 95, 10.0], 
                [55, 139, 89, 12.5],
                [49, 121, 73, 15.0],
                [64, 107, 53, 17.5],
                [77, 95, 37, 20.0]] 

for x in range (width):
    for y in range (height):
        R,G,B, A = im.getpixel ((x,y))
        #conversion of x y pixel position to meters 
        y_pos  = -float(y)/2 + 100
        x_pos = float(x)/2.3 - 20

        x_y_pgh [x][0] = round(x_pos, 0)
        x_y_pgh [x][1] = y_pos
        pgh = match (R, topologyData) 
        x_y_pgh [x][2] = pgh

