import random
r= True
while r:
	print("you rolled",random.randint(1,6))
	print("do u want to roll again? yes/no")
	r="yes"in input()
