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

        a = len(self.text2)%19
        b=(len(self.text2)-a)/19
        de=0
        self.azer=[0,0,0,0,0,0]
        for i in range(1,6) :
            f=0
            ab=""
            da = i*19
            try :
                self.text2[da-f]
            except :
                print('yo')
                da=len(self.text2)-1
            while self.text2[da-f] != " ": 
                f=f+1
            for j in range((i-1)*19-de,da-f):
                if j ==(i-1)*19-de:
                    if self.text2[j]==" ":
                        aze=45
                    else :  
                        ab=ab+self.text2[j]
                        aze=16
                else :
                    ab=ab+self.text2[j]

            

            de=f
            print(i)
            print(ab+"/")
            print(aze)
            if self.on :
                if i != 0:
                        self.text[i].config(text=ab)
                        if ab != "" :   
                            self.azer[i]=True
                        else :
                            self.azer[i]=False
            else :
                
                self.text[i]=(Label(self.master,text=ab))
                if ab != ""  :  
                    self.azer[i]=True
                else :
                    self.azer[i]=False
            
            print(b)
        self.on=True

    def mouse_position(self,e):
        self.x=e.x_root
        self.y=e.y_root
        #if self.on:
            #self.text[1].config(x=45,y=59)
        #self.can2.forget_pack()
    def showMenuColombie(self):
        self.buttonMenu1.place(x=559,y=420)
        self.buttonMenu2.place(x=559,y=440)
        self.buttonMenu3.place(x=559,y=460)
        self.buttonMenu4.place(x=559,y=480)
        self.text2=" Les sports les plus populaires en colombie sont le football, le baseball et le cyclisme. "
        #self.text="Le sport en Algérie le plus pratiqué et le plus populaire reste le football Le premier Algérien médaillé d'or est El Ouafi Boughera en 1928 lors des jeux olympiques d'Amsterdam au Marathon"
        if self.on :
            for i in range (1,5):
                print('yo')
                #self.text[i].forget_pack
        self.texte()
        #self.can2.place(x=458,y=420)
        for i in range (1,5):
            if self.azer[i]:
                self.text[i].place(x=440,y=420+(i-1)*20)
        #self.text[2].place(x=440,y=440)
        #self.text[3].place(x=440,y=460)
        #self.text[4].place(x=440,y=480)
        #self.text[5].place(x=440,y=500)
    def showMenuJapon(self):
        self.buttonMenu1.place(x=1400,y=250)
        self.buttonMenu2.place(x=1400,y=270)
        self.buttonMenu3.place(x=1400,y=290)
        self.buttonMenu4.place(x=1400,y=310)
        self.text2="de nombreux sports et arts martiaux japonais "
        if self.on :
            for i in range (1,5):
                print('yo')
                #self.text[i].config(x=1000,y=590)
                #self.text[i].forget_pack
        self.texte()
        #self.can2.place(x=458,y=420)
        for i in range (1,5):
            if self.azer[i]:
                self.text[i].place(x=1280,y=250+(i-1)*20)
        #self.text[1].place(x=1280,y=250)
        #self.text[2].place(x=1280,y=270)
        #self.text[3].place(x=1280,y=290)
        #self.text[4].place(x=1280,y=310)
        #self.text[5].place(x=1280,y=330)
    def showMenuUsa(self):
        self.buttonMenu1.place(x=500,y=250)
        self.buttonMenu2.place(x=500,y=270)
        self.buttonMenu3.place(x=500,y=290)
        self.buttonMenu4.place(x=500,y=310)
        self.text2="football  américain"
        if self.on :
            for i in range (1,5):
                print('yo')
                #self.text[i].config(x=1000,y=590)
                #self.text[i].forget_pack
        self.texte()
        #self.can2.place(x=458,y=420)
        for i in range (1,5):
            if self.azer[i]:
                self.text[i].place(x=380,y=250+(i-1)*20)
        #self.text[1].place(x=380,y=250)
        #self.text[2].place(x=380,y=270)
        #self.text[3].place(x=380,y=290)
        #self.text[4].place(x=380,y=310)
        #self.text[5].place(x=380,y=330)
    def showMenuFrance(self):
        self.buttonMenu1.place(x=875,y=225)
        self.buttonMenu2.place(x=875,y=245)
        self.buttonMenu3.place(x=875,y=265)
        self.buttonMenu4.place(x=875,y=285)
        self.text2="champion du monde de football en 1996 "
        if self.on :
            for i in range (1,5):
                print('yo')
                #self.text[i].config(x=1000,y=590)
                #self.text[i].forget_pack
        self.texte()
        #self.can2.place(x=458,y=420)
        for i in range (1,5):
            if self.azer[i]:
                self.text[i].place(x=755,y=225+(i-1)*20)
        #self.text[1].place(x=755,y=225)
        #self.text[2].place(x=755,y=245)
        #self.text[3].place(x=755,y=265)
        #self.text[4].place(x=755,y=285)
        #self.text[5].place(x=755,y=305)
    def showMenuAlgerie(self):
        self.text2="Le sport en Algérie le plus pratiqué et le plus populaire reste le football Le premier Algérien médaillé d'or est El Ouafi Boughera en 1928 lors des jeux olympiques d'Amsterdam au Marathon "
        self.texte()
        self.buttonMenu1.place(x=900,y=300)
        self.buttonMenu2.place(x=900,y=320)
        self.buttonMenu3.place(x=900,y=340)
        self.buttonMenu4.place(x=900,y=360)
        self.text2="mouais "
        if self.on :
            for i in range (1,5):
                print('yo')
                #self.text[i].config(x=1000,y=590)
                #self.text[i].forget_pack
        self.texte()
        #self.can2.place(x=458,y=420)
        for i in range (1,5):
            if self.azer[i]:
                self.text[i].place(x=780,y=300+(i-1)*20)
        #self.text[1].place(x=780,y=300)
        #self.text[2].place(x=780,y=320)
        #self.text[3].place(x=780,y=340)
        #self.text[4].place(x=780,y=360)
        #self.text[5].place(x=780,y=380)
    def showMenuAustralie(self):
        self.buttonMenu1.place(x=1380,y=550)
        self.buttonMenu2.place(x=1380,y=570)
        self.buttonMenu3.place(x=1380,y=590)
        self.buttonMenu4.place(x=1380,y=610)
        self.text2="moip "
        if self.on :
            for i in range (1,5):
                print('yo')
                #self.text[i].config(x=1000,y=590)
                #self.text[i].forget_pack
        self.texte()
        #self.can2.place(x=458,y=420)
        for i in range (1,5):
            if self.azer[i]:
                self.text[i].place(x=1260,y=550+(i-1)*20)
        #self.text[1].place(x=1260,y=550)
        #self.text[2].place(x=1260,y=570)
        #self.text[3].place(x=1260,y=590)
        #self.text[4].place(x=1260,y=610)
        #self.text[5].place(x=1260,y=630)
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
    app.on=False
    mappemonde = PhotoImage(file="BlankMap-World-v5.png")
    point = PhotoImage(file="point.png")
    pointColombie = Button(fenetre,command=app.showMenuColombie, image=point, height=15, width=15).place(x=559, y=420)
    pointJapon = Button(fenetre, image=point,command=app.showMenuJapon, height=15, width=15).place(x=1400, y=250)
    pointUsa = Button(fenetre, image=point,command=app.showMenuUsa, height=15, width=15).place(x=500, y=250)
    pointFrance = Button(fenetre, image=point,command=app.showMenuFrance, height=15, width=15).place(x=875, y=225)
    pointAlgerie = Button(fenetre, image=point,command=app.showMenuAlgerie, height=15, width=15).place(x=900, y=300)
    pointAustralie = Button(fenetre, image=point,command=app.showMenuAustralie, height=15, width=15).place(x=1380, y=550)



    can1.create_image(700, 400, image=mappemonde)
    app.buttonMenu1 = Button(fenetre, height=1, width=15, text="Match en direct")
    app.buttonMenu2 = Button(fenetre,height=1, width=15, text="Compétitions")
    app.buttonMenu3 = Button(fenetre,height=1, width=15, text="Equipes")
    app.buttonMenu4 = Button(fenetre,height=1, width=15, text="Catégories")
    #app.can2=Canvas(fenetre,width=100,height=100)
    #app.texte="Les sports les plus populaires sont en colombie le football, le baseball et le cyclisme"
    app.text=[0,0,0,0,0,0]
    """app.text[1] = Label(app.can2,text="Les sports les plus")
    app.text[2] = Label(app.can2,text="populaires en ")
    app.text[3] = Label(app.can2,text="colombie sont le")
    app.text[4] = Label(app.can2,text="football, le baseball")
    app.text[5] = Label(app.can2,text="et le cyclisme.")"""
    textalgerie="Le sport en Algérie le plus pratiqué et le plus populaire reste le football."
    textalgerie2="Le premier Algérien médaillé d'or est El Ouafi Boughera en 1928 lors des jeux olympiques d'Amsterdam au Marathon"
    textfrance="champion du monde de football en 1996"
    textjapon="de nombreux sports et arts martiaux japonais"
    textusa="football  américain"
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
