import string
from tkinter import *
import calendar
from datetime import date, time, datetime
from getpass import getpass
import re


    
def pseudo():

    pseudo = string.digits + string.ascii_letters
    pseudo_min = 6
    pseudo_max = 16
    x = string.digits + string.ascii_letters

    def pseudo_characters(pseudo):

        # vérifie la syntaxe du pseudo

        i = 0

        while i < len(pseudo):
            if pseudo[i] in string.punctuation:
                print("Critères non respectés")
                return False
            i = i + 1
            
        else :
            print("Critères respectés")
            return True

    def pseudo_length(pseudo):
    
    # verifie le nombre de caractère dans le pseudo

        if len(pseudo) < pseudo_min:
            print("Pseudo trop court")
            return False
        elif len(pseudo) > pseudo_max:
            print("Pseudo trop long")
            return False
        else:
            print("Pseudo validé")
            return True


def mailadress(mail):

# Mise en place de la syntaxe de l'adresse mail

    chars = r"^[^<>]*<([^<>]+)>$|(^[^<>]+$)"
    a = re.findall(chars, mail.strip())

    if len(a)>0:
        address = ''.join(a[0]).strip()

    else:
        address = ''

# vérifie si la syntaxe de l'adresse mail est valide 
        
    if address =='':
        return False

    else:
        chars = r"^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$"
        return re.match(chars, address) != None


def password():

    password_min = 8

    def password_characters(password):

        # vérifie la syntaxe du mot de passe

        i = 0

        while i < len(password):
            if password[i] in string.punctuation:
                print("Critères non respectés")
                return False
            i = i + 1
            
        else :
            print("Critères respectés")
            return True

    def password_length(password):

    # verifie le nombre de caractère dans le mot de passe

        if len(password) < password_min:
            print("Mot de passe trop court")
        else:
            print("Mot de passe validé")

    def validate(self):
        password_entry.delete(0, END)
        password_entry.insert(0, password)


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
label_title = Label(frame, text="Adresse de messagerie", font=("Helvetica", 15), bg='#4065A4', fg='white')
label_title.pack()

# champs/entrée/input
birthday_entry = Entry(frame, text="Adresse de messagerie", font=("Helvetica", 15), bg='#4065A4', fg='white')
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
generate_password_button = Button(frame, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white', command=pseudo)
generate_password_button.pack(pady = 30)


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