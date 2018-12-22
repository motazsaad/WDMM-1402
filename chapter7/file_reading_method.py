# method 1: read a file line by line
my_file = open('file_example.txt', 'r')
for line in my_file:
    print(line.strip())
print('---------------------------------')
# method 2: read the whole file
my_file = open('file_example.txt', 'r')
text = my_file.read()
print(text)
print('---------------------------------')
# method 3: read the all lines of a file
my_file = open('file_example.txt', 'r')
lines = my_file.readlines()
print(lines)
print('---------------------------------')
# it is like the list below
lstr = ['line 1\n', 'hello world\n', 'hola\n']
