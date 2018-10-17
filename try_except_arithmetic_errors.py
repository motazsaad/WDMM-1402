n1 = int(input('enter 1st number: '))
n2 = int(input('enter 2nd number: '))
op = input('enter operator: ')
if op == '*':
    print(n1 * n2)
if op == '/':
    try:
        print('before')
        print(n1 / n2)  # dangerous line
        print('after')
    except:
        print('division by zero error')
        print('2nd number can not be zero in division')
