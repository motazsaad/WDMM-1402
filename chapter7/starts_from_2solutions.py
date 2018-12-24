# solution 1 (continue)
my_file = open('mbox-short.txt', 'r')
for line in my_file:
    line = line.strip()
    if not line.startswith('From:'):
        continue
    print(line)

print('------------------------------')
# solution 2 (without continue)
my_file = open('mbox-short.txt', 'r')
for line in my_file:
    line = line.strip()
    if line.startswith('From:'):
        print(line)
