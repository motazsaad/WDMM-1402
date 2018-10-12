mark = int(input('enter your mark:'))
if mark >= 60:
    print('pass')
    if mark >= 90:
        print('excellent')
else:  # else means (mark < 60)
    print('fail')
