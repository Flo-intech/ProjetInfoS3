import string
from tkinter import *
from calendar import *


def Pseudo(): 

    pseudo_min = 6
    pseudo_max = 12
    all_chars = string.punctuation + string.digits + string.ascii_letters
    
def Birthday():
    return

def validate():
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