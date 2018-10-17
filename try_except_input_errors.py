try:
    mark = int(input('enter mark: '))
except:
    print('error in mark')
    print('please enter a numeric value')
    mark = -1  # out of range mark
if mark < 0:
    print('out of range')
elif mark < 60:
    print('fail')
elif mark <= 100:
    print('pass')
else:  # > 100
    print('out of range')
