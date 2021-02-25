"""
This is probably the hardest one out of these 6 small projects. This will be similar to guessing
the number, except we are guessing the word. The user needs to guess letters, Give the user no more 
than 6 attempts for guessing wrong letter. This will mean you will have to 
have a counter. You can download a ‘sowpods’ dictionary file or csv file to use as a way to get a 
random word to use.
"""
import string
import random

print ("Guess the word or the guy dies")

ascii_letters = string.ascii_letters

# Variable declaration

letter = 'aa'
huge_list = []
counter = 0

with open('sowpods.txt', "r") as f:
    huge_list = f.read().split()

word = huge_list[random.randint(0, len(huge_list))]

# Creating an empty list with determined length AND character
guessed_word = ['_'] * len(word)

while counter <=6:

    input_letter = input("Enter a letter: ").upper()

    # Check if the input_letter is in the word
    if input_letter in word:

        print("There's a match!")
        
        # Find the index of the letter:
        index = word.index(input_letter)

        # If the space is empty, then replace it
        if guessed_word[index] == '_':
        
            guessed_word[index] = input_letter

            # * Prints the whole list in one line.
            print(*guessed_word)
        
        else:
            print('Try another letter, this is already taken!')
            
    else:
        print("Nah! Try again!")
    counter+=1

print("The word was :", word)
# Verification stage
"""
while len(letter) > 1:
    letter = input ("Enter a letter: ")
    
    if len(letter) == 1 and letter.isnumeric() == False:
        for x in ascii_letters:
            if letter == x:
                print("There's a match")
            break
    elif letter.isnumeric():
        print("We don\'t like any numbers around here")
    else:
        print("Just enter one letter. Just one. Not any number nor special characters")

"""







