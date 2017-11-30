#Adoption of Graphing Program to Plot 3-D Flight Path

# plot functions like y = sin(x) and y = cos(x) 
# with Tkinter canvas and line (visible), but can be saved only in .ps format 
# simultaneously use
# PIL image, draw, line (draws in memory, but can be saved in many formats)
# Python Image Library (PIL) free from:
# http://www.pythonware.com/products/pil/index.htm
# tested with Python24      vegaseat       15may2007

# use namespace to avoid conflict with PIL's Image
import Tkinter as tk
import math
import os
# needs Python Image Library (PIL)
import Image, ImageDraw
from PIL import Image
from PIL import ImageDraw
# some color constants for PIL
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0,128,0)
datasize = 1000

###########################################
#Import Pickled Flight Data Lists - px, py, pz
px = [0]*datasize
py = [0]*datasize
pz = [0]*datasize
###########################################

root = tk.Tk()
root.title("Simple plot using canvas and line")
datasize = 1000

dim_cosine = 0.866
dim_sine = 0.5

width = 400
height = 300
centerx = width//2
centery = height//2

x_increment = 1
y_increment = 1
# width stretch
x_factor = 0.04
# height stretch
size = 80

# Tkinter create a canvas to draw on
cv = tk.Canvas(width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# create the coordinate list for the sin() curve
# have to be integers for Tkinter
x_list = []
for t in range(400):
    # x coordinates
    x_list.append(t * x_increment)
    # y coordinates
    x_list.append(int(px[t]+dim_cosine*pz[t])*size + centerx)

y_list = []
for t in range(400):
    # x coordinates
    y_list.append(t * y_increment)
    # y coordinates
    y_list.append(-int(py[t]+dim_sine*pz[t])*size + centery)

# do the Tkinter canvas drawings (visible)
str1 = "2-D Projection of 3-D Aircraft Flight Path"
cv.create_text(10, 20, anchor='sw', text=str1)
center_line = cv.create_line([0, centery, width, centery], fill='green')

#Rewrite the following lines to generate points based on the data.
sin_line = cv.create_line(x_list, fill='blue')
cos_line = cv.create_line(y_list, fill='red')

# Tkinter canvas object can only be saved as a postscipt file
# which is actually a postscript printer language text file
cv.postscript(file="my_drawing.ps", colormode='color')

# do the PIL image/draw (in memory) drawings
draw.text((10, 20), str1, black)
draw.line([0, centery, width, centery], green)
draw.line(x_list, blue)
draw.line(y_list, red)

# PIL image can be saved as .png .jpg .gif or .bmp file
filename = "my_drawing.bmp"
image1.save("mydrawing.bmp")

# to test, view the saved file, works with Windows only
# behaves like double-clicking on the saved file


root.mainloop()
