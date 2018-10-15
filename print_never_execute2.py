'''
which of print statement that will never
execute regardless of the value of x
'''
x = int(input('enter a number: '))
if x < 2:
    print('Below 2')
elif x < 20:
    print('Below 20')
elif x < 10:
    print('Below 10')  # will never execute
else:
    print('Something else')
