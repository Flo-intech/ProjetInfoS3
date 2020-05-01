import string
from tkinter import *
import calendar
from datetime import date, time, datetime
from getpass import getpass
import re

def delete():
    window1.destroy()


def delete1():
    window2.destroy()


def error():
    global window1
    window1 = Toplevel(window)
    window1.geometry("150x90")
    window1.title("Warning!")
    Label(window1, text = "All fields required", fg = "red").pack()
    Button(window1, text = "OK", command = delete).pack

def success():
    global window2
    window2 = Toplevel(window)
    window2.geometry("150x90")
    window2.title("Warning!")
    Label(window2, text = "Registration Sucess!", fg = "green").pack()
    Button(window2, text = "OK", command = delete1).pack()


def save_info():
    pseudo_info = pseudo.get()
    mailadress_info = mailadress.get()
    password_info = password.get()
    print(pseudo_info, mailadress_info, password_info)

    file = open("user.txt", "w")
    file.write(pseudo_info)
    file.write(mailadress_info)
    file.write(password_info)
    file.close()
    print(" User", pseudo_info, " has been registered successfully")

    pseudo_entry.delete(0, END)
    mailadress_entry.delete(0, END)
    password_entry.delete(0, END)

    if pseudo_info is False:
        error()

    elif mailadress_info is False:
        error()

    elif password_info is False:
        error()

    else:
        success()

    
def pseudo():

    pseudo_min = 6
    pseudo_max = 16

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


def password(password):

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
            return False

        else:
            print("Mot de passe validé")
            return True




# fenetre
window = Tk()
window.title("Inscription")
window.geometry("720x480")
window.config(background='#4065A4')
validate = window.register(mailadress)


pseudo = StringVar()
password = StringVar()
mailadress = StringVar()


# frame principale
frame = Frame(window, bg='#4065A4')

# deuxieme frame
frame1 = Frame(window, bg='#4065A4')

# titre
label_title = Label(frame, text="Pseudo", font=("Helvetica", 15), bg='#4065A4', fg='white')
label_title.pack()

# champs/entrée/input
pseudo_entry = Entry(frame, textvariable = pseudo, font=("Helvetica", 15), bg='#4065A4', fg='white')
pseudo_entry.pack()

# titre
label_title = Label(frame, text="Adresse de messagerie", font=("Helvetica", 15), bg='#4065A4', fg='white')
label_title.pack()

# champs/entrée/input
mailadress_entry = Entry(frame, textvariable = mailadress, font=("Helvetica", 15), bg='#4065A4', fg='white', validatecommand=(validate))
mailadress_entry.pack()

# titre
label_title = Label(frame, text="Mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
label_title.pack()

# champs/entrée/input
password_entry = Entry(frame, textvariable = password, font=("Helvetica", 15), bg='#4065A4', fg='white')
password_entry.pack()



# afficher la frame pricipale
frame.pack(side=TOP, pady = 100)

# creer un bouton
generate_password_button = Button(frame, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white', command=save_info)
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