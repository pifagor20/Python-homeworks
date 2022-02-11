# Greeting program
my_name = ' Mariia'
today_date = '11/02/2022'
# The first type of string formatting
print(f'Good day {my_name}! {today_date} is a perfect day to learn some python.')

# The second type of string formatting
s = 'Good day {}! {} is a perfect day to learn some python.'
print(s.format(my_name.upper(), today_date))

# The third type of string formatting
print('Good day %s! %s is a perfect day to learn some python.' % (my_name, today_date))

# The fourth type of string formatting
print('Good day {1}! {0} is a perfect day to learn some python.'.format(today_date, my_name))
