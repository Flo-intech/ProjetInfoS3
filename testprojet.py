"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *
import tkinter as tk
class Carte(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #self.master.title("Popup menu")
        self.master.bind("<Button-1>", self.mouse_position)
    def texte(self):
        a = len(self.text)%19
    def mouse_position(self,e):
        self.x=e.x_root
        self.y=e.y_root
    def showMenuColombie(self):
        self.buttonMenu1.place(x=559,y=420)
        self.buttonMenu2.place(x=559,y=440)
        self.buttonMenu3.place(x=559,y=460)
        self.buttonMenu4.place(x=559,y=480)
        #pts = [(e,h/2),(w/2,h-e),(w-e,h/2),(w/2,e)]
        #self.can2.create_polygon(pts, dash=(4, 2), fill="magenta", outline="yellow", width=3)
        self.can2.place(x=458,y=420)
        self.text1.place(x=0,y=0)
        self.text2.place(x=0,y=20)
        self.text3.place(x=0,y=40)
        self.text4.place(x=0,y=60)
        self.text5.place(x=0,y=80)
    def showMenuJapon(self):
        self.buttonMenu1.place(x=1400,y=250)
        self.buttonMenu2.place(x=1400,y=270)
        self.buttonMenu3.place(x=1400,y=290)
        self.buttonMenu4.place(x=1400,y=310)
    def showMenuUsa(self):
        self.buttonMenu1.place(x=500,y=250)
        self.buttonMenu2.place(x=500,y=270)
        self.buttonMenu3.place(x=500,y=290)
        self.buttonMenu4.place(x=500,y=310)
    def showMenuFrance(self):
        self.buttonMenu1.place(x=875,y=225)
        self.buttonMenu2.place(x=875,y=245)
        self.buttonMenu3.place(x=875,y=265)
        self.buttonMenu4.place(x=875,y=285)
    def showMenuAlgerie(self):
        self.buttonMenu1.place(x=900,y=300)
        self.buttonMenu2.place(x=900,y=320)
        self.buttonMenu3.place(x=900,y=340)
        self.buttonMenu4.place(x=900,y=360)
    def showMenuAustralie(self):
        self.buttonMenu1.place(x=1380,y=550)
        self.buttonMenu2.place(x=1380,y=570)
        self.buttonMenu3.place(x=1380,y=590)
        self.buttonMenu4.place(x=1380,y=610)
    def onExit(self):

        self.quit()


def main():
    
    
    
    fenetre = Tk()
    can1 = Canvas(fenetre, height=1700, width=1400)
    can1.pack()

    #fenetre.geometry("720x480")

    # fenetre
    fenetre.title("Mapcompetition")
    fenetre.geometry("1920x1080")
    app = Carte()
    mappemonde = PhotoImage(file="BlankMap-World-v5.png")
    point = PhotoImage(file="point.png")
    pointColombie = Button(fenetre,command=app.showMenuColombie, image=point, height=15, width=15).place(x=559, y=420)
    pointJapon = Button(fenetre, image=point,command=app.showMenuJapon, height=15, width=15).place(x=1400, y=250)
    pointUsa = Button(fenetre, image=point,command=app.showMenuUsa, height=15, width=15).place(x=500, y=250)
    pointFrance = Button(fenetre, image=point,command=app.showMenuFrance, height=15, width=15).place(x=875, y=225)
    pointAlgerie = Button(fenetre, image=point,command=app.showMenuAlgerie, height=15, width=15).place(x=900, y=300)
    pointAustralie = Button(fenetre, image=point,command=app.showMenuAustralie, height=15, width=15).place(x=1380, y=550)



    can1.create_image(700, 400, image=mappemonde)
    app.buttonMenu1 = Button(fenetre,image=point, height=15, width=75, text="Match en direct")
    app.buttonMenu2 = Button(fenetre,image=point, height=15, width=75, text="Compétitions")
    app.buttonMenu3 = Button(fenetre,image=point, height=15, width=75, text="Equipes")
    app.buttonMenu4 = Button(fenetre,image=point, height=15, width=75, text="Catégories")
    app.can2=Canvas(fenetre,width=100,height=100)
    app.texte="Les sports les plus populaires sont en colombie le football, le baseball et le cyclisme"
    app.text1 = Label(app.can2,text="Les sports les plus")
    app.text2 = Label(app.can2,text="populaires en ")
    app.text3 = Label(app.can2,text="colombie sont le")
    app.text4 = Label(app.can2,text="football, le baseball")
    app.text5 = Label(app.can2,text="et le cyclisme.")
    fenetre.mainloop()
main()
# On crée une fenêtre, racine de notre interface
"""fenetre = Tk()
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



can1.create_image(700, 400, image=mappemonde)"""



# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
#fenetre.mainloop()
