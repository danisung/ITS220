print("Hello kids!! Lets play a fun adding game!!")
print("Can you guess what is?")
import random #the randomness
x = random.randrange(1,9)
y = random.randrange(1,9)
numbers = int(x+y) #these are the random numbers that will appear.
print (x, "+", y)
guess = int(input("Enter your guess:"))
n = 0
while n != 1: #this is the loop
	if guess == numbers:
		print("You are correct!!")
		n = 1
	else:
		print("Incorrect")
		guess = int(input("Sorry, try again:"))
print("Congratulations!! You win!!")