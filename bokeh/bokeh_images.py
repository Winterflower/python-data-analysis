from __future__ import division
import numpy as np
from bokeh.plotting import figure, output_file, show, VBox
from numba import autojit


#######################################
#GENERATING A MANDELBROT IMAGE
#######################################
@autojit
def mandel(x,y,max_iters):

    #create a complex number
    c=complex(x,y)
    #what is this z? j or J is used to specify an imaginary number as a literal
    z=0.0j
    for i in range(max_iters):
        z=z*z+c
        if(z.real*z.real+z.imag*z.imag)>=4:
            #why are we returning i?
            return i
    return max_iters

###############################
#Create the fractal image
###############################
@autojit
def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height=image.shape[0]
    width=image.shape[1]

    pixel_size_x=(max_x-min_x)/width
    pixel_size_y=(max_y-min_y)/height

    for x in range(width):
        real=min_x+x*pixel_size_x
        for y in range(height):
            imag=min_y+y*pixel_size_y
            color=mandel(real,imag,iters)
            #what kind of object is image?
            image[y,x]=color



######################################################
#define the bounding coordinates of the Mandelbrot
#####################################################
min_x=-2.0
max_x=1.0
min_y=-1.0
max_y=1.0

################################
#Create an array using numpy
################################
img=np.zeros((1024,1536), dtype=np.uint8)
create_fractal(min_x, max_x, min_y, max_y, img, 20)


#######################################
#Create a static HTML output file
#######################################
output_file("bokeh_fractal.html")


p1=figure(title="Mandelbrot", plot_width=900, plot_height=600, x_range=[min_x,max_x], y_range=[min_y, max_y])

##############################################################
#Let's use the image renderer to display the Mandelbrot plot
##############################################################

p1.image(
    image=[img],
    x=[min_x],
    y=[min_y],
    dw=[max_x-min_x],
    dh=[max_y-min_y],
    palette="Spectral11"
)

show(p1)









