#this program defines a function f(x),
#which is equal to x**3 + 8.
#the function is called when x = 9
#and YAY! is printed if the result is
#larger than 27.

#this function defines f(x)
def f(x):
	return x**3 + 8


#main function
def main():
	x = 9
	f(x)
	print(f(x))
	if f(x) > 27:
		print("YAY!")

#run the main function first
if __name__ == "__main__":
	main()