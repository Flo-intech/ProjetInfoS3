"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *
import tkinter as tk
class Carte(Frame):

    def __init__(self):
        super().__init__()
        
        self.pays={"Colombie":[559,420],'Japon':[1400,250],'USA':[500,250],'France':[875,225],'Algerie':[900,300],'Australie':[1380,550]}
        self.text3={"Colombie":' Les sports les plus populaires en colombie sont le football, le baseball et le cyclisme. ','Japon':'de nombreux sports et arts martiaux japonais' ,'USA':'football  américain','France':'champion du monde de football en 1996 ','Algerie':'Le sport en Algérie le plus pratiqué et le plus populaire reste le football Le premier Algérien médaillé d\'or est El Ouafi Boughera en 1928 lors des jeux olympiques d\'Amsterdam au Marathon ','Australie':'moip' }
        self.text=[0,0,0,0,0,0]
        #self.buttonMenu1 = Button(fenetre, height=1, width=15, text="Match en direct")
        #self.buttonMenu2 = Button(fenetre,height=1, width=15, text="Compétitions")
        #self.buttonMenu3 = Button(fenetre,height=1, width=15, text="Equipes")
        #self.buttonMenu4 = Button(fenetre,height=1, width=15, text="Catégories")
        
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
            #print(i)
            #print(ab+"/")
            #print(aze)
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
        #print(self.text3["Colombie"])
        #print(self.pays["Colombie"][0])
        #if self.on:
            #self.text[1].config(x=45,y=59)
        #self.can2.forget_pack()
    def ShowMenu(self,pays):
        print('yo')
        print(pays)
        print(self.pays[pays][0])
        #self.point2[pays].forget_pack()
        for i in range (1,5) :
            print(i)
            self.buttonMenu[i].place(x=self.pays[pays][0],y=self.pays[pays][1]+20*(i-1))
            self.text2=self.text3[pays]
            self.texte()
        for i in range (1,6):
            if self.azer[i]:
                self.text[i].place(x=self.pays[pays][0]-120,y=self.pays[pays][1]+20*(i-1))
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
    


    can1.create_image(700, 400, image=mappemonde)
   
    app.buttonMenu1 = Button(fenetre, height=1, width=15, text="Match en direct")
    app.buttonMenu2 = Button(fenetre,height=1, width=15, text="Compétitions")
    app.buttonMenu3 = Button(fenetre,height=1, width=15, text="Equipes")
    app.buttonMenu4 = Button(fenetre,height=1, width=15, text="Catégories")
    app.buttonMenu=[0,app.buttonMenu1,app.buttonMenu2,app.buttonMenu3,app.buttonMenu4]
    #self.can2=Canvas(fenetre,width=100,height=100)
    #self.texte="Les sports les plus populaires sont en colombie le football, le baseball et le cyclisme"
    """self.text[1] = Label(self.can2,text="Les sports les plus")
    self.text[2] = Label(self.can2,text="populaires en ")
    self.text[3] = Label(self.can2,text="colombie sont le")
    self.text[4] = Label(self.can2,text="football, le baseball")
    self.text[5] = Label(self.can2,text="et le cyclisme.")"""
    textalgerie="Le sport en Algérie le plus pratiqué et le plus populaire reste le football."
    textalgerie2="Le premier Algérien médaillé d'or est El Ouafi Boughera en 1928 lors des jeux olympiques d'Amsterdam au Marathon"
    textfrance="champion du monde de football en 1996"
    textjapon="de nombreux sports et arts martiaux japonais"
    textusa="football  américain"
    #app.point2={'Colombie':0,'Japon':1,'USA':2,'France':0,'Algerie':0,'Australie':0}
    pointColombie = Button(fenetre,command= lambda: app.ShowMenu('Colombie'), image=point, height=15, width=15).place(x=559, y=420)
    pointJapon = Button(fenetre, image=point,command= lambda: app.ShowMenu('Japon'), height=15, width=15).place(x=1400, y=250)
    pointUSA = Button(fenetre, image=point,command=lambda: app.ShowMenu('USA'), height=15, width=15).place(x=500, y=250)
    pointFrance = Button(fenetre, image=point,command=lambda: app.ShowMenu('France'), height=15, width=15).place(x=875, y=225)
    pointAlgerie = Button(fenetre, image=point,command=lambda: app.ShowMenu('Algerie'), height=15, width=15).place(x=900, y=300)
    point2Australie = Button(fenetre, image=point,command=lambda: app.ShowMenu('Australie'), height=15, width=15).place(x=1380, y=550)

    fenetre.mainloop()

main()
# On crée une fenêtre, racine de notre interface
"""fenetre = Tk()
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



can1.create_image(700, 400, image=mappemonde)"""



# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre

