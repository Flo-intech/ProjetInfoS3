import string
from tkinter import *
from tkinter import messagebox
import re
from Pseudo import Personne

class Window(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.window = Tk(self)
        window.title("Inscription")
        window.geometry("720x480")
        window.config(background='#4065A4')

        self.info = 'tempfile.temp'


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

        self.validate_button = Button(window, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white', command=self.save_info).place(x=250, y=430)

        
    def save_info(self):

        if Personne.get() == "":
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

    def initialisation(self):
        pseudo.set("")
        password.set("")
        password_confirmation.set("")
        emailadress.set("")

window = Tk()
my_gui = Window(window)
window.mainloop()