import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 50, 150, 150, fill='teal')
canvas.create_rectangle(70, 70, 170, 170, fill='cyan')
canvas.create_rectangle(90, 90, 190, 190, fill='deepskyblue')
canvas.create_rectangle(110, 110, 210, 210, fill='aquamarine')

canvas.mainloop()