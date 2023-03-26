# get image data
from PIL import Image
im = Image.open ('topology.png')
width, height = im.size

# file output settings
import csv
file = open('Topology.csv', 'w',newline='')
writer = csv.writer(file)
header = ['X', 'Y', 'pgh']
writer.writerow(header)

# iterate through topologyData to find the pgh value that corresponds to the R value of the x-y position
def match(R,G,B , topologyData):
    deviation = 0
    threshhold = 12 #allowable amount of deviation from exact RGB pixel value
    for i in range (13):
        deviation = abs(topologyData[i][0] - R) + abs(topologyData[i][1] - G) + abs(topologyData[i][2] - B)
        if deviation < threshhold:
            return topologyData [i][3]

# initialization of arrays
x_y_pgh = [0, 0 , 0]
pgh_previous = 0

#format         [ R,   G,   B,   pgh]
topologyData = [[209, 250, 254, -2.5],  [194, 241, 195, 0], 
                [176, 230, 119, 2.5],   [145, 204, 110, 5.0],
                [112, 180, 103, 7.5],   [79, 158, 95, 10.0], 
                [55, 139, 89, 12.5],    [49, 121, 73, 15.0],
                [64, 107, 53, 17.5],    [77, 95, 37, 20.0], 
                [90, 96, 36, 22.5],     [103, 98, 42, 25.0], 
                [115, 99, 47, 27.5],    [137, 101, 57, 30.0]] 

for x in range (0, width, 2):
    for y in range (0, height, 2):
            R,G,B, A = im.getpixel ((x,y))
            #conversion of x y pixel position to meters 
            y_pos  = -float(y)/2 + 100
            x_pos = float(x)/2 - 20

            x_y_pgh [0]= x_pos
            x_y_pgh [1]= y_pos
            x_y_pgh [2] = match (R,G,B, topologyData) 
            writer.writerow (x_y_pgh)
            
            # reduces error in pixel detection by setting NULL value to previous pgh values
            if x_y_pgh [2] != None:
                pgh_previous = x_y_pgh [2] 
            else:
                x_y_pgh [2]  = pgh_previous
file.close()


