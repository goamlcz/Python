import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def nahodny_ctverec():
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    velikost = 50
    canvas.create_rectangle(x, y, x + velikost, y + velikost, fill='blue')

nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()

canvas.mainloop()