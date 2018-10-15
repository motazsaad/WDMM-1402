'''
write a program that ask the user to
enter the student mark and print the
grade (excellent, v. good, good,
acceptable, fail).
'''
mark = int(input('enter mark: '))
if mark < 0:
    print('out of range')
elif mark < 60:
    print('fail')
elif mark < 70:
    print('acceptable')
elif mark < 80:
    print('good')
elif mark < 90:
    print('v. good')
elif mark <= 100:
    print('excellent')
else:
    print('out of range')
