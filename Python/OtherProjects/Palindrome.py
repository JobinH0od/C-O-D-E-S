word = input("Enter a simple word : ")

if word[::-1].upper() == word.upper():
    print("This word is a palindrome")

elif word[::-1].upper() != word.upper():
    print("This word is not a palindrome... It prints", word[::-1].upper(), "when reversed.")
