#import libraries
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm		#get access to color maps

#define a nice plot
def image_plot(x,
	flag_save = True,
	xlabel = 'x',
	ylabel = 'y',
	dcmap = 'magma', 	#default color map
	fs = 12,
	fname = 'image_plot.png'):
	
	#define a figure and axis
	f, ax = plt.subplots(1,1,figsize=(4,4))
	#plot x vs y
	si = ax.imshow(x, cmap = dcmap, origin = 'lower')
	#label the axes
	ax.set_xlabel(xlabel, fontsize = fs)
	ax.set_ylabel(ylabel, fontsize = fs)
	#get a colorbar
	cbar = f.colorbar(si)
	cbar.ax.set_ylabel('z', fontsize = fs)
	#save the plot?
	if (flag_save):
		plt.savefig(fname,bbox_inches='tight',dpi=400)

#define main function
def main():
	print('making a plot')
	#make a dummy x variable
	x = np.linspace(0, np.pi, 400)
	y = np.linspace(0, 2*np.pi, 400)
	x,y = np.meshgrid(x,y)
	#make a function of x and y
	z = 3*np.cos(x)*np.sin(y)
	#make the plot
	image_plot(z)

#execute main()
if __name__ == "__main__":
	main()