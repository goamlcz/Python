import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(30, 30, 330, 200, fill='white')
canvas.create_rectangle(30, 100, 330, 130, fill='blue')
canvas.create_rectangle(100, 30, 130, 200, fill='blue')


canvas.mainloop()