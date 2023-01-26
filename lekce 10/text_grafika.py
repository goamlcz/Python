import tkinter
canvas = tkinter.Canvas()

canvas.pack()
canvas.create_text(150, 50, text='posílám pozdrav z grafické plochy')

canvas.mainloop()