from tkinter import *
import sports
import tkinter.ttk as tk
import datetime


class AllSoccer:
    
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
        self.s.set("")
        self.text_widget.insert(END, self.s.get())

        self.buttonFrame = Frame(self.master)
        self.buttonFrame.pack(side = BOTTOM, fill=X, pady = 6)
        self.all_matches_button = tk.Button(self.buttonFrame, text="All Matches", command=self.get_all_soccer) 
        self.all_matches_button.pack(side=LEFT, padx=2)


    def get_all_soccer(self): # montre tous les matchs en direct

        match_str = '               Live NBA Matches ' + str(datetime.datetime.now()) + '\n'

        try:
            matches = sports.get_sport(sports.SOCCER)
            self.text_widget.delete('1.0', END)
            self.s.set(match_str)
            self.text_widget.insert(INSERT, matches) 
        except:
            print("Error")


class AllBasketball:
    
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
        self.s.set("")
        self.text_widget.insert(END, self.s.get())

        self.buttonFrame = Frame(self.master)
        self.buttonFrame.pack(side = BOTTOM, fill=X, pady = 6)
        self.all_matches_button = tk.Button(self.buttonFrame, text="All Matches", command=self.get_all_basketball) 
        self.all_matches_button.pack(side=LEFT, padx=2)


    def get_all_basketball(self): # montre tous les matchs en direct

        match_str = '               Live NBA Matches ' + str(datetime.datetime.now()) + '\n'

        try:
            matches = sports.get_sport(sports.BASKETBALL)
            self.text_widget.delete('1.0', END)
            self.s.set(match_str)
            self.text_widget.insert(INSERT, matches) 
        except:
            print("Error")

class AllTennis:
    
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
        self.s.set("")
        self.text_widget.insert(END, self.s.get())

        self.buttonFrame = Frame(self.master)
        self.buttonFrame.pack(side = BOTTOM, fill=X, pady = 6)
        self.all_matches_button = tk.Button(self.buttonFrame, text="All Matches", command=self.get_all_tennis) 
        self.all_matches_button.pack(side=LEFT, padx=2)


    def get_all_tennis(self): # montre tous les matchs en direct

        match_str = '               Live NBA Matches ' + str(datetime.datetime.now()) + '\n'

        try:
            matches = sports.get_sport(sports.TENNIS)
            self.text_widget.delete('1.0', END)
            self.s.set(match_str)
            self.text_widget.insert(INSERT, matches) 
        except:
            print("Error")


class AllVolleyball:
    
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
        self.s.set("")
        self.text_widget.insert(END, self.s.get())

        self.buttonFrame = Frame(self.master)
        self.buttonFrame.pack(side = BOTTOM, fill=X, pady = 6)
        self.all_matches_button = tk.Button(self.buttonFrame, text="All Matches", command=self.get_all_volleyball) 
        self.all_matches_button.pack(side=LEFT, padx=2)


    def get_all_volleyball(self): # montre tous les matchs en direct

        match_str = '               Live NBA Matches ' + str(datetime.datetime.now()) + '\n'

        try:
            matches = sports.get_sport(sports.VOLLEYBALL)
            self.text_widget.delete('1.0', END)
            self.s.set(match_str)
            self.text_widget.insert(INSERT, matches) 
        except:
            print("Error")