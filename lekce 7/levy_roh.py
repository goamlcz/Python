import tkinter
canvas = tkinter.Canvas()
canvas.pack()

#Tyto čtverce mají společný levý horní roh, jehož souřadnice jsou v proměnných x, y.
#Čtverce se postupně zmenšují tak, že červený má délku strany 100, modrý 70
#a tmavomodrý 40.

x = 100
y = 60
cerveny = 100
modry = 70
tmavemodry = 40
cervena = "red"
modra = "blue"
tmavemodra = "darkblue"

canvas.create_rectangle(x, y, x + cerveny, y + cerveny, fill=cervena)
canvas.create_rectangle(x, y, x + modry, y + modry, fill=modra)
canvas.create_rectangle(x, y, x + tmavemodry, y + tmavemodry, fill=tmavemodra)

canvas.mainloop()
