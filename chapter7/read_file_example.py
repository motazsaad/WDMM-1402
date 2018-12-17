file_handle = open('file_example.txt', 'r')
# read file line by line
for line in file_handle:
    # clean_line = line.strip()
    # if clean_line.endswith(','):
    #     print(line)

    if line.strip().endswith(','):
        print(line)
