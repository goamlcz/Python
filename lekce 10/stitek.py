import tkinter
import random

vyska = 600
sirka = 800

canvas = tkinter.Canvas(width=sirka, height=vyska, bg='white')
canvas.pack()

def stitek():
    stitek_sirka = 100
    stitek_vyska = 30
    x = random.randint(0, sirka - stitek_sirka)
    y = random.randint(0, vyska - stitek_vyska)    
    text_x = x + stitek_sirka / 2
    text_y = y + stitek_vyska / 2

    canvas.create_rectangle(x, y, x + stitek_sirka, y + stitek_vyska)
    canvas.create_text(text_x, text_y, text='superman')

stitek()
stitek()
stitek()
stitek()
stitek()
stitek()
stitek()
stitek()
stitek()
stitek()

canvas.mainloop()