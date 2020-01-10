# This is a collection of functions that creates snowflakes using turtle
import turtle

pat = turtle.Turtle()
pat.speed(0)

def flake1(size, color='red'):
    pat.color(color)
    for i in range(12):
        for j in range(2):
            pat.forward(10 * size)
            pat.right(60)
            pat.forward(10 * size)
            pat.right(120)
        pat.right(30)

flake1(20)
flake1(4, 'blue')

pat.forward(100)
