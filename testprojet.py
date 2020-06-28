"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""
#remplir les blancs par eq- la chose en question
#button a mettre en arrière-plan
# On importe Tkinter
from donnees_liste_joueurs_pays import * 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from functools import partial

class Carte(Frame):

    def __init__(self,fenetre):
        super().__init__()
        self.root=fenetre
        self.pays={"Colombie":[309,420],'Japon':[1150,250],'USA':[250,250],'France':[625,225],'Algérie':[630,330],'Australie':[1130,550]}
        self.text3={"Colombie":' Les sports les plus populaires en colombie sont le football et le baseball ','Japon':'Au japon de nombreux sports et arts martiaux dont le football ' ,'USA':'Aux USA Le football et le baseball ','France':'En france champion du monde de football en 1998 et handball en 1970,1981,1989,2001,2017 ','Algérie':'Le sport en Algérie le plus pratiqué et le plus populaire reste le football ','Australie':'de nombreux sports existent en australie dont le football ' }
        self.sportsPays={"Colombie":['football','baseball'],"USA":['baseball','basketball'],"France":["football","handball"],"Algérie":["football"],"Australie":["football"],"Japon":["football"]}
        self.couleur={"football":"blue","baseball":"red"}
        self.liste_joueurs_pays=liste_joueurss() 
        #print(self.liste_role)
        self.selected_sports_pays={}
        for i in self.sportsPays:
            z={}
            for j in self.sportsPays[i]:
                z.update({j:False})
            self.selected_sports_pays.update({i:z})
        print(self.selected_sports_pays)
        self.text=[0,0,0,0,0,0]
        self.list_label=[]
        
        
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
    
    def selection(self):
            if self.selected_sports_pays[self.paysActuel]["baseball"]:
                self.bouton_sports_colombie[1].config(background='white')
            else :
                self.bouton_sports_colombie[1].config(background=self.couleur["baseball"])
            if self.selected_sports_pays[self.paysActuel]["football"]:
                self.bouton_sports_colombie[0].config(background='white')
            else :
                self.bouton_sports_colombie[0].config(background=self.couleur["football"])

    def competition(self):
        self.ligne=True
        a=0
        c=1
        g=1
        height=len(self.competition_football)
        for i in range(1,height+1): #Rows
                
                try :
                    self.list_label[a].config(text=self.competition_football[a])

                except:
                    if len(self.list_label)% 23==0 : #and self.ligne:
                        self.ligne=False
                        g=g+1
                        c=2
                    b = Label(self.new, text=self.competition_football[a])
                    self.list_label.append(b)
                    b.grid(row=c, column=g) 
                a=a+1
                c=c+1
    def rec(self,menu):
        if isinstance (menu,list):
            for k in menu:
                self.rec(k)
        elif isinstance (menu,dict):
            for l in menu:
                if l ==self.sport_Actuel or l in self.liste_joueurs_pays[self.paysActuel][self.sport_Actuel]:
                    self.a=True
                else :
                    self.a=False
                if self.a:
                    self.liste_role[self.g]=l
                    self.g=self.g+1
                    print("*"+l)
                print ("//"+l)
                self.rec(menu[l])
        else:
            print("/"+menu)
    def show():

        tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
        tempList.sort(key=lambda e: e[1], reverse=True)

        for i, (name, score) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(i, name, score))

 
        #label = tk.Label(scores, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
        # create Treeview with 3 columns
        #cols = ('Position', 'Name', 'Role')
        #listBox = ttk.Treeview(scores, columns=cols, show='headings')
        # set column headings
        #for col in cols:
         #   listBox.heading(col, text=col)    
        #listBox.grid(row=1, column=0, columnspan=2)

        #showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
        #closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)
    def equipe(self,sportss):
        width = 5
        a=0
        print(sportss)
        if sportss=="football":
            #self.p.add(self.bouton_sports_colombie[3])
            #self.p.grid()
            
            #self.p.grid()
            self.selected_sports_pays[self.paysActuel]["football"]=True
            self.selected_sports_pays[self.paysActuel]["baseball"]=False
            self.selection()
            height = len(self.liste_joueurs_pays[self.paysActuel][sportss])
            for i in range(1,height+1): #Rows
                
            #for j in range(width): #Columns
                #b = Label(self.new, text=liste_joueurs[a])
                
                
                try :
                    self.list_label[a].config(text=self.liste_joueurs_pays[self.paysActuel][sportss][a])
                    #print('yo')
                except:
                    #print(self.list_label)
                    #print('yo2')
                    b = Label(self.new, text=self.liste_joueurs_pays[self.paysActuel][sportss][a])
                    self.list_label.append(b)
                    b.grid(row=i, column=1) 
                a=a+1
        else :
            
            self.selected_sports_pays[self.paysActuel]["baseball"]=True
            self.selected_sports_pays[self.paysActuel]["football"]=False
            self.selection()
            height = len(liste_joueurs_baseball["Pitchers"])
            #self.b.forget_grid()
            for i in range(1,height+1): #Rows
                #self.b.config(text=liste_joueurs_baseball["Pitchers"][a])
            #for j in range(width): #Columns
                #b = Label(self.new, text=liste_joueurs_baseball["Pitchers"][a])
                #b.focus_set()
                #b.grid(row=i, column=1)
                
                try:
                    self.list_label[a].config(text=liste_joueurs_baseball["Pitchers"][a])
                    #print('yo')
                except:
                    #print('yo2')
                    b = Label(self.new, text=liste_joueurs_baseball["Pitchers"][a])
                    self.list_label.append(b)
                    b.grid(row=i, column=1)
                a=a+1
            for i in range (height,len(self.list_label)):
                self.list_label[i].config(text="")
        if self.selected_sports_pays[self.paysActuel]["football"]:
            self.bouton_sports_colombie[2].grid(row=0,column=2)
        else :
            self.bouton_sports_colombie[2].grid_forget()
    def Sports(self,sports):
        #sport=self.sportsPays[self.paysActuel][sport]
        #self.selected_Colombie[sport]=True
        #for i in self.sportsPays[self.paysActuel]:
         #   if i != sport:
          #      self.selected_Colombie[i]=False
        try:
            if self.new.state() == "normal":
                self.new.focus()
        except:
            self.new = tk.Toplevel(self.root)
        self.new.geometry('500x500')
        #self.p = PanedWindow(self.new)
        #couleur=['blue','red','green']
        #j=0
        #sport=["football","baseball","cyclisme"]
        #self.p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
        #self.bouton_sports_colombie=[Button(self.new, text=self.sportsPays['Colombie'][0], background=couleur[0], anchor=CENTER,command= lambda : self.equipe(sport[0])),
        #Button(self.new, text=self.sportsPays['Colombie'][1], background=couleur[1], anchor=CENTER,command= lambda : self.equipe(sport[1])),
        #Button(self.new, text=self.sportsPays['Colombie'][2], background=couleur[2], anchor=CENTER,command= lambda : self.equipe(sport[2])),
        #Button(self.new, text='mondial de foot des -20 ans', background='yellow', anchor=CENTER,command= self.competition)]
        #self.bouton_sports_colombie[0].grid(row=0,column=0)
        #self.bouton_sports_colombie[1].grid(row=0,column=1)
        self.sport_Actuel=sports
        self.a=False
        self.g=0
        self.liste_role=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.rec(self.liste_joueurs_pays[self.paysActuel])
        self.liste_role[0]=0
        #self.liste_role[1]=0
        label = tk.Label(self.new, text=sports+"'s team of "+self.paysActuel, font=("Arial",30)).grid(row=0, columnspan=3)
        #create Treeview with 3 columns
        cols = ('Position', 'Name', 'Role')
        listBox = ttk.Treeview(self.new, columns=cols, show='headings')
        # set column headings
        for col in cols:
            listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)
        for i in self.liste_role:
            if i !=0:
                for j in self.liste_joueurs_pays[self.paysActuel][self.sport_Actuel][i]:
                    h=j.split()
                    listBox.insert("", "end", values=(h[0],h[1], i)) 
        self.bouton_sports_pays=[Button(self.new, text="Close", width=15),
        Button(self.new, text="Close", width=15),
        Button(self.new, text="Close", width=15)]        
        for i in range (0,len(self.sportsPays[self.paysActuel])):
            self.bouton_sports_pays[i].config(text=self.sportsPays[self.paysActuel][i],command =self.Callback(self.buttonMenu[i]))
            self.bouton_sports_pays[i].grid(row=4,column=i)
        #showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
        #closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)
        #self.equipe(sports)
    def Callback(self,button):
        return lambda: self.Sports(button["text"])
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
        liste=[False,False]
        self.paysActuel=pays
        self.liste=[]
        for i in range (0,len(self.sportsPays[pays])):
            #self.buttonMenu1 = Button(fenetre, height=1, width=15, text="Match en direct")
            #self.buttonMenu.append(self.buttonMenu1)
            #print(self.buttonMenu[i])
            self.buttonMenu[i].config(text=self.sportsPays[pays][i],command =self.Callback(self.buttonMenu[i]))
            #self.buttonMenu[i].bind("<Button-1>", self.Sports(self.sportsPays[pays][i]))
            
        #self.point2[pays].forget_pack()
        self.text2=self.text3[pays]
        self.texte()
        for i in range (0,len(self.sportsPays[pays])) :
            liste[i]=True
            self.buttonMenu[i].place(x=self.pays[pays][0],y=self.pays[pays][1]+20*(i))
        for i in range (len(self.sportsPays[pays]),len(liste)):
            self.buttonMenu[i].place_forget() 
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
    app = Carte(fenetre)
    
    app.on=False
    mappemonde = PhotoImage(file="BlankMap-World-v5.png")
    point = PhotoImage(file="point.png")
    


    can1.create_image(700, 400, image=mappemonde)
    #app.menu_widget = Menu(fenetre)
    app.buttonMenu1 = Button(fenetre, height=1, width=15, text="Match en direct")#,command= )
    app.buttonMenu2 = Button(fenetre,height=1, width=15, text="Compétitions")#,command= )
    app.buttonMenu3 = Button(fenetre,height=1, width=15, text="Equipes")#,command= )
    app.buttonMenu4 = Button(fenetre,height=1, width=15, text="yo")#,command= app.Sports)
    app.buttonMenu=[app.buttonMenu1,app.buttonMenu2,app.buttonMenu3,app.buttonMenu4]
    textalgerie="Le sport en Algérie le plus pratiqué et le plus populaire reste le football."
    textalgerie2="Le premier Algérien médaillé d'or est El Ouafi Boughera en 1928 lors des jeux olympiques d'Amsterdam au Marathon"
    textfrance="champion du monde de football en 1996"
    textjapon="de nombreux sports et arts martiaux japonais"
    textusa="football  américain"
    #app.point2={'Colombie':0,'Japon':1,'USA':2,'France':0,'Algerie':0,'Australie':0}
    pointColombie = Button(fenetre,command= lambda: app.ShowMenu('Colombie'), image=point, height=15, width=15).place(x=309, y=420)
    pointJapon = Button(fenetre, image=point,command= lambda: app.ShowMenu('Japon'), height=15, width=15).place(x=1150, y=250)
    pointUSA = Button(fenetre, image=point,command=lambda: app.ShowMenu('USA'), height=15, width=15).place(x=250, y=250)
    pointFrance = Button(fenetre, image=point,command=lambda: app.ShowMenu('France'), height=15, width=15).place(x=625, y=225)
    pointAlgerie = Button(fenetre, image=point,command=lambda: app.ShowMenu('Algérie'), height=15, width=15).place(x=630, y=330)
    point2Australie = Button(fenetre, image=point,command=lambda: app.ShowMenu('Australie'), height=15, width=15).place(x=1130, y=550)

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