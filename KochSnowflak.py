import turtle

def KochCurve(level, length, t):
	if level == 0:
		t.forward(length)
	elif level == 1:
		t.forward(length/3)
		t.left(60)
		t.forward(length/3)
		t.right(120)
		t.forward(length/3)
		t.left(60)
		t.forward(length/3)
	else:
		KochCurve(level-1, length/3, t)
		t.left(60)
		KochCurve(level-1, length/3, t)
		t.right(120)
		KochCurve(level-1, length/3, t)
		t.left(60)
		KochCurve(level-1, length/3, t)

def KochSnowflak(level, length, t):
	for angle in (0, 120, 120):
		t.right(angle)
		KochCurve(level, length, t)


if __name__ == '__main__':
	t = turtle.Turtle()
	t_wn = turtle.Screen()
	t.setheading(0)
	KochSnowflak(3, 300, t)
	t_wn.exitonclick()