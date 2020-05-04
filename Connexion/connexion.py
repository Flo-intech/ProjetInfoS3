import string
from tkinter import *
from tkinter import messagebox
import re
import Inscription from inscription.py

window = Tk()

#Définir la variable data sur tempfile.temp

info = 'tempfile.temp'

# fenetre
window.title("Inscription")
window.geometry("720x480")
window.config(background='#4065A4')


def check_login():

    # Prendre tout le document file dans lequel non met les informations et les place dans la variable de données

    with open(info) as f:
        data = f.readlines() 
        name = data[0].rstrip() 
        pwd = data[1].rstrip()
        mail = data[2].rstrip() 
 
    if pseudo.get() == name and password.get() == pwd and emailadress.get() == mail:
        miniwindow = Tk() 
        miniwindow.title('Succes')
        miniwindow.geometry('150x50') 
        rlbl = Label(miniwindow, text='\n[+] Utilisateur connecté')
        rlbl.pack() 
        miniwindow.mainloop()
    else:
        miniwindow = Tk()
        miniwindow.title('Echec')
        miniwindow.geometry('150x50')
        rlbl = Label(miniwindow, text='\n[!] Utilisateur invalide')
        rlbl.pack()
        miniwindow.mainloop()

    
# titre
label_title = Label(window, text="Pseudo", font=("Helvetica", 15), bg='#4065A4', fg='white')
label_title.place(x=240, y=80)

# champs/entrée/input
pseudo_entry = Entry(window, textvariable = pseudo, font=("Helvetica", 15), bg='#4065A4', fg='white')
pseudo_entry.place(x=240, y=110)

# titre
label_title = Label(window, text="Mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
label_title.place(x=240, y=160)

# champs/entrée/input
password_entry = Entry(window, show="*", textvariable = password, font=("Helvetica", 15), bg='#4065A4', fg='white')
password_entry.place(x=240, y=190)


# Bouton Validé
validate_button = Button(window, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white', command=check_login).place(x=250, y=250)

#Bouton Initialisé
back_button = Button(window, text="Retour", font=("Helvetica", 17), bg='#4065A4', fg='white').place(x=360, y=250)


# creation de la barre de menu
menu_bar = Menu(window)

# creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=pseudo)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configuration de la fenetre pour ajouter le menu bar
window.config(menu=menu_bar)

# Afficher la fenetre
window.mainloop()