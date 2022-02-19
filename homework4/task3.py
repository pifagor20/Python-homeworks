# Task 3: Words combination
# The first version when we use random shuffle, in this case our original input word will be changed as well
import random
# input the word that should be mixed
word = list(input("Please enter the word you want to mix: "))
counter = 0
while counter < 5:
    counter += 1
    random.shuffle(word)
    result = ''.join(word)
    print( result)

# The second version  when we use random sample, in this case our original input word will not be changed

# input the word that should be mixed
word_2 = input("Please enter the word you want to mix: ")
counter = 0
while counter < 5:
    counter += 1
    result_2 = ''.join(random.sample(word_2, len(word_2)))
    print(result_2)
