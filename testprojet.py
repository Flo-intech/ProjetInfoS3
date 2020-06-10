"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *
import tkinter as tk

#menu
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
can1 = Canvas(fenetre, height=1700, width=1400)
can1.pack()
menubar = Menu(fenetre)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="FOOTBALL", command=donothing)
filemenu.add_command(label="BASKETBALL", command=donothing)
filemenu.add_command(label="TENNIS", command=donothing)
filemenu.add_command(label="NATATION", command=donothing)
filemenu.add_command(label="ATHLETISME", command=donothing)

#menu
filemenu.add_separator()

filemenu.add_command(label="Exit", command=fenetre.quit)
menubar.add_cascade(label="Menu", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Tout les sports", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Football", command=donothing)
editmenu.add_command(label="Basketball", command=donothing)
editmenu.add_command(label="Tennis", command=donothing)
editmenu.add_command(label="Natation", command=donothing)
editmenu.add_command(label="Athletisme", command=donothing)

menubar.add_cascade(label="Quiz", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Football", command=donothing)
helpmenu.add_command(label="Basketball", command=donothing)
helpmenu.add_command(label="Tennis", command=donothing)
helpmenu.add_command(label="Natation", command=donothing)
helpmenu.add_command(label="Athlétisme", command=donothing)
menubar.add_cascade(label="Matchs en direct", menu=helpmenu)

# fenetre
fenetre.title("Mapcompetition")
fenetre.geometry("1920x1080")

mappemonde = PhotoImage(file="BlankMap-World-v5.png")
point = PhotoImage(file="point.png")
pointColombie = Button(fenetre, image=point, height=15, width=15).place(x=559, y=420)
pointJapon = Button(fenetre, image=point, height=15, width=15).place(x=1400, y=250)
pointUsa = Button(fenetre, image=point, height=15, width=15).place(x=500, y=250)
pointFrance = Button(fenetre, image=point, height=15, width=15).place(x=875, y=225)
pointAlgerie = Button(fenetre, image=point, height=15, width=15).place(x=900, y=300)
pointAustralie = Button(fenetre, image=point, height=15, width=15).place(x=1380, y=550)



can1.create_image(700, 400, image=mappemonde)



# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.config(menu=menubar)
fenetre.mainloop()
