#####################################

import turtle as t

t.shape('turtle')
t.speed(0)
t.pensize(3)
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

t.color('yellow')
draw2(300, 90)

t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()

t.color('blue')
draw1(150, 72)


t.mainloop()

###############################################

from tkinter import *
import turtle as t

win = Tk()

win.geometry("400x600")
win.title("turtle")

def pri():
    t.shape("turtle")
    t.speed(100)
    t.pensize(4)
    t.color("cyan")
    while(1):
        t.forward(100)
        t.left(120)
        t.forward(100)
        t.left(121)
b1 = Button(text="버튼입니다", command=pri)

b1.config(command=pri)

b1.pack()
win.mainloop()

