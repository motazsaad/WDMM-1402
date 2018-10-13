# multi way if
x = int(input('enter number: '))
if x < 2:
    print('small')
elif x < 10:  # else mean x >=2
    print('Medium')
else:  # else mean x >= 10
    print('LARGE')
print('All done')
