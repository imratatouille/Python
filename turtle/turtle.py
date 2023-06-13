
import turtle as t

t.shape('turtle')
t.speed(500)
t.pensize(1)
t.color("cyan")
def draw1(line, angle):
	t.begin_fill()
	for i in range(line):
		t.forward(i + 3)
		t.right(angle + 4)
	t.end_fill()


def draw2(line, angle):
	t.begin_fill()
	for i in range(line):
		t.forward(i + 2)
		t.right(angle + 4)
	t.end_fill()

t.color('magenta')
draw2()

t.mainloop()