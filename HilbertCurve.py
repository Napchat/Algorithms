import turtle
from turtle import left, right, forward

size = 30

'''def hilbert(level, angle):
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
    right(angle)'''

def draw_base_curve(angle, t):
    for i in range(3):
        t.forward(size)
        t.right(angle)

def hilbert(level, direction, t):
    if level == 1:
        if direction == 'left':
            t.setheading(0)
            draw_base_curve(90, t)
        elif direction == 'right':
            t.setheading(180)
            draw_base_curve(90, t)
        elif direction == 'up':
            t.setheading(270)
            draw_base_curve(-90, t)
        elif direction == 'down':
            t.setheading(90)
            draw_base_curve(-90, t)
        return
    else:
        if direction == 'left':
            hilbert(level-1, 'up', t)
            t.setheading(0)
            t.forward(size)
            hilbert(level-1, 'left', t)
            t.setheading(270)
            t.forward(size)
            hilbert(level-1, 'left', t)
            t.setheading(180)
            t.forward(size)
            hilbert(level-1, 'down', t)
        elif direction == 'right':
            hilbert(level-1, 'down', t)
            t.setheading(180)
            t.forward(size)
            hilbert(level-1, 'right', t)
            t.setheading(90)
            t.forward(size)
            hilbert(level-1, 'right', t)
            t.setheading(0)
            t.forward(size)
            hilbert(level-1, 'up', t)
        elif direction == 'up':
            hilbert(level-1, 'left', t)
            t.setheading(270)
            t.forward(size)
            hilbert(level-1, 'up', t)
            t.setheading(0)
            t.forward(size)
            hilbert(level-1, 'up', t)
            t.setheading(90)
            t.forward(size)
            hilbert(level-1, 'right', t)
        else:
            hilbert(level-1, 'right', t)
            t.setheading(90)
            t.forward(size)
            hilbert(level-1, 'down', t)
            t.setheading(180)
            t.forward(size)
            hilbert(level-1, 'down', t)
            t.setheading(270)
            t.forward(size)
            hilbert(level-1, 'left', t)
        return
        
if __name__ == '__main__':
    t = turtle.Turtle()
    t_win = turtle.Screen()
    #t.speed('slowest')
    hilbert(2, 'up', t)
    t_win.exitonclick()