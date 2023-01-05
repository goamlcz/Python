import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(30, 30, 130, 130, fill='red')
canvas.create_rectangle(160, 30, 260, 130, fill='green')
canvas.create_rectangle(30, 160, 130, 260, fill='blue')
canvas.create_rectangle(160, 160, 260, 260, fill='yellow')


canvas.mainloop()