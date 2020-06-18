"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *
import tkinter as tk
class Mappemonde:

    def __init__(self, master):
    
        self.master=master
        self.master.geometry("1920x1080")
        self.master.title("Mapcompetition")       
        self.mappemonde = PhotoImage(file="BlankMap-World-v5.png") 

        self.can1 = Canvas(self.master, height=1700, width=1400)
        self.can1.create_image(700, 400, image=self.mappemonde)      
        self.can1.pack()

        self.point = PhotoImage(file="point.png")
        self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
        self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)
        self.pointUsa = Button(self.master, image=self.point, height=15, width=15).place(x=500, y=250)
        self.pointFrance = Button(self.master, image=self.point, height=15, width=15).place(x=875, y=225)
        self.can1pointAlgerie = Button(self.master, image=self.point, height=15, width=15).place(x=900, y=300)
        self.pointAustralie = Button(self.master, image=self.point, height=15, width=15).place(x=1380, y=550)
