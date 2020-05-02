import string
from tkinter import *
from tkinter import messagebox
import re



window = Tk()


def validPseudo(pseudo):
    
    i = 0 

    if i < len(pseudo):
        if pseudo[i] in string.punctuation:
            return True
        return False
            
    else:
        messagebox.showinfo('Information', 'This is not a valid Pseudo')
        return False

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




# fenetre
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