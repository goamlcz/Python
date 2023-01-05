import tkinter
canvas = tkinter.Canvas() 
canvas.pack()

canvas.create_rectangle(10, 10, 110, 190, fill='green')
canvas.create_rectangle(110, 10, 210, 190, fill='white')
canvas.create_rectangle(210, 10, 310, 190, fill='red')


canvas.mainloop()
