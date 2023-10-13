#This program declares a class of my favorite animal
#and prints out its physical characteristics.


#class of my favorite animal
class Animal:
	#initialization function
	def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
		#arm & leg length are made up !
		self.arm_length = arm_length
		self.leg_length = leg_length
		self.num_eyes = num_eyes
		self.has_tail = has_tail
		self.is_furry = is_furry
	#this function prints out the features
	def print(self):
		print("Let's learn about snow leopards!")
		print(f"Length of arms = {self.arm_length}")
		print(f"Length of legs = {self.leg_length}")
		print(f"Number of eyes = {self.num_eyes}")
		print(f"Has a tail = {self.has_tail}")
		print(f"Is furry = {self.is_furry}")

#main function
def main():
	snow_leopard = Animal(10.1, 12.5, 2, True, True)
	snow_leopard.print()


#run the main function first
if __name__ == "__main__":
	main()