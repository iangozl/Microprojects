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

# Variables
answer = 1

while answer == 1:

    random_number = random.randint(0, 1)
    second_random_number = random.randint(0,100)

    # Making a list of 100 RANDOM numbers

    number_list = [x for x in range(random_number, second_random_number, 2)]

    # This list will show hints about the possible numbers in the list
    showed_list = ["_"] * len(number_list)

    # print("Number of elements", len(number_list))
    list_length = len(number_list)
    

    print("\nGuess one of the missing numbers!")

    for x in number_list:
        so_random = random.randint(0,1)
        index = number_list.index(x)
        showed_list[index] = '_'
        if so_random == 1:    
            showed_list[index] = x

    random.shuffle(showed_list)

    print("\nHere's a hint!")
    print(*showed_list)

    user_input = int(input("\nEnter a number between 0 and 100: "))

    def binarySearchIterative(the_list, number):
        left = 0
        right = len(the_list) - 1

        while left <= right:
            mid = right + left//2
            if the_list[mid] == number:
                return True
            elif number < the_list[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return False

        
    if binarySearchIterative(number_list, user_input) == True and user_input not in showed_list:
        
        for x in showed_list:
            if x == '_':
                index = showed_list.index(x)
                showed_list[index] = user_input 
        print("YOU GUESSED IT! \nThe Number is in the list!")

    else:
        print("Seems like this number is not in the list or it's already taken!")

    print("\nHere's the original list")
    print(*number_list)

    answer = int(input("\nDo you want to continue? \n1. Yes \n2. No. \nEnter your answer: "))
    if answer == 2:
        break
    else:
        continue