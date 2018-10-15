'''
which of print statement that will never
execute regardless of the value of x
'''
x = int(input('enter a number: '))
if x < 2:
    print('Below 2')
elif x >= 2:
    print('Two or more')
else:
    print('Something else')  # will never execute
