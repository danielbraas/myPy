# This is a collection of functions that creates snowflakes using turtle
import turtle

pat = turtle.Turtle()

def flake1(size):    #should add color option
    for i in range(12):
        for j in range(2):
            pat.forward(10 * size)
            pat.right(60)
            pat.forward(10 * size)
            pat.right(120)
        pat.right(30)

flake1(20)
input()