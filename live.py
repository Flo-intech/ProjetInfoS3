import sports
import json
from tkinter import *
import tkinter.ttk as tk
import datetime

class Bundesliga:

    def __init__(self, master):
       
        self.master=master
        self.master.title("Bundesliga")
        self.master.resizable(0, 0)
        self.master.configure(background='white') 

        self.selectorFrame = Frame(self.master, background="white")
        self.selectorFrame.pack(anchor = "nw", pady = 2, padx=10)
        self.match_label = Label(self.selectorFrame, text = "Select Team 1 vs Team 2 :", background="white")
        self.match_label.pack(anchor="w")

        self.team1 = tk.Combobox(self.selectorFrame)
        self.team1.pack(side = LEFT, padx=3)

        self.team2 = tk.Combobox(self.selectorFrame)
        self.team2.pack(side = LEFT, padx=3)

        self.s = StringVar()

        self.matchFrame = Frame(self.master)
        self.matchFrame.pack(side=TOP)
        self.match = Label(self.matchFrame)
        self.match.pack()
        self.text_widget = Text(self.match, fg='white', background='black')
        self.text_widget.pack()
        self.s.set("d")
        self.text_widget.insert(END, self.s.get())

        self.buttonFrame = Frame(self.master)
        self.buttonFrame.pack(side = BOTTOM, fill=X, pady = 6)
        self.all_matches_button = tk.Button(self.buttonFrame, text="All Matches", command=self.get_bundesliga_matches) 
        self.all_matches_button.pack(side=LEFT, padx=2)

        self.team_tuple = tuple()
        self.bundesliga_list = [] # data

        self.f = open("bundesliga.txt", "r")
        for self.line in self.f.readlines():
            self.line = self.line.replace('\n', '')
            self.bundesliga_list.append(self.line)
            self.team_tuple += (self.line, )
        self.f.close()

        self.team1["values"] = self.team_tuple
        self.team1.current(1)
        self.team2["values"] = self.team_tuple
        self.team2.current(0)



    def get_bundesliga_matches(self): # montre tous les matchs en direct

        match_str = '               Live Bundesliga Matches ' + str(datetime.datetime.now()) + '\n'

        try:
            matches1 = sports.get_sport(sports.SOCCER)
            for item in matches1:
                match_all = str(item)
                for bundesliga_team in self.bundesliga_list:
                    if(bundesliga_team in match_all):
                        match_str += (match_all)  + '\n'
                        self.bundesliga_team = bundesliga_team
                        break
            self.text_widget.delete('1.0', END)
            self.s.set(match_str)
            self.text_widget.insert(INSERT, self.s.get()) 
        except:
            print("Error")


class SpainBasket:

    def __init__(self, master):
           
        self.master=master
        self.master.title("Bundesliga")
        self.master.resizable(0, 0)
        self.master.configure(background='white') 

        self.selectorFrame = Frame(self.master, background="white")
        self.selectorFrame.pack(anchor = "nw", pady = 2, padx=10)
        self.match_label = Label(self.selectorFrame, text = "Select Team 1 vs Team 2 :", background="white")
        self.match_label.pack(anchor="w")

        self.team1 = tk.Combobox(self.selectorFrame)
        self.team1.pack(side = LEFT, padx=3)

        self.team2 = tk.Combobox(self.selectorFrame)
        self.team2.pack(side = LEFT, padx=3)

        self.s = StringVar()

        self.matchFrame = Frame(self.master)
        self.matchFrame.pack(side=TOP)
        self.match = Label(self.matchFrame)
        self.match.pack()
        self.text_widget = Text(self.match, fg='white', background='black')
        self.text_widget.pack()
        self.s.set("d")
        self.text_widget.insert(END, self.s.get())

        self.buttonFrame = Frame(self.master)
        self.buttonFrame.pack(side = BOTTOM, fill=X, pady = 6)
        self.all_matches_button = tk.Button(self.buttonFrame, text="All Matches", command=self.get_spainbasket_matches) 
        self.all_matches_button.pack(side=LEFT, padx=2)

        self.team_tuple2 = tuple()
        self.spain_basket_list = [] # data

        self.f = open("spainbasket.txt", "r")
        for self.line in self.f.readlines():
            self.line = self.line.replace('\n', '')
            self.spain_basket_list.append(self.line)
            self.team_tuple2 += (self.line, )
        self.f.close()

        self.team1["values"] = self.team_tuple2
        self.team1.current(1)
        self.team2["values"] = self.team_tuple2
        self.team2.current(0)



    def get_spainbasket_matches(self): # montre tous les matchs en direct

        match_str = '               Live ACB Spain Matches ' + str(datetime.datetime.now()) + '\n'

        try:
            matches2 = sports.get_sport(sports.BASKETBALL)
            for item in matches2:
                match_all = str(item)
                for spainbasket_team in self.spain_basket_list:
                    if(spainbasket_team in match_all):
                        match_str += (match_all)  + '\n'
                        self.spainbasket_team = spainbasket_team
                        break
            self.text_widget.delete('1.0', END)
            self.s.set(match_str)
            self.text_widget.insert(INSERT, self.s.get()) 
        except:
            print("Error")

class England:
    
    def __init__(self, master):
           
        self.master=master
        self.master.title("Premier League")
        self.master.resizable(0, 0)
        self.master.configure(background='white') 

        self.selectorFrame = Frame(self.master, background="white")
        self.selectorFrame.pack(anchor = "nw", pady = 2, padx=10)
        self.match_label = Label(self.selectorFrame, text = "Select Team 1 vs Team 2 :", background="white")
        self.match_label.pack(anchor="w")

        self.team1 = tk.Combobox(self.selectorFrame)
        self.team1.pack(side = LEFT, padx=3)

        self.team2 = tk.Combobox(self.selectorFrame)
        self.team2.pack(side = LEFT, padx=3)

        self.s = StringVar()

        self.matchFrame = Frame(self.master)
        self.matchFrame.pack(side=TOP)
        self.match = Label(self.matchFrame)
        self.match.pack()
        self.text_widget = Text(self.match, fg='white', background='black')
        self.text_widget.pack()
        self.s.set("d")
        self.text_widget.insert(END, self.s.get())

        self.buttonFrame = Frame(self.master)
        self.buttonFrame.pack(side = BOTTOM, fill=X, pady = 6)
        self.all_matches_button = tk.Button(self.buttonFrame, text="All Matches", command=self.get_premierleague_matches) 
        self.all_matches_button.pack(side=LEFT, padx=2)

        self.team_tuple2 = tuple()
        self.premierleague_list = [] # data

        self.f = open("premierleague.txt", "r")
        for self.line in self.f.readlines():
            self.line = self.line.replace('\n', '')
            self.premierleague_list.append(self.line)
            self.team_tuple2 += (self.line, )
        self.f.close()

        self.team1["values"] = self.team_tuple2
        self.team1.current(1)
        self.team2["values"] = self.team_tuple2
        self.team2.current(0)



    def get_premierleague_matches(self): # montre tous les matchs en direct

        match_str = '               Live Premier League Matches ' + str(datetime.datetime.now()) + '\n'

        try:
            matches2 = sports.get_sport(sports.SOCCER)
            for item in matches2:
                match_all = str(item)
                for premierleague_team in self.premierleague_list:
                    if(premierleague_team in match_all):
                        match_str += (match_all)  + '\n'
                        self.premierleague_team = premierleague_team
                        break
            self.text_widget.delete('1.0', END)
            self.s.set(match_str)
            self.text_widget.insert(INSERT, self.s.get()) 
        except:
            print("Error")

class NBA:
    
    def __init__(self, master):
           
        self.master=master
        self.master.title("NBA")
        self.master.resizable(0, 0)
        self.master.configure(background='white') 

        self.selectorFrame = Frame(self.master, background="white")
        self.selectorFrame.pack(anchor = "nw", pady = 2, padx=10)
        self.match_label = Label(self.selectorFrame, text = "Select Team 1 vs Team 2 :", background="white")
        self.match_label.pack(anchor="w")

        self.team1 = tk.Combobox(self.selectorFrame)
        self.team1.pack(side = LEFT, padx=3)

        self.team2 = tk.Combobox(self.selectorFrame)
        self.team2.pack(side = LEFT, padx=3)

        self.s = StringVar()

        self.matchFrame = Frame(self.master)
        self.matchFrame.pack(side=TOP)
        self.match = Label(self.matchFrame)
        self.match.pack()
        self.text_widget = Text(self.match, fg='white', background='black')
        self.text_widget.pack()
        self.s.set("d")
        self.text_widget.insert(END, self.s.get())

        self.buttonFrame = Frame(self.master)
        self.buttonFrame.pack(side = BOTTOM, fill=X, pady = 6)
        self.all_matches_button = tk.Button(self.buttonFrame, text="All Matches", command=self.get_nba_matches) 
        self.all_matches_button.pack(side=LEFT, padx=2)

        self.team_tuple2 = tuple()
        self.nba_list = [] # data

        self.f = open("nba.txt", "r")
        for self.line in self.f.readlines():
            self.line = self.line.replace('\n', '')
            self.nba_list.append(self.line)
            self.team_tuple2 += (self.line, )
        self.f.close()

        self.team1["values"] = self.team_tuple2
        self.team1.current(1)
        self.team2["values"] = self.team_tuple2
        self.team2.current(0)



    def get_nba_matches(self): # montre tous les matchs en direct

        match_str = '               Live NBA Matches ' + str(datetime.datetime.now()) + '\n'

        try:
            matches2 = sports.get_sport(sports.BASKETBALL)
            for item in matches2:
                match_all = str(item)
                for nba_team in self.nba_list:
                    if(nba_team in match_all):
                        match_str += (match_all)  + '\n'
                        self.nba_team = nba_team
                        break
            self.text_widget.delete('1.0', END)
            self.s.set(match_str)
            self.text_widget.insert(INSERT, self.s.get()) 
        except:
            print("Error")

class SpainSoccer:
    
    def __init__(self, master):
           
        self.master=master
        self.master.title("Bundesliga")
        self.master.resizable(0, 0)
        self.master.configure(background='white') 

        self.selectorFrame = Frame(self.master, background="white")
        self.selectorFrame.pack(anchor = "nw", pady = 2, padx=10)
        self.match_label = Label(self.selectorFrame, text = "Select Team 1 vs Team 2 :", background="white")
        self.match_label.pack(anchor="w")

        self.team1 = tk.Combobox(self.selectorFrame)
        self.team1.pack(side = LEFT, padx=3)

        self.team2 = tk.Combobox(self.selectorFrame)
        self.team2.pack(side = LEFT, padx=3)

        self.s = StringVar()

        self.matchFrame = Frame(self.master)
        self.matchFrame.pack(side=TOP)
        self.match = Label(self.matchFrame)
        self.match.pack()
        self.text_widget = Text(self.match, fg='white', background='black')
        self.text_widget.pack()
        self.s.set("d")
        self.text_widget.insert(END, self.s.get())

        self.buttonFrame = Frame(self.master)
        self.buttonFrame.pack(side = BOTTOM, fill=X, pady = 6)
        self.all_matches_button = tk.Button(self.buttonFrame, text="All Matches", command=self.get_spainsoccer_matches) 
        self.all_matches_button.pack(side=LEFT, padx=2)

        self.team_tuple2 = tuple()
        self.spain_soccer_list = [] # data

        self.f = open("ligaBBVA.txt", "r")
        for self.line in self.f.readlines():
            self.line = self.line.replace('\n', '')
            self.spain_soccer_list.append(self.line)
            self.team_tuple2 += (self.line, )
        self.f.close()

        self.team1["values"] = self.team_tuple2
        self.team1.current(1)
        self.team2["values"] = self.team_tuple2
        self.team2.current(0)



    def get_spainsoccer_matches(self): # montre tous les matchs en direct

        match_str = '               Live Liga BBVA Matches ' + str(datetime.datetime.now()) + '\n'

        try:
            matches2 = sports.get_sport(sports.SOCCER)
            for item in matches2:
                match_all = str(item)
                for spain_soccer_team in self.spain_soccer_list:
                    if(spain_soccer_team in match_all):
                        match_str += (match_all)  + '\n'
                        self.spain_soccer_team = spain_soccer_team
                        break
            self.text_widget.delete('1.0', END)
            self.s.set(match_str)
            self.text_widget.insert(INSERT, self.s.get()) 
        except:
            print("Error")