# void vs return functions
def add1(n1, n2):  # void function
    print(n1 + n2)


def add2(n1, n2):  # function return a value
    return n1 + n2


x = add1(2, 4)
print('value of x:', x)  # output: x = None
add2(3, 4)  # no output
add2(4, 9)  # no output
x = add2(3, 4)  # returned value assigned to x
print('value of x:', x)  # output: value of x: 7
x = x + 10
print('value of x:', x)  # output: value of x: 17
print(add2(1, 2))  # output: 3
print(add2(1, 2) + 9)  # output: 12
