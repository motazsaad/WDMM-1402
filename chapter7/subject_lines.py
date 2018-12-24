'''
write a program that asks the user to enter a file name,
then read the file and count the lines that start with Subject.
If the file name is incorrect, print an error message to user
that the file not found.
'''

file_name = input('enter file name: ')
try:
    subject_count = 0
    my_file = open(file_name, 'r')
    for line in my_file:
        if line.strip().startswith('Subject:'):
            subject_count += 1
    print('subject count:', subject_count)
except:
    print('file not found')
