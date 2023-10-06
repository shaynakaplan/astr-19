import numpy as np

def main():
	i = 1			#integers an be declared with a number
	n = 10          #another integer
	x = 19.0        #floating point numbers are declared with a '.'

	#numpy can be used to quicklyy delcare arrays
	y = np.zeros(n, dtype = float) #declares 10 zeros as floats using np

	#use for loops to iterate with a variable
	for i in range (n):		#i in range [0, n-1]
		y[i] = 2.0 * float(i) + 1  		#set y = 2i + 1 as floats

	#simply iterate through a variable
	for y_element in y:
		print(y_element)

#execute the main function
if __name__ == "__main__":
	main()