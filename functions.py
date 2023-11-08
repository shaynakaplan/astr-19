import numpy as np
import sys			#gives access to operating system

#define a function that returns a value
def expo(x):
	return np.exp(x)	#return the np e^x function

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))	#call the expo function

#define the main function
def main():
	n = 10 		#provide a default value for n
	#check if there is a command line argument provided
	if (len(sys.argv)>1):
		n = int(sys.argv[1])	#if an argument was provided
	show_expo(n) 	#call the show_expo subroutine

#run the main fuction
if __name__ == "__main__":
	main()