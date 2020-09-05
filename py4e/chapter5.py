n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
    print(str(count) + ':', itervar)
print('Count: ', count)

largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)