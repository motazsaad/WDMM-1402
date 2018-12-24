fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if not line.startswith('From:'):
        continue
    print(line)
