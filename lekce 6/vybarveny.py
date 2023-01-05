import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 50, 130, 130, fill='red')
canvas.create_rectangle(150, 50, 230, 130, fill='blue')
canvas.create_rectangle(50, 150, 130, 230, fill='yellow')
canvas.create_rectangle(150, 150, 230, 230, fill='green')

canvas.mainloop()
