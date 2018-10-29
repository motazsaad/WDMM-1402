'''
write a function that compute the following expression
x to the power of (y to the power z)
'''


def my_power(x, y, z):
    # w = y ** z
    # return x ** w
    return x ** (y ** z)


print(my_power(2, 3, 2))
