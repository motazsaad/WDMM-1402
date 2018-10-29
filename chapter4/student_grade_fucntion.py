'''
write a function that takes a student grade and return
the grade (fail, accepted, good, v. good, excellent)
'''


def grade(mark):
    if mark < 0:
        return 'bad mark'
    elif mark < 60:
        return 'fail'
    elif mark < 70:
        return 'accepted'
    elif mark < 80:
        return 'good'
    elif mark < 90:
        return 'v. good'
    elif mark <= 100:
        return 'excellent'
    else:
        return 'bad mark'


print(90, grade(90))
print(43, grade(43))
print(101, grade(101))
print(-10, grade(-10))
mark = int(input('enter your mark'))
print(mark, grade(mark))
