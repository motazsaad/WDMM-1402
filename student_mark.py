# write a program that asks the user to enter the student mark
# and print the result pass/fail, and print the if student got
# excellent or not.
mark = int(input('enter your mark:'))
if mark >= 60:
    print('pass')
    if mark >= 90:
        print('excellent')
else:  # else means (mark < 60)
    print('fail')
