import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(30, 30, 330, 80, fill='red')
canvas.create_rectangle(30, 80, 330, 130, fill='white')
canvas.create_rectangle(30, 130, 330, 180, fill='blue')

canvas.mainloop()