x = [0.0, 3.0, 5.0, 2.5, 3.7]	#defines a list
print(type(x))

#remove the third element
x.pop(2)
print("x.pop(2)? ", x)

#remove the element equal to 2.5
x.remove(2.5)
print("x.remove(2.5)? ", x)

#add an element at the end
x.append(1.2)
print("x.append(1.2)? ", x)

#get a copy
y = x.copy()
print("y = x.copy()? ", y)

#how many elements are 0.0
print("y.count(0.0)? ", y.count(0.0))

#print the index with value 3.7
print("y.index(3.7)? ", y.index(3.7))

#sort the list
y.sort()
print("y.sort()? ", y)

#reverse the list
y.reverse()
print("y.reverse()? ", y)

#remove all elements
y.clear()
print("y.clear()? ", y)