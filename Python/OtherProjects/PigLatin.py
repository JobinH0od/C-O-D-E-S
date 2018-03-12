import time

def PygLatin():
	
	pyg = "ay"
	
	print("Welcome to my Pig Latin program!")

	original = input("Enter a simple word : ")

	if len(original) > 0 and original.isalpha():
		print(original)
		word = original.lower()
		first = original[0]
		
	else:
		print("Enter a valid word please")

	
	newWord = word + first + pyg
	newWord = newWord[1:]
	
	print(newWord)

	print()
	
PygLatin()	
	
	
	


time.sleep(4)