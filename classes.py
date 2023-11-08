#define a class with an initialize
#set of parameters

#import sys
import sys

class Shape:
	#a class for geometric shapes
	def print(self):
		print("Here is our shape!")
		print(f'Number of sides = {self.num_sides}')
		print(f'Lenght of sides = {self.side_length}')

	def __init__(self,nsides = 3, length = 1.):
		self.num_sides = nsides
		self.side_length = length

def main():
	#set default number of sides and length
	nsides = 3
	length = 10.
	# if there are at least 2 command line
	#arguments, set nsides equal to the second
	if (len(sys.argv)>=2):
		nsides = int(sys.argv[1])
	#if there are 3 command line arguments,
	#set length equal to the third
	if (len(sys.argv)>=3):
		length = float(sys.argv[2])
	#intiialize our shape
	our_shape = Shape(nsides = nsides, length = length)
	#print out info about our shape
	our_shape.print()

#run the program
if __name__ == "__main__":
	main()