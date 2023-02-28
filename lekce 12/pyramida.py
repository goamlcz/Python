import tkinter
canvas = tkinter.Canvas()
canvas.pack()

for i in range(10):
    y = 200 - i * 20
    d = 100 - i * 10
    canvas.create_rectangle(190 - d, y, 190 + d, y + 20, fill='gold')

canvas.mainloop()