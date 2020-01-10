print('hello world!')

inp = input('Some silly stuff')
print(inp)

speed = input('Something: ')
if type(speed) != ''

type(speed)

int(15.4)

x = input('How many hours: ')
x = float(x)
rate = 10
if x > 40:
    print('Wage:', rate * 40 + 1.5 * rate * (x-40))
else:
    print('Wage:', rate * x)

#more sophisticated script
rate = input('Rate: ')
try:
    rate = float(rate)
except:
    print('non-numeric value for rate')

hours = input('How many hours: ')
try:
    hours = float(hours)
    if hours > 40:
        print('Wage:', rate * 40 + 1.5 * rate * (hours-40))
    else:
        print('Wage:', rate * hours)
except:
    print('non-numeric value entered')

#Excercise #3

x = input('Enter score between 0.0 and 1.0: ')
try:
    x = float(x)
    if (1.0 > x > 0.0):
        if x < 0.6:
            print('F')
        elif x >= 0.9:
            print('Perfect:\nA')
        elif x >= 0.8:
            print('B')
        elif x >= 0.7:
            print('C')
        elif x >= 0.6:
            print('D')
    else:
        print("Bad range")
except:
    print("You did not enter a number")
