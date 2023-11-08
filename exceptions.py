#python exceptions let you deal with
#unexpected results

try:
	print(a)	#this throws an exception since a isn't defined
except:
	print("a is not defined.")

#there are specific errors to help with cases
try:
	print(a)	#this throws an exception since a isn't defined
except NameError:
	print("a is still not defined.")
except:
	print("something else went wrong.")

#this will break our program since a is
#not defined
print(a)