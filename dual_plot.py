#import libraries
import numpy as np 
import matplotlib.pyplot as plt

#define a nice plot
def dual_plot(x, y, z,
	flag_save = True,			#save the figure?
	xlabel = 'x',				#x-axis label
	ylabel = 'y, z',			#y-axis label
	lcolor = 'red',				#line color
	pcolor = 'gold',			#point color
	fs = 14,					#font size
	fname = 'dual_plot.png'):	#default plot filename

	#by default, flag_save = True, and we'll save the
	#figure to a file. The plot filename fname = 'plot.png'
	#by default, but we can change this.

	#define a figure and axis
	f, ax = plt.subplots(1, 1, figsize = (4, 4))

	#plot y vs x
	#a line
	ax.plot(x, y, color = lcolor, linewidth = 1.5, label = 'y(line)')
	#circle
	ax.plot(x, z, 'o', color = pcolor, markersize = 3, label = 'z(points)')

	#label our axes
	ax.set_xlabel(xlabel, fontsize = fs)
	ax.set_ylabel(ylabel, fontsize = fs)

	#create a legend without a frame in upper left corner
	ax.legend(loc = 'upper left', frameon = False)

	#save the plot?
	if (flag_save):
		plt.savefig(fname, bbox_inches = 'tight', dpi = 400)

#define main
def main():
	print('Making a plot!')
	#make a dummy x variable
	x = np.linspace(0, 1, 10)
	#make a dummy y variable
	y = x**2
	#make a scond dependent variable
	z = x**1.5

#execute main()
if __name__ == "__main__":
	main()