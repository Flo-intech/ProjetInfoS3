"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *
import tkinter as tk

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
can1 = Canvas(fenetre, height=1700, width=1400)
can1.pack()


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
fenetre.mainloop()
