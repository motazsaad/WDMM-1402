'''
write a program to read a file and print
- number of lines
- number of lines that start with "From"
'''

mail_file = open('mbox-short.txt', 'r')
# r = read
# w = write
print(mail_file)
# read file line by line
line_count = 0
from_count = 0
for line in mail_file:
    line_count += 1
    if line.startswith('From:'):
        from_count += 1
print('# of lines:', line_count)
print('# from lines:', from_count)
