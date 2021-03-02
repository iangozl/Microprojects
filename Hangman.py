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

huge_list = []
counter = 0
winning_code = 0

with open('sowpods.txt', "r") as f:
    huge_list = f.read().split()

#word = huge_list[random.randint(0, len(huge_list))]
word = "AMA"

# Creating an empty list with determined length AND character
guessed_word = ['_'] * len(word)

while counter < 6:

    input_char = input("Enter a letter: ").upper()

    # Check if the INPUT_CHAR is equal to 1 character or not

    if len(input_char) > 1:

        if input_char == word:
            print('You guessed the word! CONGRATULATIONS!')
            winning_code = 1
            break

        else:
            print('Sorry! Try Again!')
        
    elif len(input_char) == 1:  
        
        # Making a list of a character that is repeated in the word 
        list_indexes = [idx for idx, char in enumerate(word) if char == input_char]

        # If it's greater than zero, that means it's not empty, then we can proceed with the other calculations
        if len(list_indexes) > 0:            
            
            print("There's a match!")
            
            loop_counter = 0

            for index in list_indexes:

                # If the space is empty, then replace it
                if guessed_word[index] == '_':
                    guessed_word[index] = input_char
                    # * Prints the whole list in one line.
                    print(*guessed_word)
                    break

                loop_counter += 1
                
                if loop_counter == len(list_indexes) and guessed_word[index] != '_': 
                    print("Letter already taken")

        else:
            print("Nah! This letter it's not in the word!")
    counter+=1
    print(6 - counter,"tries left")

if winning_code == 0:
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







