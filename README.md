# Topography-image-data-script

Uses a python image library to convert a pixel to RGB which is watched against an array to produce topography height data. 
This is written to a CSV in the following format.

| X      | Y | Height |
| ----------- | ----------- | ------ |
| -20 | -20 |  |
| ... | ... |  |
| 100 |100  |  |

The code is limited in it's use and only applicable for the RGB values of the specific image that I was working on. 

A much more advanced implementation that takes a generic topographic image like this one and converts it to a 3d terrain model can be found [here](https://github.com/georgelin-eng/topographic-map-to-3D-terrain-model-)
