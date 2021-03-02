"""
Create a random list of numbers between 0 and 100 with a difference of 2 between each number. Ask the user for a number between 0 
and 100 to check whether their number is in the list. The programme should work like this. The programme will half the list of 
numbers and see whether the users number matches the middle element in the list. If they do not match, the programme will check 
which half the number lies in, and eliminate the other half. The search then continues on the remaining half, again checking 
whether the middle element in that half is equal to the user’s number. This process keeps on going until the programme finds the 
users number, or until the size of the subarray is 0, which means the users number isn't in the list.

"""

import random

# Making a list of 100 RANDOM numbers
number_list = [random.randint(0, 100) for x in range(100)]

print(*number_list)
print("Number of elements", len(number_list))