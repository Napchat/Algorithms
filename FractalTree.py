import turtle
from random import randrange

def tree(branch_len, t, width): 
    t.width(branch_len // 10)
    if branch_len > 15: 
        if branch_len <= 25:
            t.color('red')
        t.forward(branch_len) 
        t.right(20) 
        right_len = branch_len - randrange(10, 12)
        tree(right_len, t, right_len) 
        t.left(40)
        left_len = branch_len - randrange(10, 12)
        tree(left_len, t, left_len) 
        t.right(20)
        t.backward(branch_len)
        t.color('green')

if __name__ ==  '__main__':
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75, t, 75)
    myWin.exitonclick()