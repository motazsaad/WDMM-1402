'''
Write a program that calculates student's GPA.
The program asks the user to enter the mark and hours for each
course. The program should ask the user for entering another course
or not, and the user respond (yes/no).
'''
answer = 'yes'
total_hours = 0
mark_hours = 0
while answer == 'yes':
    mark = int(input('enter mark: '))
    hours = int(input('enter hours: '))
    total_hours = total_hours + hours
    mark_hours = mark_hours + mark * hours
    answer = input('enter another course? yes/no: ')

print('total hours:', total_hours)
print('GPA: ', mark_hours / total_hours)
