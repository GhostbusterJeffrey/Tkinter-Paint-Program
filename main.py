import turtle, tkinter

larry = turtle.Turtle()
window = tkinter.Tk()
window.title("Paint")
window.geometry('135x100')
turtle.title("Paint")

def turn_left():
    larry.left(10)

def turn_right():
    larry.right(10)

def pen_up():
    larry.penup()

def pen_down():
    larry.pendown()

def forward():
    larry.forward(10)

def backward():
    larry.backward(10)

def clear():
    larry.clear()

button1 = tkinter.Button(window, text="Left", command=turn_left).grid(column=1, row=1)
button2 = tkinter.Button(window, text="Right", command=turn_right).grid(column=2, row=1)
button3 = tkinter.Button(window, text="Forward", command=forward).grid(column=1, row=2)
button4 = tkinter.Button(window, text="Backward", command=backward).grid(column=2, row=2)
button5 = tkinter.Button(window, text="Pen Up", command=pen_up).grid(column=1, row=3)
button6 = tkinter.Button(window, text="Pen Down", command=pen_down).grid(column=2, row=3)
button7 = tkinter.Button(window, text="Clear", command=clear).grid(column=1, row=4)

window.mainloop()
turtle.done()
