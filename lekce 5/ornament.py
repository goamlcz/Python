import tkinter
canvas = tkinter.Canvas()
canvas.pack()

# 13 Vytvoř program ornament.py, který z pěti čtverců nakreslí následující ornament.
# Rozměry čtverců zvol podle svého uvážení (všechny menší čtverce budou stejně velké):

canvas.create_rectangle(100, 50, 150, 100)
canvas.create_rectangle(100, 100, 200, 200)
canvas.create_rectangle(200, 100, 250, 150)
canvas.create_rectangle(150, 200, 200, 250)
canvas.create_rectangle(50, 150, 100, 200)

canvas.mainloop()
