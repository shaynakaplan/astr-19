#define a function
def flow_control(k):
	#define a string based on the value of k
	if (k == 0):
		s = "Variable k = %d equals 0. " % k
				# %d prints out an integer 
	elif (k == 1):
		s = "Variable k = %d equals 1. " % k
	else:
		s = "Variable k = %d does not equal 0 or 1. " % k
	#print the variable
	print(s)

#define a main function
def main():
	#declare an integer
	i = 0
	#try flow control for 0, 1, 2
	flow_control(i)
	i = 1
	flow_control(i)
	i = 2
	flow_control (i)

#run the program
if __name__ == "__main__":
	main()