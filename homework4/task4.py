# Task 4: The math quiz program
import random
while True:
    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    print("Please calculate the sum of ", num_1, "+", num_2)
    user_input = input("Please enter the answer here or use 'q' to quit: ")
    if user_input == 'q':
        print("Goodbye!")
        break
    elif int(user_input) == num_1 + num_2:
        print("You are the winner here! Yoooohooo!")
    else:
        print("We hope you will have more luck next time...")
