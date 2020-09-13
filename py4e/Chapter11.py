# Chapter 11: Regular expressions

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

count = 0
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('[Ff]rom', line):
        print(line)
        count += 1
print('There were ' + str(count) + ' instances.')

inp = open('mbox-short.txt').read()
len(re.findall('[Ff]rom', inp))
test = re.search('[Ff]rom', inp[4:])
test.span()[1]
test.start()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:|from', line):
        print(line)

mail = str()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)
       # mail =  # Concatenating mail and match to collect all matches

y = list()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        y.append(x)
        print(x)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)      
