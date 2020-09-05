# Exercise 1:
fruit = 'banana'

index = len(fruit)
while index >= 1:
    letter = fruit[index - 1]
    print(letter)
    index = index - 1

# Exercise 3:

def count(string, letter):
    count = 0 # I know this is not cool...but it works
    for l in string:
        if l == letter:
            count += 1
    print(count)        

fruit.find('b')

camels = 42
'I have spotted %d camels.' % camels
'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

