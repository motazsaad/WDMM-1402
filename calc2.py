'''
write a program that asks the user to enter two
numbers and the operator (*, /), and compute the result
according the operator. You have to handle error
in user's input
'''
num1 = int(input('enter 1st number: '))
num2 = int(input('enter 2nd number: '))
op = input('enter operator: ')
if op == '*':
    print(num1 * num2)
if op == '/':
    try:
        print(num1 / num2)
        print('anything')
    except:
        print('error: division by zero')
