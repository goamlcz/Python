import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def nahodne_cislo():
    cislo = random.randint(10000, 99999)
    x = random.randint(50, 300)
    y = random.randint(50, 200)
    canvas.create_text(x, y, text=cislo, font="arial 20")

nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()

canvas.mainloop()
