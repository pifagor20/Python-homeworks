# Task 2: Exclusive common numbers.

import random
# The empty lists were created to append new values
our_list = []
our_second_list =[]
i = 0    # index
while i < 10:
    rand_num = random.randint(1, 10)    # Random number generation
    our_list.append(rand_num)           # Adding each new value to our first list
    rand_num_2 = random.randint(1, 10)  # Random number generation
    our_second_list.append(rand_num_2)  # Adding each new value to our second list
    i += 1
# print(our_list, our_second_list)      # To double-check that everything works as expected
st_list1 = set(our_list)                # To find common elements of set and list
intersection = st_list1.intersection(our_second_list)

print("The third list is: ", intersection)