'''
write a program that ask the user to enter student
mark and print his/her result (pass/fail). You have to
handle user input errors
'''
try:
    mark = int(input('enter mark: '))
except:
    mark = -1
    print('error in mark')
if mark >= 60:
    print('pass')
else:
    print('fail')
