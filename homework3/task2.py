# Task 2: The valid phone number program
phone_number = '3048dfsd58'

# Check if entered values are numbers and the phone number is 10 digits long
if phone_number.isdigit() and len(phone_number) == 10:
    print("The number is " + phone_number + " correct")

# Warning when the number is more or less than 10 digits
elif phone_number.isdigit() and len(phone_number) > 10:
    print("Your number is more than 10 digits. Please recheck it. Should be 10 digits.")
elif phone_number.isdigit() and len(phone_number) < 10:
    print("Your number is less than 10 digits. Please recheck it. Should be 10 digits.")

# When the client will enter the numbers this warning will appear
else:
    print("The entered number is wrong! Please note that our system accept only numbers! Thanks :) ")