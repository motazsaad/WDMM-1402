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
