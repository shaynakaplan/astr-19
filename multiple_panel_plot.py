#import libraries
import numpy as np 
import matplotlib.pyploy as plt

#define a nice plot
def multiple_panel_plot(x, y,
	flag_save = True,			#save the figure?
	xlabel = 'x',				#x-axis label
	ylabel = 'y',				#y-axis label
	lcolor = 'red',				#line color
	fs = 14,					#font size
	fname = 'multiple_panel_plot.png'):

	#by default, flag_save = True, and we'll save the
	#figure to a file. The plot filename fname = 'plot.png'
	#by default, but we can change this.

	#define a figure and axis
	nrow = 4
	ncolumn = 2
	f, ax = plt.subplots(nrow,ncolumn,figsize=(4*ncolumn, 4*nrow))
	#set each panel
	for i in range(nrow):
		for j in range(ncolumn):
			z = y + float(i)
			#plot y vs x
			#a line
			ax[i,j].plot(x,z,color=lcolor,linewidth=1.5,label='model(line)')
			#label our axes
			ax[i,j].set_xlabel(xlabel, fontsize = fs)
			ax[i,j].set_ylabel(ylabel, fontsize, fs)
	#fix the layour
	plt.tight_layout()
	#save the plot?
	if (flag_save):
		plt.savefig(fname, bbox_inches = 'tight', dpi=400)

#define main()
def main():
	print('Making a plot!')
	#make a dummy x variable
	x = np.linspace(0,1,10)
	#make a dummy y variable
	y = x**2
	#make the plot
	multiple_panel_plot(x, y)

#execute main()
if __name__ == "__main__":
	main()