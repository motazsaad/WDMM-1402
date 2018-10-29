'''
write a function that takes two numbers and return
the maximum
'''


def my_max(x, y):
    if x > y:
        return x
    else:
        return y


'''
write a function that takes two numbers and return 
the minimum 
'''


def my_min(x, y):
    if x < y:
        return x
    else:
        return y


print(my_max(3, 4))  # 4
print(my_min(2, 7))  # 2
# print(my_max(7, '3')) # type error

n1 = int(input('enter 1st no.: '))
n2 = int(input('enter 1st no.: '))
print(my_max(n1, n2))
