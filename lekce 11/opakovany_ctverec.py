import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def cerveny_ctverec():
    x = random.randint(10, 360)
    y = random.randint(10, 250)
    canvas.create_rectangle(x, y, x + 10, y + 10, fill='red')

def modry_ctverec():
    x = random.randint(10, 360)
    y = random.randint(10, 250)
    canvas.create_rectangle(x, y, x + 10, y + 10, fill='blue')

for i in range(2000):
    cerveny_ctverec()
    modry_ctverec()

canvas.mainloop()
