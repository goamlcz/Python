import tkinter

canvas = tkinter.Canvas()
canvas.pack()

for i in range(6):
    x = i * 50 + 10
    canvas.create_rectangle(x, 100, x + 20, 200, fill='red')

canvas.mainloop()