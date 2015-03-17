from __future__ import division
__author__ = 'winterflower'
###########################################
#Bokeh tutorial on scatter point plots
##########################################


import numpy as np
from bokeh.plotting import figure, show, output_file, VBox, HBox
from bokeh.models import Range1d

######################################
#CREATE DATA
######################################
#1. Create data with Python lists
x1=range(10)
y1=range(0,20,2)

#2. Create data using numpy arrays
x2=np.random.random_sample(10)
y2=np.random.random_sample(10)

#3. Create some data
x3=np.random.randn(10)
y3=np.random.randn(10)


##########################################
#Write the output to a static html file
#########################################

output_file("bokeh_scatter.html")


####################################
TOOLS="pan, wheel_zoom, box_zoom, reset, save"

############################
#CREATE two range1d objects to reuse in the plots
##################################################

range1=Range1d(start=-10, end=10)
range2=Range1d(start=-10, end=10)

################################
#Create figures for the data
#################################

p1=figure(y_range=range1, x_range=range2, tools=TOOLS, plot_width=300, plot_height=300)
p1.scatter(x1,y1, size=12, color="blue", marker="triangle", alpha=0.5 )


p2=figure(y_range=range1, x_range=range2, tools=TOOLS, plot_width=200, plot_height=200)
p2.scatter(x2,y2, size=6, color="pink", marker="circle", alpha=0.8)

p3=figure(y_range=range1, x_range=range2, tools=TOOLS,plot_width=200, plot_height=300)
p3.scatter(x3,y3, size=8, color="purple", marker="circle", alpha=0.5)


show(HBox(p1,p2,p3))

