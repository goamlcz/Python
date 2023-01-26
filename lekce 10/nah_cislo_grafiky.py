import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def nahodne_cislo():
    cislo = random.randint(10000, 99999)
    x = random.randint(0, 300)
    y = random.randint(0, 250)
    canvas.create_text(x, y, text=cislo)

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