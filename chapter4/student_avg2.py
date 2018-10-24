# define function to get the average of two numbers
def avg(num1, num2):
    average = (num1 + num2) / 2
    return average
    # return (num1 + num2) / 2


def student_average(name, mark1, mark2):
    print('student name', name)
    print('mark1 =', mark1)
    print('mark2 =', mark2)
    average = avg(mark1, mark2)  # function call
    print('average =', average)
    print('----------------------')


student_average('ahmed', 90, 96)
student_average('ali', 80, 99)
student_average('hasan', 65, 62)
