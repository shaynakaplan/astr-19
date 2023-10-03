# This program will print the sum of 
#two floating point numbers, the difference 
#between two integers, and the product of a 
#floating point number and an integer, and print
#out the data type of each resulting answer.

#Assigning values to variables.
a = 1.2
b = 4.8
c = 5
d = 3

#This function adds two floating
#point numbers and prints out the sum
#and data type.
def adding():
	total = a + b
	print(total)
	print(type(total))

#This function subtracts two integers
#and prints out the difference
#and data type.
def subtracting():
	dif = c - d
	print(dif)
	print(type(dif))

#This function multiplies a floating
#point number and an integer and prints
#out the difference and data type.
def multiplying():
	prod = a * d
	print(prod)
	print(type(prod))

#This defines our main()
#for the program.
def main():
	adding()
	subtracting()
	multiplying()

#This executes first when we run
#the program.
if __name__=="__main__":
	main()