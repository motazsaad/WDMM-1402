# read arabic file with utf-8 encoding

file_handle = open('arabic_file.txt', 'r', encoding='utf-8')
print(file_handle)
line_count = 0
for line in file_handle:
    print(line.strip())
    line_count += 1
print('# of lines:', line_count)
