fhand = open('mbox-short.txt')
fhand

count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

fhand = open('mbox-short.txt')
inp = fhand.read()

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)

fhand = open('mbox-short.txt')
for line in fhand:
line = line.rstrip()
if line.startswith('From:'):
print(line)        

count = 0
for letter in inp:
    count += 1
print(count)

