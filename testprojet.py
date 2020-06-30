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
        self.pointColombie = Button(self.master, image=self.point, height=15, width=15, command=self.change_north_america).place(x=559, y=420)
        self.pointJapon = Button(self.master, image=self.point, height=15, width=15, command=self.change_asie).place(x=1400, y=250)
        self.pointUsa = Button(self.master, image=self.point, height=15, width=15, command=self.change_north_america).place(x=500, y=250)
        self.pointFrance = Button(self.master, image=self.point, height=15, width=15, command=self.change_europa).place(x=875, y=225)
        self.can1pointAlgerie = Button(self.master, image=self.point, height=15, width=15, command=self.change_africa).place(x=900, y=300)
        self.pointAustralie = Button(self.master, image=self.point, height=15, width=15, command=self.change_oceanie).place(x=1380, y=550)

    def change_north_america(self):
        root1=Toplevel(self.master)
        north_america=NorthAmerica(root1)

    def change_europa(self):
        root2=Toplevel(self.master)
        europe=Europe(root2)

    def change_africa(self):
        root3=Toplevel(self.master)
        africa=Africa(root3)

    def change_south_america(self):
        root4=Toplevel(self.master)
        America=SouthAmerica(root4)

    def change_asie(self):
        root5=Toplevel(self.master)
        asie=Asia(root5)

    def change_oceanie(self):
        root6=Toplevel(self.master)
        oceania=Oceanie(root6)

class NorthAmerica:
    
    def __init__(self, master):
    
        self.master=master
        self.master.resizable(0, 0)
        self.master.title("Amérique du Nord")       
        self.mappemonde = PhotoImage(file="amérique-nord123.png") 

        self.can1 = Canvas(self.master, height=1700, width=1200)
        self.can1.create_image(700, 400, image=self.mappemonde)      
        self.can1.pack()

        self.point = PhotoImage(file="point.png")
        self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
        self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)

class SouthAmerica:
    
    def __init__(self, master):
    
        self.master=master
        self.master.resizable(0, 0)
        self.master.title("Amérique du Nord")       
        self.mappemonde = PhotoImage(file="amérique-sud123.png") 

        self.can1 = Canvas(self.master, height=1700, width=1200)
        self.can1.create_image(700, 400, image=self.mappemonde)      
        self.can1.pack()

        self.point = PhotoImage(file="point.png")
        self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
        self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)

class Europe:
    
    def __init__(self, master):
    
        self.master=master
        self.master.resizable(0, 0)
        self.master.title("Europe")       
        self.mappemonde = PhotoImage(file="europe123.png") 

        self.can1 = Canvas(self.master, height=1700, width=1200)
        self.can1.create_image(700, 400, image=self.mappemonde)      
        self.can1.pack()

        self.point = PhotoImage(file="point.png")
        self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
        self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)

class Africa:
    
    def __init__(self, master):
    
        self.master=master
        self.master.resizable(0, 0)
        self.master.title("Afrique")       
        self.mappemonde = PhotoImage(file="africa123.png") 

        self.can1 = Canvas(self.master, height=1700, width=1200)
        self.can1.create_image(700, 400, image=self.mappemonde)      
        self.can1.pack()

        self.point = PhotoImage(file="point.png")
        self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
        self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)

class Asia:
    
    def __init__(self, master):
    
        self.master=master
        self.master.resizable(0, 0)
        self.master.title("Asie")       
        self.mappemonde = PhotoImage(file="asie123.png") 

        self.can1 = Canvas(self.master, height=1700, width=1200)
        self.can1.create_image(700, 400, image=self.mappemonde)      
        self.can1.pack()

        self.point = PhotoImage(file="point.png")
        self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
        self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)

class Oceanie:
    
    def __init__(self, master):
    
        self.master=master
        self.master.resizable(0, 0)
        self.master.title("Oceanie")       
        self.mappemonde = PhotoImage(file="oceanie123.png") 

        self.can1 = Canvas(self.master, height=1700, width=1200)
        self.can1.create_image(700, 400, image=self.mappemonde)      
        self.can1.pack()

        self.point = PhotoImage(file="point.png")
        self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
        self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)