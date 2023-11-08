#define some strings
s = "ASTR 19"
t = "keeps"
u = "getting"
v = "better?"

#use f-strings to print out
#the content of the strings
print(f"{s} {t} {u} {v}")

#define an integer and format
#the f-string output
i = 10230493
print(f"{i:12d}")	#print out i with 12 ttotal spaces
print(f"{i:012d}")	#print out i with 12 spaces, 0 pre-appended

#define some floating point numbers
x = 1031029233.4
print(f"x with 9 digits, 8 after decimal, sci notation = {x:9.8e}")