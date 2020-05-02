import string
from tkinter import *
from tkinter import messagebox
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

    pseudo_min = 6
    pseudo_max = 16

    if len(pseudo) < pseudo_min:
        print("Pseudo trop court")
        return False
    elif len(pseudo) > pseudo_max:
        print("Pseudo trop long")
        return False
    else:
        print("Pseudo validé")
        return True


def validEmail(mail):

# Mise en place de la syntaxe de l'adresse mail

    if len(mail) > 7:
        if re.match("^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$", user_email) != None:
            return True
        return False
    else:
        messagebox.showinfo('Information', 'This is not a valid email address')
        return False

# vérifie si la syntaxe de l'adresse mail est valide 



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

    password_min = 8

    # verifie le nombre de caractère dans le mot de passe

    if len(password) < password_min:
        print("Mot de passe trop court")
        return False

    else:
        print("Mot de passe validé")
        return True



def save_info():
    if pseudo.get() == "":
        messagebox.showinfo('Information', 'Please Enter FullName to Proceed')
    elif password.get() == "":
        messagebox.showinfo('Information', 'Please Enter Password to Proceed')
    elif emailadress.get() == "":
        messagebox.showinfo('Information', 'Please Enter Email to Proceed')
    elif pseudo.get()  == "":
        status1 = pseudo_characters(pseudo.get())
        status2 = pseudo_length(pseudo.get())
        if (status1):
            messagebox.showinfo('Information', 'User Registered Successfully')
        if (status2):
            messagebox.showinfo('Information', 'User Registered Successfully')
    elif password.get() == "":
        status3 = password_characters(pseudo.get())
        status4 = password_length(pseudo.get())
        if (status3):
            messagebox.showinfo('Information', 'User Registered Successfully')
        if (status4):
            messagebox.showinfo('Information', 'User Registered Successfully')
    elif emailadress.get() == "":
        status5 = validEmail(emailadress.get())
        if(status5):
            messagebox.showinfo('Information', 'User Registered Successfully')
    else:
        messagebox.showinfo('Information', 'User Registered Successfully')

# fenetre
window = Tk()
window.title("Inscription")
window.geometry("720x480")
window.config(background='#4065A4')


pseudo = StringVar()
password = StringVar()
emailadress = StringVar()


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
emailadress_entry = Entry(frame, textvariable = emailadress, font=("Helvetica", 15), bg='#4065A4', fg='white')
emailadress_entry.pack()

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