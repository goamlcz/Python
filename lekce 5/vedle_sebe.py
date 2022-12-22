import tkinter
canvas = tkinter.Canvas()
canvas.pack()

# tady se kreslí
# Vytvoř nový program vedle_sebe.py, který vedle sebe nakreslí dva čtverce se
# stranami délky 80 (pozici čtverců zvol podle uvážení):

canvas.create_rectangle(50, 50, 130, 130)
canvas.create_rectangle(180, 50, 260, 130)

canvas.mainloop()
