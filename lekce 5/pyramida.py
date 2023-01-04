import tkinter
canvas = tkinter.Canvas()
canvas.pack()

# 12. Vytvoř program pyramida.py, který ze tří obdélníků o rozměrech 150x50, 100x50
# a 50x50 nakreslí následující pyramidu:

canvas.create_rectangle(200, 50, 250, 100)
canvas.create_rectangle(200-25, 100, 250+25, 150)
canvas.create_rectangle(200-25-25, 150, 250+25+25, 200)

canvas.mainloop()
