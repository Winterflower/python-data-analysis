__author__ = 'winterflower'
from bokeh.plotting import HBox,output_file, figure, show, VBox
#what do these imported elements do?
#figure= the main canvas on which Bokeh draws
#show=function used to show the Bokeh figure
from bokeh.models import Range1d
#what is Range1d needed for?

#############################
#CREATING SAMPLE DATASETS
#############################
import numpy as np

x1=range(10)
y1=np.random.random_sample(10)

#Exercise: Create two more data sets

x2=range(0,20,2)
y2=np.random.random_sample(10)

x3=range(10)
y3=np.random.random_sample(10)

###################################
#Set the Bokeh output html file
##################################

output_file("bokeh_scatter.html")


########################################
#PLOT EACH DATA SET IN ITS OWN FIGURE
########################################

p1=figure(plot_height=300, plot_width=300)
p1.line(x1,y1,size=12,color="red", alpha=0.5)

p2=figure(plot_height=300, plot_width=300)
p2.line(x2,y2,size=6, color="blue", alpha=0.8)

p3=figure(plot_height=300, plot_width=300)
p3.line(x3,y3, size=18, color="red", alpha=0.2)

###############################################
#Create a fourth plot and make all lines appear in one plot
##############################################

#NOTE: the below solution is incorrect
"""
p4=figure(plot_height=400, plot_width=400)
p4.line(x1+x2+x3, y1+y2+y3, color="green", alpha=0.4)
"""

p4=figure()
p4.line(x1,y1,size=12,color="red", alpha=0.5)
p4.line(x2,y2,size=10, color="blue", alpha=0.4)
p4.line(x3,y3,size=8, color="green", alpha=0.8)


show(VBox(HBox(p1,p2,p3),p4))