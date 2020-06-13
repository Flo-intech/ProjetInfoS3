from tkinter import *
from tkinter import messagebox
from testprojet import Mappemonde
from sports import *

class Welcome:
    
    def __init__(self, master):
        self.master=master
        self.master.geometry("720x480")
        self.master.title("Welcome")
        self.master.config(background='#4065A4') 

        self.login_button = Button(self.master, text="Connexion", font=("Helvetica", 17), bg='#4065A4', fg='white', width=15, command=self.change2).place(x=260, y=150)

        self.register_button = Button(self.master, text="Inscription", font=("Helvetica", 17), bg='#4065A4', fg='white', width=15, command=self.change1).place(x=260, y=220) 

        self.invite_button = Button(self.master, text="Invité", font=("Helvetica", 17), bg='#4065A4', fg='white', width=15).place(x=260, y=290) 

    def change1(self):
        root2=Toplevel(self.master)
        Register=Window(root2)

    
    def change2(self):
        
        root3=Toplevel(self.master)
        Login=Connexion(root3)

class Window:
    
    def __init__(self, master):
        self.master=master
        self.master.geometry("720x480")
        self.master.title("Inscription")
        self.master.config(background='#4065A4')

        self.info = 'tempfile.temp'

        self.pseudo = StringVar()
        self.password = StringVar()
        self.password_confirmation = StringVar()
        self.emailadress = StringVar()


        self.pseudo_label = Label(self.master, text="Pseudo", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.pseudo_label.place(x=240, y=80)

        self.pseudo_entry = Entry(self.master, font=("Helvetica", 15), textvariable = self.pseudo, bg='#4065A4', fg='white')
        self.pseudo_entry.place(x=240, y=110)

        self.emailadress_label = Label(self.master, text="Adresse de messagerie", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.emailadress_label.place(x=240, y=160)

        self.emailadress_entry = Entry(self.master, font=("Helvetica", 15), textvariable = self.emailadress, bg='#4065A4', fg='white')
        self.emailadress_entry.place(x=240, y=190)

        self.password_label = Label(self.master, text="Mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.password_label.place(x=240, y=240)

        self.password_entry = Entry(self.master, show="*", textvariable = self.password, font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.password_entry.place(x=240, y=270)

        self.password_confirmation_label = Label(self.master, text="Confirmer mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.password_confirmation_label.place(x=240, y=320)

        self.password_confirmation_entry = Entry(self.master, show="*", font=("Helvetica", 15), bg='#4065A4', fg='white', textvariable = self.password_confirmation)
        self.password_confirmation_entry.place(x=240, y=350)

        self.initialisation_button = Button(self.master, text="Initialser", font=("Helvetica", 17), bg='#4065A4', fg='white', command=self.initialisation).place(x=360, y=430)

        self.validate_button = Button(self.master, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white', command=self.save_info).place(x=250, y=430)

    def initialisation(self):
        pseudo = self.pseudo.set("")
        password = self.password.set("")
        password = self.password_confirmation.set("")
        emailadress = self.emailadress.set("")
    

    def save_info(self):
        if self.pseudo.get() == "":
            messagebox.showinfo('Information', 'Veuillez entrer le nom complet pour continuer')
        elif self.password.get() == "":
            messagebox.showinfo('Information', 'Veuillez entrer le mot de passe pour continuer')
        elif self.password_confirmation.get() == "":
            messagebox.showinfo('Information', "Veuillez confirmer l'adresse mail pour continuer")
        elif self.password.get() != self.password_confirmation.get():
            messagebox.showinfo('Information', 'Mot de passe différent')
        elif len(self.pseudo.get()) < 6:
            messagebox.showinfo('Information', 'Veuillez entrer 6 caractères minimum du pseudo pour continuer')
        elif len(self.pseudo.get()) > 16:
            messagebox.showinfo('Information', 'Veuillez entrer 16 caractères maximum du pseudo pour continuer')
        elif len(self.password.get()) < 8:
            messagebox.showinfo('Information', 'Veuillez entrer 8 caractères minimum du mot de passe pour continuer')
        elif self.emailadress.get() == "":
            messagebox.showinfo('Information', "Veuillez entrer l'adresse mail pour continuer")
        elif self.emailadress.get() != "":
            status2 = self.validEmail(self.emailadress.get())
            if(status2):
                messagebox.showinfo('Information', 'Utilisateur enregistré avec succès')
        else:       
            messagebox.showinfo('Information', 'Utilisateur enregistré avec succès')

    def validEmail(self, mail):
        
# Mise en place de la syntaxe de l'adresse mail
# vérifie si la syntaxe du pseudo est valide 

        if len(mail) > 7:
        
            if re.match("^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$", mail) != None:
                return True
            return False
        else:
            messagebox.showinfo('Information', "Cette adresse email n'est pas valide")
            return False       

class Connexion:

    def __init__(self, master):
        self.master=master
        self.master.geometry("720x480")
        self.master.title("Connexion")
        self.master.config(background='#4065A4')


        self.pseudo_label = Label(self.master, text="Pseudo", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.pseudo_label.place(x=240, y=80)


        self.pseudo_entry = Entry(self.master, font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.pseudo_entry.place(x=240, y=110)


        self.password_label = Label(self.master, text="Mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.password_label.place(x=240, y=160)


        self.password_entry = Entry(self.master, show="*", font=("Helvetica", 15), bg='#4065A4', fg='white')
        self.password_entry.place(x=240, y=190)


        self.validate_button = Button(self.master, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white', command=self.check_login).place(x=250, y=250)

        self.back_button = Button(self.master, text="Retour", font=("Helvetica", 17), bg='#4065A4', fg='white').place(x=360, y=250)



    def check_login(self):
        # Prendre tout le document file dans lequel non met les informations et les place dans la variable de données
        info = 'tempfile.temp'
        
        with open(info) as f:
            self.data = f.readlines() 
            name = self.data[0].rstrip() 
            pwd = self.data[1].rstrip() 
    
        if self.pseudo_entry.get() == name and self.password_entry.get() == pwd:
            messagebox.showinfo('Information', "Utilisateur connecté")
            self.name = name
            self.pwd = pwd
            
            self.root3=Toplevel(self.master)
            self.Map=Mappemonde(self.root3)
      

        else:
            messagebox.showinfo('Information', "Utilisateur invalide")


def main():

    root = Tk()
    obj = Welcome(root) 
    root.mainloop()

if __name__ == '__main__':
    main()