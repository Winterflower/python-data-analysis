import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import brewer

#make a list of categories
# let's make it something finance themes

securities=['equities', 'options', 'interest rate swaps']


N=10
#this language construct is a bit foreign to me. Is this a lambda expression?
data={cat: np.random.randint(10,100, size=N) for cat in securities}

print data
