import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def nahodny_ctverec():
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    velikost = 50
    canvas.create_rectangle(x, y, x + velikost, y + velikost, fill='blue')

def nahodny_obdelnik():
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    velikost_a = random.randint(10, 50)
    velikost_b = random.randint(10, 50)
    canvas.create_rectangle(x, y, x + velikost_a, y + velikost_b, fill='green')

nahodny_ctverec()
nahodny_obdelnik()
nahodny_ctverec()
nahodny_obdelnik()
nahodny_ctverec()
nahodny_obdelnik()
nahodny_ctverec()
nahodny_obdelnik()
nahodny_ctverec()
nahodny_obdelnik()

canvas.mainloop()