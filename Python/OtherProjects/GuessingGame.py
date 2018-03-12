import random

guessesTaken = 0 

print("Hello, what is your name? : ")
myName = input()

number = random.randint(1,5)
print("Well, " + myName + ", I am thinking of a random number between 1 & 5.")

while guessesTaken < 5:
	print("Take a guess.")
	guess = input() 
	guess = int(guess)

	guessesTaken += 1

	if guess < number:
		print("Your guess is too low.")

	if guess > number:
		print("Your guess is too high.")

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print("Good job," + myName + "! You guessed my number in " + guessesTaken + " guesses!")

if guess != number:
	number = str(number)
	print("Nope. The number I was thinking of was " + number + ".")