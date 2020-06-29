import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk() 
root.geometry('300x200')

labelChoix = tk.Label(root, text = "Veuillez faire un choix !")
labelChoix.pack()

# 2) - créer la liste Python contenant les éléments de la liste Combobox
listeProduits=['Amiens', 'Angers', 'Bordeaux', 'Dijon', 'Lille',
  'Lyon', 'Marseille', 'Metz', 'Monaco', 'Montpellier', 'Nantes',
  'Nice', 'Nimes', 'ParisSaintGermain', 'Reims', 'Rennes', 'SaintEtienne', 'StadeBrestois29',
  'Strasbourg', 'Toulouse']

# 3) - Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(root, values=listeProduits)

# 4) - Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)


listeCombo.pack()

lab = tk.Label(root, text ="Bonjour", bg ="ivory", width =15)
lab.place(x=135, y=150)
lab.pack()

text_widget = tk.Text(root, fg='white', background='black')
text_widget.pack()

def clearTextInput():
    text_widget.delete("1.0","end")

textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Clear", 
                    command=clearTextInput)

btnRead.pack()

def changeLabel():
    lab.configure(text = listeCombo.get())
    prenom = listeCombo.get()
    file_ = open("utilisateur", 'a')
    file_.write(prenom + '\n') # Rajout d'un saut de ligne
    file_.close()
    file_ = open("utilisateur", 'r')
    first_name = file_.read()
    file_.close()
    print("Le contenu du fichier est:\n{}".format(first_name))
    # fichier = open("utilisateur", "r")
    # content = fichier.read()
    # fichier.close()
    text_widget.insert(END, listeCombo.get() + "\n")
    # text_widget.insert(END, first_name + "\n")


bou = tk.Button(root, text ="Test", command=changeLabel).place(x=135, y=150)
root.mainloop()








# import tkinter as tk
# from tkinter import ttk
# from tkinter import *

# root = tk.Tk() 
# root.geometry('300x200')

# labelChoix = tk.Label(root, text = "Veuillez faire un choix !")
# labelChoix.pack()

# # 2) - créer la liste Python contenant les éléments de la liste Combobox
# listeProduits=['Amiens', 'Angers', 'Bordeaux', 'Dijon', 'Lille',
#   'Lyon', 'Marseille', 'Metz', 'Monaco', 'Montpellier', 'Nantes',
#   'Nice', 'Nimes', 'ParisSaintGermain', 'Reims', 'Rennes', 'SaintEtienne', 'StadeBrestois29',
#   'Strasbourg', 'Toulouse']

# # 3) - Création de la Combobox via la méthode ttk.Combobox()
# listeCombo = ttk.Combobox(root, values=listeProduits)

# # 4) - Choisir l'élément qui s'affiche par défaut
# listeCombo.current(0)


# listeCombo.pack()

# lab = tk.Label(root, text ="Bonjour", bg ="ivory", width =15)
# lab.place(x=135, y=150)
# lab.pack()

# text_widget = tk.Text(root, fg='white', background='black')
# text_widget.pack()

# def clearTextInput():
#     text_widget.delete("1.0","end")

# textExample=tk.Text(root, height=10)
# textExample.pack()
# btnRead=tk.Button(root, height=1, width=10, text="Clear", 
#                     command=clearTextInput)

# btnRead.pack()

# def changeLabel():
#     lab.configure(text = listeCombo.get())
#     prenom = listeCombo.get()
#     file_ = open("utilisateur", 'a')
#     file_.write(prenom + '\n') # Rajout d'un saut de ligne
#     file_.close()
#     file_ = open("utilisateur", 'r')
#     first_name = file_.read()
#     file_.close()
#     print("Le contenu du fichier est:\n{}".format(first_name))
#     fichier = open("utilisateur", "r")
#     content = fichier.read()
#     fichier.close()
#     # text_widget.insert(END, listeCombo.get() + "\n")
#     text_widget.insert(END, first_name + "\n")


# bou = tk.Button(root, text ="Test", command=changeLabel).place(x=135, y=150)
# root.mainloop()
