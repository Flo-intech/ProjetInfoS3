import string
from tkinter import *
import calendar
from datetime import date, time, datetime
from getpass import getpass


    
def pseudo():

    pseudo = string.digits + string.ascii_letters
    pseudo_min = 6
    pseudo_max = 16
    x = string.digits + string.ascii_letters

    def pseudo_characters(pseudo):

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


        if len(pseudo) < pseudo_min:
            print("Pseudo trop court")
            return False
        elif len(pseudo) > pseudo_max:
            print("Pseudo trop long")
            return False
        else:
            print("Pseudo validé")
            return True



    def birthday(self, x, y, z):

        today = datetime.now()
        birthday_year = int(input("Année de naissance: "))
        birthday_month = int(input("Mois de naissace: "))
        birthday_day = int(input("Jour de naissance"))
        birthday = datetime

        while True:
          try:
              birthday_day = int(input("Jour de naissance : "))
              if birthday_day < 1 or birthday_day > 31:
                  raise ValueError
            
          except ValueError:
              print("Le jour de naissance n'est pas correct !")
              continue
          break

        while True:
          try:
              birthday_month = int(input("Mois de naissance : "))
              if birthday_month < 1 or birthday_month > 12:
                  raise ValueError
            
          except ValueError:
              print("Le mois de naissance n'est pas correct !")
              continue
          break

        while True:
              try:
                birthday_year = int(input("Année de naissance : "))
                if today.year - birthday_year > 10:
                        raise ValueError
            
              except ValueError:
                  print("Tu n'as pas encore 10 ans !")
                  continue
              break

def password():

    def password_characters(self, password):

        x = string.digits + string.ascii_letters
        found = False
        i = 0
        

        while i < len(password):
            if password[i] == x:
                found = True
                print("Critères respectés")
            i = i + 1

        else :
            print("Critères non respectés")

    def password_length(self, password):

        password_min = 8

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