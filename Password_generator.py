import random

def items():
	items.Numbers = range(1,100001)
	items.Up_Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	items.Low_Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	items.Characters = ['@','#','&','!','*','%','(',')','?']

def generator(factors):
	Num_gen = random.choice(items.Numbers)
	Up_gen = random.choice(items.Up_Letters)
	Low_gen = random.choice(items.Low_Letters)
	Char = random.choice(items.Characters)

	print(str(Low_gen) + str(Num_gen) + str(Up_gen) + str(Up_gen)+ str(Low_gen) + str(Char))
	

generator(items())