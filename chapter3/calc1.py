'''
write a program that asks the user to enter two
numbers and the operator (*, /), and compute the result
according the operator.
'''
number1 = float(input('enter 1st number:'))
number2 = float(input('enter 2nd number:'))
op = input('enter operator: ')
# addition
if op == '+':
    print(number1 + number2)
# subtraction
if op == '-':
    print(number1 - number2)
# you can complete the code for * and / operators
