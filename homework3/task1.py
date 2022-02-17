# The program will print the first 2 and last  2 letters of our input
a = ('Hello World')
if len(a) >= 2:
    print(a[0:2] + a[-2:])

# When the word is one letter it will print empty string
else:
    print('')