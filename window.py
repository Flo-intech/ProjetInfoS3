import sys
import string
from tkinter import *
from tkinter import messagebox
import re

class Window():

    def __init__(self):
        self.window = Window
        window.title("Inscription")
        window.geometry("720x480")
        window.config(background='#4065A4')


        self.pseudo_label = Label(window, text="Pseudo", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.pseudo_label.place(x=240, y=80)

        self.pseudo_entry = Entry(window, textvariable = pseudo, font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.pseudo_entry.place(x=240, y=110)

        self.emailadress_label = Label(window, text="Adresse de messagerie", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.emailadress_label.place(x=240, y=160)

        self.emailadress_entry = Entry(window, textvariable = emailadress, font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.emailadress_entry.place(x=240, y=190)

        self.password_label = Label(window, text="Mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.password_label.place(x=240, y=240)

        self.password_entry = Entry(window,show="*", textvariable = password, font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.password_entry.place(x=240, y=270)

        self.password_confirmation_label = Label(window, text="Confirmer mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.password_confirmation_label.place(x=240, y=320)

        self.password_confirmation_entry = Entry(window, show="*", textvariable = password_confirmation, font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.password_confirmation_entry.place(x=240, y=350)

        self.initialisation_button = Button(window, text="Initialser", font=("Helvetica", 17), bg='#4065A4', fg='white', command=initialisation).place(x=360, y=430)

        self.validate_button = Button(window, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white', command=save_info).place(x=250, y=430)

        
        def validPseudo(self, pseudo):
        
            i = 0 

            if i < len(pseudo):
                if self.pseudo[i] in string.punctuation:
                    return True
                return False
            
            else:
                messagebox.showinfo('Information', 'This is not a valid Pseudo')
                return False


