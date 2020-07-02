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
import math
class Pays:

    def __init__(self,position,nom,description,sport):
        self.position=position
        self.nom=nom
        self.description=description
        self.sport=sport
class Sport:

    def __init__(self,equipe,competition,nom):
        self.equipe=equipe
        self.competition=competition
        self.nom=nom
"""class Mappemonde:
    
    def __init__(self, master):
    
        self.master=master
        self.master.geometry("1920x1080")
        self.master.title("Mapcompetition")       
        self.mappemonde = PhotoImage(file="BlankMap-World-v5.png") 

        self.can1 = Canvas(self.master, height=1700, width=1400)
        self.can1.create_image(700, 400, image=self.mappemonde)      
        self.can1.pack()

        #self.point = PhotoImage(file="point.png")
        #self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
        #self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)
        #self.pointUsa = Button(self.master, image=self.point, height=15, width=15).place(x=500, y=250)
        #self.pointFrance = Button(self.master, image=self.point, height=15, width=15).place(x=875, y=225)
        #self.can1pointAlgerie = Button(self.master, image=self.point, height=15, width=15).place(x=900, y=300)
        #self.pointAustralie = Button(self.master, image=self.point, height=15, width=15).place(x=1380, y=550)
	    pointColombie = Button(self.master,command= lambda: app.ShowMenu('Colombie'), image=point, height=15, width=15).place(x=309, y=420)
    	pointJapon = Button(self.master, image=point,command= lambda: app.ShowMenu('Japon'), height=15, width=15).place(x=1150, y=250)
    	pointUSA = Button(self.master, image=point,command=lambda: app.ShowMenu('USA'), height=15, width=15).place(x=250, y=250)
    	pointFrance = Button(self.master, image=point,command=lambda: app.ShowMenu('France'), height=15, width=15).place(x=625, y=225)
    	pointAlgerie = Button(self.master, image=point,command=lambda: app.ShowMenu('Algérie'), height=15, width=15).place(x=630, y=330)
    	pointAustralie = Button(self.master, image=point,command=lambda: app.ShowMenu('Australie'), height=15, width=15).place(x=1130, y=550)"""
class Carte:

    def __init__(self,master):
        super().__init__()
        #self.root=fenetre
        self.compet=False
        self.liste_pays={}
        self.liste_pays["Colombie"]=Pays([309,420],
        "Colombie",
        "Les sports les plus populaires en colombie sont le football et le baseball ",
        ['football','baseball'])

        self.liste_pays["Japon"]=Pays([1150,250],
        "Japon",
        "Au japon de nombreux sports et arts martiaux dont le football",
        ["football"])
        self.liste_pays["USA"]=Pays([250,250],
        "USA",
        'Aux USA Le football et le baseball ',
        ['baseball','basketball'])
        self.liste_pays["France"]=Pays([625,225],
        "France",
        'En france champion du monde de football en 1998 et handball en 1970,1981,1989,2001,2017 ',
        ["football","handball"])
        self.liste_pays["Algérie"]=Pays([630,330],
        "Algérie",
        'Le sport en Algérie le plus pratiqué et le plus populaire reste le football ',
        ["football"])
        self.liste_pays["Australie"]=Pays([1130,550],
        "Australie",
        'de nombreux sports existent en australie dont le football ',
        ["football"])
        self.liste_joueurs_pays=liste_joueurss()
        for i in self.liste_pays:
            for j in range(0,len(self.liste_pays[i].sport)):
                self.liste_pays[i].sport[j]=Sport(self.liste_joueurs_pays[self.liste_pays[i].nom][self.liste_pays[i].sport[j]],self.liste_joueurs_pays[self.liste_pays[i].nom]["competition_"+self.liste_pays[i].sport[j]],self.liste_pays[i].sport[j]) 
                print(self.liste_pays[i].sport)
        #print(self.liste_role)
        self.selected_sports_pays={}
        for i in self.liste_pays:
            z={}
            for j in self.liste_pays[i].sport:
                z.update({j:False})
            self.selected_sports_pays.update({i:z})
        print(self.selected_sports_pays)
        self.text=[0,0,0,0,0,0]
        self.list_label=[]
        #self.initUI()
        self.master=master
        self.master.geometry("1920x1080")
        self.master.title("Mapcompetition")       
        self.mappemonde = PhotoImage(file="BlankMap-World-v5.png") 

        self.can1 = Canvas(self.master, height=1700, width=1400)
        self.can1.create_image(700, 400, image=self.mappemonde)      
        self.can1.pack()

        self.point = PhotoImage(file="point.png")
        #self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
        #self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)
        #self.pointUsa = Button(self.master, image=self.point, height=15, width=15).place(x=500, y=250)
        #self.pointFrance = Button(self.master, image=self.point, height=15, width=15).place(x=875, y=225)
        #self.can1pointAlgerie = Button(self.master, image=self.point, height=15, width=15).place(x=900, y=300)
        #self.pointAustralie = Button(self.master, image=self.point, height=15, width=15).place(x=1380, y=550)
        pointColombie = Button(self.master,command= lambda: self.ShowMenu('Colombie'), image=self.point, height=15, width=15).place(x=309, y=420)
        pointJapon = Button(self.master, image=self.point,command= lambda: self.ShowMenu('Japon'), height=15, width=15).place(x=1150, y=250)
        pointUSA = Button(self.master, image=self.point,command=lambda: self.ShowMenu('USA'), height=15, width=15).place(x=250, y=250)
        pointFrance = Button(self.master, image=self.point,command=lambda: self.ShowMenu('France'), height=15, width=15).place(x=625, y=225)
        pointAlgerie = Button(self.master, image=self.point,command=lambda: self.ShowMenu('Algérie'), height=15, width=15).place(x=630, y=330)
        pointAustralie = Button(self.master, image=self.point,command=lambda: self.ShowMenu('Australie'), height=15, width=15).place(x=1130, y=550)
        self.buttonMenu1 = Button(self.master, height=1, width=15, text="Match en direct")#,command= )
        self.buttonMenu2 = Button(self.master,height=1, width=15, text="Compétitions")#,command= )
        self.buttonMenu3 = Button(self.master,height=1, width=15, text="Equipes")#,command= )
        self.buttonMenu4 = Button(self.master,height=1, width=15, text="yo")#,command= app.Sports)
        self.buttonMenu=[self.buttonMenu1,self.buttonMenu2,self.buttonMenu3,self.buttonMenu4]


    """def initUI(self):

        #self.master.title("Popup menu")
        self.master.bind("<Button-1>", self.mouse_position)"""
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
            if self.selected_sports_pays[self.paysActuel.nom]["baseball"]:
                self.bouton_sports_colombie[1].config(background='white')
            else :
                self.bouton_sports_colombie[1].config(background=self.couleur["baseball"])
            if self.selected_sports_pays[self.paysActuel.nom]["football"]:
                self.bouton_sports_colombie[0].config(background='white')
            else :
                self.bouton_sports_colombie[0].config(background=self.couleur["football"])

    def rec(self,menu):
        if isinstance (menu,list):
            for k in menu:
                self.rec(k)
        elif isinstance (menu,dict):
            for l in menu:
                if l ==self.sport_Actuel or l in self.liste_joueurs_pays[self.paysActuel.nom][self.sport_Actuel]:
                    self.a=True
                else :
                    self.a=False
                if self.a:
                    self.liste_role[self.g]=l
                    self.g=self.g+1
                    print("*"+str(l))
                print ("//"+str(l))
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
            self.selected_sports_pays[self.paysActuel.nom]["football"]=True
            self.selected_sports_pays[self.paysActuel.nom]["baseball"]=False
            self.selection()
            height = len(self.liste_joueurs_pays[self.paysActuel.nom][sportss])
            for i in range(1,height+1): #Rows
                
            #for j in range(width): #Columns
                #b = Label(self.new, text=liste_joueurs[a])
                
                
                try :
                    self.list_label[a].config(text=self.liste_joueurs_pays[self.paysActuel.nom][sportss][a])
                    #print('yo')
                except:
                    #print(self.list_label)
                    #print('yo2')
                    b = Label(self.new, text=self.liste_joueurs_pays[self.paysActuel.nom][sportss][a])
                    self.list_label.append(b)
                    b.grid(row=i, column=1) 
                a=a+1
        else :
            
            self.selected_sports_pays[self.paysActuel.nom]["baseball"]=True
            self.selected_sports_pays[self.paysActuel.nom]["football"]=False
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
        if self.selected_sports_pays[self.paysActuel.nom]["football"]:
            self.bouton_sports_colombie[2].grid(row=0,column=2)
        else :
            self.bouton_sports_colombie[2].grid_forget()
    def show_competition(self):
        liste=["Huitièmes de finale","Quarts de finale", "Demi-finales","Finale"]
        self.compet=True
        image_n=PhotoImage(file="carre_noir.png")
        a=0
        b=0
        c=-1
        liste_label_rang={}
        liste_label=[]
        liste_label_dim=[]
        self.liste_label_noir=[]
        self.liste_label_to_forget=[]
        self.listBox.grid_forget()
        self.titre_label.grid_forget()
        for i in self.liste_boutons_competitions:
            i.grid_forget()
        for j in self.bouton_sports_pays:
            j.grid_forget()
        for i in range (0,len(self.paysActuel.sport)):
            print("***")
            b=b+1
            self.bouton_sports_pays[i].config(text=self.paysActuel.sport[i].nom,command =self.Callback(self.buttonMenu[i]))
            self.bouton_sports_pays[i].place(x=b*150,y=0)
        for i in liste:
            liste_label=[]
            liste_label_dim=[]
            c=c+1
            e=0
            h=0
            d=[0,1,3,10]
            g=[1,4,11,0]
            f=g[c]
            a=d[c]
            for j in self.competition2[i]:
                e=e+1
                h=h+1
                if h%3==0:
                    h=h+1
                    e=e+f
                liste_label.append((100*c,(a+e)*20))
                label=Label(self.new,text=j,anchor='w')
                label.place(x=100*c,y=(a+e)*20)
                self.liste_label_to_forget.append(label)
                label.update()
                hauteur=label.winfo_height()
                largeur=label.winfo_width()
                liste_label_dim.append((largeur,hauteur))
                print(str(liste_label_dim)+str(liste_label))
            liste_label_rang[i]=[liste_label,liste_label_dim]
        #Button(self.new,text="yo2",background='red').place(x=250,y=250)
        #Button(self.new,text="yo3",background="yellow").place(x=0,y=0)
        #place 
        #100=30
        #print(liste_label)
        def Path(a,z,e,ra):
            if max(e,z)==e:
                    lm=9
                    aj=0
            else :
                    aj=3
                    lm=-9
            for i in range (0,round((ra-a)/36)):
                aa=Label(self.new,background='black',image=image_n,width=5,height=5)
                aa.place(x=a+i*9,y=z)#(9,9)
                self.liste_label_noir.append(aa)
            for j in range (0,round((max(e,z)-min(e,z))/9)+aj):
                ab=Label(self.new,background='black',image=image_n,width=5,height=5)
                ab.place(x=a+i*9,y=z+j*lm)
                self.liste_label_noir.append(ab)
            for r in range (i,i+round((ra-a)/36)):
                ac=Label(self.new,background='black',image=image_n,width=5,height=5)
                ac.place(x=a+r*9,y=z+j*lm)#(9,9)
                self.liste_label_noir.append(ac)
        for l in range (0,len(liste)-1):
            for i in range (0,len(self.competition2[liste[l]])-1,2):
                g=self.competition2[liste[l]][i]
                h=self.competition2[liste[l]][i+1]
                g=g.split()
                h=h.split()
                print(g)
                print(h)
                if int(g[1])>int(h[1]):#1=liste_label_dim #0=liste_label
                    print("****"+str(int(i/2)))
                    pos_depart_x=liste_label_rang[liste[l]][0][i][0]+liste_label_rang[liste[l]][1][i][0]
                    pos_depart_y=liste_label_rang[liste[l]][0][i][1]+math.floor(liste_label_rang[liste[l]][1][i][1]/2)
                    pos_fin_y=liste_label_rang[liste[l+1]][0][int(i/2)][1]+liste_label_rang[liste[l+1]][1][int(i/2)][1]
                    pos_fin_x=liste_label_rang[liste[l+1]][0][int(i/2)][0]+liste_label_rang[liste[l+1]][1][int(i/2)][0]
                    print(pos_depart_x,pos_depart_y,pos_fin_y,pos_fin_x)
                    Path(pos_depart_x,pos_depart_y,pos_fin_y,pos_fin_x)
                elif int(g[1])==int(h[1]):
                    if int(g[2])>int(h[2]):#1=liste_label_dim #0=liste_label
                        print("****"+str(int(i/2)))
                        pos_depart_x=liste_label_rang[liste[l]][0][i][0]+liste_label_rang[liste[l]][1][i][0]
                        pos_depart_y=liste_label_rang[liste[l]][0][i][1]+math.floor(liste_label_rang[liste[l]][1][i][1]/2)
                        pos_fin_y=liste_label_rang[liste[l+1]][0][int(i/2)][1]+liste_label_rang[liste[l+1]][1][int(i/2)][1]
                        pos_fin_x=liste_label_rang[liste[l+1]][0][int(i/2)][0]+liste_label_rang[liste[l+1]][1][int(i/2)][0]
                        print(pos_depart_x,pos_depart_y,pos_fin_y,pos_fin_x)
                        Path(pos_depart_x,pos_depart_y,pos_fin_y,pos_fin_x)
                    else :
                        pos_depart_x=liste_label_rang[liste[l]][0][i+1][0]+liste_label_rang[liste[l]][1][i+1][0]
                        pos_depart_y=liste_label_rang[liste[l]][0][i+1][1]+math.floor(liste_label_rang[liste[l]][1][i+1][1]/2)
                        pos_fin_y=liste_label_rang[liste[l+1]][0][int((i+1)/2)][1]+liste_label_rang[liste[l+1]][1][int((i+1)/2)][1]
                        #print(self.competition2[liste[1]][int((i+1)/2)])
                        pos_fin_x=liste_label_rang[liste[l+1]][0][int(i/2)][0]+liste_label_rang[liste[l+1]][1][int(i/2)][0]
                        print(pos_depart_x,pos_depart_y,pos_fin_y,pos_fin_x)
                        Path(pos_depart_x,pos_depart_y,pos_fin_y,pos_fin_x)

                else :
                    pos_depart_x=liste_label_rang[liste[l]][0][i+1][0]+liste_label_rang[liste[l]][1][i+1][0]
                    pos_depart_y=liste_label_rang[liste[l]][0][i+1][1]+math.floor(liste_label_rang[liste[l]][1][i+1][1]/2)
                    pos_fin_y=liste_label_rang[liste[l+1]][0][int((i+1)/2)][1]+liste_label_rang[liste[l+1]][1][int((i+1)/2)][1]
                    #print(self.competition2[liste[1]][int((i+1)/2)])
                    pos_fin_x=liste_label_rang[liste[l+1]][0][int(i/2)][0]+liste_label_rang[liste[l+1]][1][int(i/2)][0]
                    #print(pos_depart_x,pos_depart_y,pos_fin_y,pos_fin_x)
                    Path(pos_depart_x,pos_depart_y,pos_fin_y,pos_fin_x)
            
    def Sports(self,sports):
        try :
            self.titre_label.grid_forget()
        except:
            yo=0
        if self.compet:
            self.compet=False
            for i in self.liste_label_to_forget:
                i.place_forget()
            for j in self.liste_label_noir:
                j.place_forget()

        #sport=self.sportsPays[self.paysActuel][sport]
        #self.selected_Colombie[sport]=True
        #for i in self.sportsPays[self.paysActuel]:
         #   if i != sport:
          #      self.selected_Colombie[i]=False
        try:
            if self.new.state() == "normal":
                self.new.focus()
        except:
            self.new = tk.Toplevel(self.master)
        self.new.geometry('500x500')
        self.sport_Actuel=sports
        self.a=False
        self.g=0
        self.liste_role=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.rec(self.liste_joueurs_pays[self.paysActuel.nom])
        self.liste_role[0]=0
        ad=0
        #self.liste_role[1]=0
        print("*"+sports+"*")
        self.titre_label = Label(self.new, text=sports+"'s team of "+self.paysActuel.nom, font=("Arial",30))
        self.titre_label.grid(row=0, columnspan=3)
        #create Treeview with 3 columns
        cols = ('Position', 'Name', 'Role')
        self.listBox = ttk.Treeview(self.new, columns=cols, show='headings')
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)    
        self.listBox.grid(row=1, column=0, columnspan=4)
        for i in self.liste_role:
            if i !=0:
                for j in self.liste_joueurs_pays[self.paysActuel.nom][self.sport_Actuel][i]:
                    h=j.split()
                    self.listBox.insert("", "end", values=(h[0],h[1], i)) 
        self.liste_boutons_competitions=[Button(self.new),Button(self.new),Button(self.new),Button(self.new)]
        self.bouton_sports_pays=[Button(self.new, text="Close"),
        Button(self.new, text="Close"),
        Button(self.new, text="Close")]        
        for i in range (0,len(self.paysActuel.sport)):
            self.bouton_sports_pays[i].config(text=self.paysActuel.sport[i].nom,command =self.Callback(self.buttonMenu[i]))
            self.bouton_sports_pays[i].grid(row=4,column=i)
            for j in range (0,len( self.paysActuel.sport[i].competition)):#self.liste_joueurs_pays[self.paysActuel.nom]["competition_"+
                print(str(i)+"*"+str(j))
                ad=ad+1
                self.liste_boutons_competitions[ad].config( text=self.paysActuel.sport[i].competition[j][0], command= lambda i=i,j=j : self.competition(self.paysActuel.sport[i].competition[j]))
                print(self.liste_boutons_competitions[j])
                self.liste_boutons_competitions[ad].grid(row=5+j, column=i)
        #showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
        #closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)
        #self.equipe(sports)
    def competition(self,C):
        self.competition2=C
        return self.show_competition()
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
        liste=[False,False]
        self.paysActuel=self.liste_pays[pays]
        self.liste=[]
        for i in range (0,len(self.paysActuel.sport)):
            #self.buttonMenu1 = Button(fenetre, height=1, width=15, text="Match en direct")
            #self.buttonMenu.append(self.buttonMenu1)
            #print(self.buttonMenu[i])
            self.buttonMenu[i].config(text=self.paysActuel.sport[i].nom,command =self.Callback(self.buttonMenu[i]))
            #self.buttonMenu[i].bind("<Button-1>", self.Sports(self.sportsPays[pays][i]))
            
        #self.point2[pays].forget_pack()
        print("yo36")
        self.text2=self.paysActuel.description
        print(self.text2)
        self.texte()
        for i in range (0,len(self.paysActuel.sport)) :
            liste[i]=True
            self.buttonMenu[i].place(x=self.paysActuel.position[0],y=self.paysActuel.position[1]+20*(i))
        for i in range (len(self.paysActuel.sport),len(liste)):
            self.buttonMenu[i].place_forget() 
        for i in range (1,6):
            if self.azer[i]:
                self.text[i].place(x=self.paysActuel.position[0]-120,y=self.paysActuel.position[1]+20*(i-1))
    def onExit(self):

        self.quit()

#     def change_north_america(self):
#         root1=Toplevel(self.master)
#         north_america=NorthAmerica(root1)

#     def change_europa(self):
#         root2=Toplevel(self.master)
#         europe=Europe(root2)

#     def change_africa(self):
#         root3=Toplevel(self.master)
#         africa=Africa(root3)

#     def change_south_america(self):
#         root4=Toplevel(self.master)
#         America=SouthAmerica(root4)

#     def change_asie(self):
#         root5=Toplevel(self.master)
#         asie=Asia(root5)

#     def change_oceanie(self):
#         root6=Toplevel(self.master)
#         oceania=Oceanie(root6)

# class NorthAmerica:
    
#     def __init__(self, master):
    
#         self.master=master
#         self.master.resizable(0, 0)
#         self.master.title("Amérique du Nord")       
#         self.mappemonde = PhotoImage(file="amérique-nord123.png") 

#         self.can1 = Canvas(self.master, height=1700, width=1200)
#         self.can1.create_image(700, 400, image=self.mappemonde)      
#         self.can1.pack()

#         self.point = PhotoImage(file="point.png")
#         self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
#         self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)

# class SouthAmerica:
    
#     def __init__(self, master):
    
#         self.master=master
#         self.master.resizable(0, 0)
#         self.master.title("Amérique du Nord")       
#         self.mappemonde = PhotoImage(file="amérique-sud123.png") 

#         self.can1 = Canvas(self.master, height=1700, width=1200)
#         self.can1.create_image(700, 400, image=self.mappemonde)      
#         self.can1.pack()

#         self.point = PhotoImage(file="point.png")
#         self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
#         self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)

# class Europe:
    
#     def __init__(self, master):
    
#         self.master=master
#         self.master.resizable(0, 0)
#         self.master.title("Europe")       
#         self.mappemonde = PhotoImage(file="europe123.png") 

#         self.can1 = Canvas(self.master, height=1700, width=1200)
#         self.can1.create_image(700, 400, image=self.mappemonde)      
#         self.can1.pack()

#         self.point = PhotoImage(file="point.png")
#         self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
#         self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)

# class Africa:
    
#     def __init__(self, master):
    
#         self.master=master
#         self.master.resizable(0, 0)
#         self.master.title("Afrique")       
#         self.mappemonde = PhotoImage(file="africa123.png") 

#         self.can1 = Canvas(self.master, height=1700, width=1200)
#         self.can1.create_image(700, 400, image=self.mappemonde)      
#         self.can1.pack()

#         self.point = PhotoImage(file="point.png")
#         self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
#         self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)

# class Asia:
    
#     def __init__(self, master):
    
#         self.master=master
#         self.master.resizable(0, 0)
#         self.master.title("Asie")       
#         self.mappemonde = PhotoImage(file="asie123.png") 

#         self.can1 = Canvas(self.master, height=1700, width=1200)
#         self.can1.create_image(700, 400, image=self.mappemonde)      
#         self.can1.pack()

#         self.point = PhotoImage(file="point.png")
#         self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
#         self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)

# class Oceanie:
    
#     def __init__(self, master):
    
#         self.master=master
#         self.master.resizable(0, 0)
#         self.master.title("Oceanie")       
#         self.mappemonde = PhotoImage(file="oceanie123.png") 

#         self.can1 = Canvas(self.master, height=1700, width=1200)
#         self.can1.create_image(700, 400, image=self.mappemonde)      
#         self.can1.pack()

#         self.point = PhotoImage(file="point.png")
#         self.pointColombie = Button(self.master, image=self.point, height=15, width=15).place(x=559, y=420)
#         self.pointJapon = Button(self.master, image=self.point, height=15, width=15).place(x=1400, y=250)
