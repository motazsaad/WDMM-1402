'''
rewrite the calculator program using return function
'''


def calc(n1, n2, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2


print(calc(3, 4, '+') - 7)
print(calc(1, 4, '-') + 2)
print(calc(9, 10, '+') + 13)
result = calc(3, 6, '+')
print('result: ', result)
