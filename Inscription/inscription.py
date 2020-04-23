import string
from tkinter import *
import calendar
from datetime import date, time, datetime
from getpass import getpass


def pseudo(self, pseudo):

    pseudo = str 
    pseudo_min = len(6)
    pseudo_max = len(12)
    x = string.punctuation + string.digits + string.ascii_letters
    i = 0
    found = False

    while i < len(pseudo):
        if pseudo[i] == x:
            found = True
        i = i + 1

    if len(pseudo) >= pseudo_min or len(pseudo) <= pseudo_max:
        print(pseudo)
    
    else:
        print("Pseudo trop court ou trop long")


def birthday(self, x, y, z):

    today = datetime.now()
    birthday = datetime(year=x, month=y, day=z)

    if today.year - birthday.year < 10 :
        print("Tu n'as pas encore 10 ans")

    return


def password(self):
    password_min = len(8)
    x = string.digits + string.ascii_letters
    password = str
    i = 0
    for i in range(len(password)):
        if i < len(password_min):
            print("Mot de passe trop court")
            break
            
            if password != str:
                print("Caractère non identifié")
                break
        print(i)


def validate(self):
    return


# fenetre
window = Tk()
window.title("Inscription")
window.geometry("720x480")
window.config(background='#4065A4')

# frame principale
frame = Frame(window, bg='#4065A4')

# deuxieme frame
frame1 = Frame(window, bg='#4065A4')

# titre
label_title = Label(frame, text="Pseudo", font=("Helvetica", 15), bg='#4065A4', fg='white')
label_title.pack()

# champs/entrée/input
pseudo_entry = Entry(frame, text="Pseudo", font=("Helvetica", 15), bg='#4065A4', fg='white')
pseudo_entry.pack()

# titre
label_title = Label(frame, text="Date de naissance", font=("Helvetica", 15), bg='#4065A4', fg='white')
label_title.pack()

# champs/entrée/input
birthday_entry = Entry(frame, text="Date de naissance ", font=("Helvetica", 15), bg='#4065A4', fg='white')
birthday_entry.pack()

# titre
label_title = Label(frame, text="Mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
label_title.pack()

# champs/entrée/input
password_entry = Entry(frame, text="Mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
password_entry.pack()



# afficher la frame pricipale
frame.pack(side=TOP, pady = 100)

# creer un bouton
generate_password_button = Button(frame, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white', command=validate)
generate_password_button.pack(pady = 30)


# creation de la barre de menu
menu_bar = Menu(window)

# creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=validate)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configuration de la fenetre pour ajouter le menu bar
window.config(menu=menu_bar)

# Afficher la fenetre
window.mainloop()