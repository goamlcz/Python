import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def hlava():
    canvas.create_rectangle(50, 50 ,100, 90, fill="blue")

def ruce():
    canvas.create_rectangle(0, 130, 140, 150, fill="salmon")

def nohy():
    canvas.create_rectangle(50, 200, 70, 250, fill="purple")
    canvas.create_rectangle(80, 200, 100, 250, fill="purple")

def telo():
    canvas.create_rectangle(60, 90, 90, 100, fill="lightblue")
    canvas.create_rectangle(40, 100, 110, 200, fill="navy")

hlava()
ruce()
nohy()
telo()

canvas.mainloop()
