#This programs writes out table of 
#the function sin(x) vs. x, where x 
#is tabulated between 0 and 2 with 1k entries.

#importing libraries
import numpy as np 
from astropy.table import Table
from astropy.io import ascii
from astropy.io import fits

#main function
def main():
	#writes out table of fn sin(x) vs x with 1k entries
	x = np.linspace(0, 2*np.pi, 1000)
	y = np.sin(x)
	data = Table([x, y], names = ['x', 'y'])
	ascii.write(data, 'table.txt', format = 'commented_header')
	data_in = ascii.read('table.txt')
	print(data_in)


#run the main function first
if __name__ == "__main__":
	main()
