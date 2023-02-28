import tkinter
import random

canvas = tkinter.Canvas(background='navy')
canvas.pack()

def hvezdicka():
    x = random.randint(10, 360)
    y = random.randint(10, 250)
    a = random.randint(2, 4)
    canvas.create_rectangle(x, y, x + a, y + a, fill='yellow')


for i in range(1000):
    hvezdicka()

canvas.mainloop()