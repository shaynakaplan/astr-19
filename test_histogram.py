#import libraries
import numpy as np 
import matplotlib.pyplot as plt

#define a nice plt
def histogram_plot(x,
	flag_save = True,
	xlabel = 'x',
	yllabel = 'y',
	lcolor = 'red',
	fs = 14,
	fname = 'histogram_plot.png'):
	
	#define a figure and axis
	f, ax = plt.subplots(1, 1, figsize = (4, 4))
	#plot y vs x
	ax.hist(x,facecolor=lcolor,bins=50,edgecolor='black',alpha=0.5)
	#label our axes
	ax.set_xlabel(xlabel, fontsize = fs)
	ax.set_ylabel(ylabel, fontsize = fs)
	#save the plot?
	if (flag_save):
		plt.savefig(fname, bbox_inches='tight', dpi=400)

#define main
def main():
	print('Making a plot!')
	#make a dummy x variable
	x = np.random.normal(scale=1, size=1000)
	#make the plot
	histogram_plot(x)

#execut main()
if __name__ == "__main__":
	main()