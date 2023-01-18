import tkinter
canvas = tkinter.Canvas()
canvas.pack()

#11. Pět barevných čtverců leží těsně vedle sebe na jedné podložce. Velikosti stran jsou
#postupně 100, 80, 60, 40, 20. Napiš program rada_ctvercu.py, jestliže
#souřadnice levého dolního rohu prvního čtverce jsou v proměnných x, y:

x = 1
y = 200

canvas.create_rectangle(x, y - 100, x + 100, y, fill="red")
canvas.create_rectangle(x + 100, y - 80, x + 180, y, fill="yellow")
canvas.create_rectangle(x + 180, y - 60, x + 240, y, fill="green")
canvas.create_rectangle(x + 240, y - 40, x + 280, y, fill="pink")
canvas.create_rectangle(x + 280, y - 20, x + 300, y, fill="blue")


canvas.mainloop()
