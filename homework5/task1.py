# Task 1:The greatest number
import random
# The empty list was created to append new values of a list
our_list = []
i = 0    # index
while i < 10:
    rand_num = random.randint(1, 100)    # random number generation
    our_list.append(rand_num)   # adding each new value to our list
    i += 1
print(our_list)
print("The max value of our randomly generated list is ", max(our_list))

