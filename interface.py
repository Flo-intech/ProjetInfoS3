from tkinter import *
import tkinter as tk

window = Tk()
c = Canvas(window, height=800, width=800)
c.pack()

# fenetre
window.title("Inscription")
window.geometry("720x480")

mappemonde = PhotoImage(file="mappemonde.png")
button1 = PhotoImage(file="button1.png")

c.create_image(350, 270, image=mappemonde)

buttonSouthAmerica = Button(window, image=button1, height=15, width=15).place(x=170, y=310)
buttonNorthAmerica = Button(window, image=button1, height=15, width=15).place(x=100, y=170)
buttonAsia = Button(window, image=button1, height=15, width=15).place(x=500, y=170)
buttonEurope = Button(window, image=button1, height=15, width=15).place(x=350, y=170)
buttonAfrica = Button(window, image=button1, height=15, width=15).place(x=370, y=270)
buttonOceania = Button(window, image=button1, height=15, width=15).place(x=610, y=350)


window.mainloop()
