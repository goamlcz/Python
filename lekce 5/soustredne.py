import tkinter
canvas = tkinter.Canvas()
canvas.pack()

# první čtverec o straně délky 100
canvas.create_rectangle(100, 100, 200, 200)
# druhý čtverec o straně délky 150
canvas.create_rectangle(75, 75, 225, 225)

canvas.mainloop()
