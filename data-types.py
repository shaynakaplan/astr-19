import numpy as np 		#import numpy library

#integers
i = 10				#integer
print(type(i))		#print out the data type of i

a_i = np.zeros(i, dtype = int)	#declare an array of ints
print(type(a_i))				#will return nd array
print(type(a_i[0]))				#will return int64

#floats
x = 19.10			#floating point number
print(type(x))		#print out the data type of x

y = 1.9e2			#floating 190 in scientific notation
print(type(y))		#print out the data type of x

z = np.zeros(i, dtype = float)	#declare array of floats
print(type(z))					#will return nd array
print(type(z[0]))				#will return float 64

#data types continued!!

#string
s = "I am a string."
print(type(s))			#will say str

#Boolean
yes = True			#Boolean True
print(type(yes))

no = False			#Boolean False
print(type(no))

#list – ordered and changeable
alpha_list = ["a", "b", "c"]	#list initialization
print(type(alpha_list))			#will say list
print(type(alpha_list[0]))		#will say string
alpha_list.append("d")			#will add "d" to list end
print(alpha_list)				#will print list

#tuple – ordered and unchangeable
alpha_tuple = ("a", "b", "c")	#tuple initialization
print(type(alpha_tuple))		#will say tuple

try:									#attept the following line
	alpha_tuple[2] = "d"				#won't work & will raise Type Error
except TypeError:						#when we get a TypeError
	print("We can't add elements to tuples!")	#print this message
print(alpha_tuple)