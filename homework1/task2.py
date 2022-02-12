# comment from Vika
# veeeeery good job! even saving to file is written

# This code will print: This is my first home task!
print("This is my first home task!", end='\n')

# Printing numbers with weird separator
print(1,2,4,5,6,7,7,7,8,8,8,8,9,9,9,0,0, sep='_^_', end='\n')



# Weird figure picture
print('#', '#', sep='   ', end='\n')
print('##', '##', sep='  ', end='\n')
print('###', '###', sep=' ', end='\n')
print('########', end='\n')
print('#######', end='\n')
print('######', end='\n')
print('#####', end='\n')
print('####', end='\n')
print('###', end='\n')
print('##', end='\n')
print('#', end='\n')
print('#', end='\n')

# Printing output into the file
sourceFile = open('welcome.txt', 'w')
print('Hello! How you doing?', file=sourceFile, flush=True)
sourceFile.close()

# Calculating the sum of values
a=5
b=6
c=8
print(a+b+c, end='\n')
print(a-b+c, end='\n')
print(a+b-c, end='\n')

