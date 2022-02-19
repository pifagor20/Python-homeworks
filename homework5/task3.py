# Task 3: Extracting numbers.
my_list = list(range(1, 100))               # List creation
my_new_list = []                            # The new list where the extracted values will be added
i = 0
# The cycle to identify numbers divisible by 7 but not a multiple of 5
while i < len(my_list):
    elem = my_list[i]
    if elem % 7 == 0 and elem % 5 != 0:
        my_new_list.append(elem)
    i += 1
print("Hello! I am your newly created list !;D ", '\n', my_new_list)
