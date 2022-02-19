# Task 2: The birthday greeting program.
while True:
    name = input("Please, enter your name: ")

    # Validation of a name value
    if not name.isalpha():
        print("Your input is wrong. The name can accept only letters.")
        continue

    age = input("How old are you? " '\n' "Please write here using numbers: ")

    # Validation of an age value
    if not age.isdigit():
        print("Your input is wrong. The age can accept only numbers.")
        continue

    # Expected greeting
    print("Hello " + name + " on your next birthday you’ll be " + str(int(age)+1) + " years")
    break

