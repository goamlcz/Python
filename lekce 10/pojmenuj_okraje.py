import tkinter

sirka = 500
vyska = 200

canvas = tkinter.Canvas(width=sirka, height=vyska, bg='white')
canvas.pack()

canvas.create_text(sirka/2, 20, text='Horní okraj')
canvas.create_text(sirka/2, vyska-20, text='Dolní okraj')
canvas.create_text(sirka-50, vyska/2, text='Pravý okraj')
canvas.create_text(50, vyska/2, text='Levý okraj')

canvas.mainloop()