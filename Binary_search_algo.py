"""
Create a random list of numbers between 0 and 100 with a difference of 2 between each number. 
Ask the user for a number between 0 and 100 to check whether their number is in the list. 
The programme should work like this. The programme will half the list of numbers and see whether 
the users number matches the middle element in the list. If they do not match, the programme will 
check which half the number lies in, and eliminate the other half. The search then continues on the 
remaining half, again checking whether the middle element in that half is equal to the user’s number. 
This process keeps on going until the programme finds the users number, or until the size of the 
subarray is 0, which means the users number isn't in the list.
"""
import random

random_number = random.randint(0, 1)
# Making a list of 100 RANDOM numbers

number_list = [x for x in range(random_number, 100, 2)] 
random.shuffle(number_list) 

print(*number_list)
# print("Number of elements", len(number_list))

list_length = len(number_list)

# Getting the middle index of the list
middle_index = list_length//2


# First half
first_half = number_list[:middle_index]
print("\nFirst Half:", *first_half)

# Second half
second_half = number_list[middle_index:]
print("\nSecond Half:", *second_half)

user_input = int(input("Enter a number between 0 and 100: "))

# Check if the middle_index is the correct number
if number_list[middle_index] == user_input:
    print("CONGRATULATIONS! YOU GUESSED THE NUMBER!")

else: 
    print("Keep Trying!")

# A counter

counter = 0 
"""
# Trying to split the list 4 times
for x in range(4):
    
    middle_index = len(number_list)//2.
    first_half = number_list[:middle_index]
    print("\n", counter ,"Half:", *first_half)

    number_list = first_half

    counter +=1

"""