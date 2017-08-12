import turtle
from turtle import left, right, forward

size = 30

def hilbert(level, angle):
    if level == 0:
        return

    turtle.color("Blue")
    turtle.speed('slowest')

    right(angle)
    hilbert(level - 1, -angle)
    forward(size)
    left(angle)
    hilbert(level - 1, angle)
    forward(size)
    hilbert(level - 1, angle)
    left(angle)
    forward(size)
    hilbert(level - 1, -angle)
    right(angle)

if __name__ == '__main__':
	hilbert(2, 90)