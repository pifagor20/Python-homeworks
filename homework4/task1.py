# Task 1: The Guessing Game.
import random

print("Let's play the game!")
player = int(input("Please choose the number from 1 to 10. Let's check how great your intuition is :D "'\n'
                   "Print the number here: "))
# Checking if the value is included in our range
if 10 >= player >= 1:
    computer = random.randint(1, 10)

# The winner's message in case the person chosen the right number
    if computer == player:
        print("You are the winner! The number is right! :)")

# The message in case of incorrect number
    elif computer != player:
        print("Your intuition is not so great :( ...Will see if you have more luck next time!" +
              "The number was " + str(computer) + "...")
else:
    print("Your input is breaking the game :(((... Please enter the number within the range from 1 to 10 included!")