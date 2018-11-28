# iterate over letters of a string
fruit = 'banana'

# method 1: using index and for
for i in range(len(fruit)):
    print(i, fruit[i])
print('-----------------------')
# method 2: using an iterating variable (letter)
for letter in fruit:
    print(letter)
print('-----------------------')
# method 3: using index and while
i = 0
while i < len(fruit):
    print(i, fruit[i])
    i = i + 1
