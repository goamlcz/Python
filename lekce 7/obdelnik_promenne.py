import tkinter
canvas = tkinter.Canvas()
canvas.pack()

x = 100
y = 70
sirka = 200
vyska = 50
cervena = "red"

canvas.create_rectangle(x, y, x + sirka, y + vyska, fill=cervena)

canvas.mainloop()
