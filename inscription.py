import string
from tkinter import *
from tkinter import messagebox
import re
import os


window = Tk()

#Définir la variable info sur tempfile.temp

info = 'tempfile.temp'

pseudo = StringVar()
password = StringVar()
password_confirmation = StringVar()
emailadress = StringVar()

def validPseudo(pseudo):
    
    i = 0 

    if i < len(pseudo):
        if pseudo[i] in string.punctuation:
            return True
        return False
            
    else:
        messagebox.showinfo('Information', 'This is not a valid Pseudo')
        return False

def initialisation():
    pseudo.set("")
    password.set("")
    password_confirmation.set("")
    emailadress.set("")

def validEmail(mail):
    
# Mise en place de la syntaxe de l'adresse mail
# vérifie si la syntaxe du pseudo est valide 

    if len(mail) > 7:
        if re.match("^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$", mail) != None:
            return True
        return False
    else:
        messagebox.showinfo('Information', "Cette adresse email n'est pas valide")
        return False

def save_info():
    if pseudo.get() == "":
        messagebox.showinfo('Information', 'Veuillez entrer le nom complet pour continuer')
    elif password.get() == "":
        messagebox.showinfo('Information', 'Veuillez entrer le mot de passe pour continuer')
    elif emailadress.get() == "":
        messagebox.showinfo('Information', "Veuillez entrer l'adresse mail pour continuer")
    elif password_confirmation.get() == "":
        messagebox.showinfo('Information', "Veuillez confirmer l'adresse mail pour continuer")
    elif password.get() != password_confirmation.get():
        messagebox.showinfo('Information', 'Mot de passe différent')
    elif len(pseudo.get()) < 6:
            messagebox.showinfo('Information', 'Veuillez entrer 6 caractères minimum du pseudo pour continuer')
    elif len(pseudo.get()) > 16:
            messagebox.showinfo('Information', 'Veuillez entrer 16 caractères maximum du pseudo pour continuer')
    elif len(password.get()) < 8:
            messagebox.showinfo('Information', 'Veuillez entrer 8 caractères minimum du mot de passe pour continuer')
    elif emailadress.get() != "":
        status2 = validEmail(emailadress.get())
        if(status2):
            messagebox.showinfo('Information', 'Utilisateur enregistré avec succès')
    else:       
        messagebox.showinfo('Information', 'Utilisateur enregistré avec succès')

    with open(info, 'w') as f:
        f.write(pseudo_entry.get()) 
        f.write('\n') 
        f.write(password_entry.get()) 
        f.write('\n') 
        f.write(emailadress_entry.get()) 
        f.close() 



# fenetre
window.title("Inscription")
window.geometry("720x480")
window.config(background='#4065A4')



# titre
pseudo_label = Label(window, text="Pseudo", font=("Helvetica", 15), bg='#4065A4', fg='white')
pseudo_label.place(x=240, y=80)

# champs/entrée/input
pseudo_entry = Entry(window, textvariable = pseudo, font=("Helvetica", 15), bg='#4065A4', fg='white')
pseudo_entry.place(x=240, y=110)

# titre
emailadress_label = Label(window, text="Adresse de messagerie", font=("Helvetica", 15), bg='#4065A4', fg='white')
emailadress_label.place(x=240, y=160)

# champs/entrée/input
emailadress_entry = Entry(window, textvariable = emailadress, font=("Helvetica", 15), bg='#4065A4', fg='white')
emailadress_entry.place(x=240, y=190)

# titre
password_label = Label(window, text="Mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
password_label.place(x=240, y=240)

# champs/entrée/input
password_entry = Entry(window,show="*", textvariable = password, font=("Helvetica", 15), bg='#4065A4', fg='white')
password_entry.place(x=240, y=270)

# titre
password_confirmation_label = Label(window, text="Confirmer mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
password_confirmation_label.place(x=240, y=320)

# champs/entrée/input
password_confirmation_entry = Entry(window, show="*", textvariable = password_confirmation, font=("Helvetica", 15), bg='#4065A4', fg='white')
password_confirmation_entry.place(x=240, y=350)

# Bouton Validé
validate_button = Button(window, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white', command=save_info).place(x=250, y=430)

#Bouton Initialisé
initialisation_button = Button(window, text="Initialser", font=("Helvetica", 17), bg='#4065A4', fg='white', command=initialisation).place(x=360, y=430)

# creation de la barre de menu
menu_bar = Menu(window)

# creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=initialisation)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configuration de la fenetre pour ajouter le menu bar
window.config(menu=menu_bar)

# Afficher la fenetre
window.mainloop()