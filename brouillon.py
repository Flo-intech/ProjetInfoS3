from tkinter import *


class Welcome:
    
    def __init__(self, master):
        self.master=master
        self.master.geometry("720x480")
        self.master.title("Welcome")
        self.master.config(background='#4065A4') 

        self.login_button = Button(self.master, text="Connexion", font=("Helvetica", 17), bg='#4065A4', fg='white', width=15, command=self.change2).place(x=260, y=150)

        self.register_button = Button(self.master, text="Inscription", font=("Helvetica", 17), bg='#4065A4', fg='white', width=15, command=self.change1).place(x=260, y=220)   

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

        self.emailadress_entry = Entry(self.master, font=("Helvetica", 15), bg='#4065A4', fg='white')
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

        self.validate_button = Button(self.master, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white').place(x=250, y=430)

    def initialisation(self):
        pseudo = self.pseudo.set("")
        password = self.password.set("")
        password = self.password_confirmation.set("")
        emailadress = self.emailadress.set("")
    

       

class Connexion:

    def __init__(self, master,):
        self.master=master
        self.master.geometry("720x480")
        self.master.title("Connexion")
        self.master.config(background='#4065A4')

        pseudo_label = Label(self.master, text="Pseudo", font=("Helvetica", 15), bg='#4065A4', fg='white')
        pseudo_label.place(x=240, y=80)


        pseudo_entry = Entry(self.master, font=("Helvetica", 15), bg='#4065A4', fg='white')
        pseudo_entry.place(x=240, y=110)


        password_label = Label(self.master, text="Mot de passe", font=("Helvetica", 15), bg='#4065A4', fg='white')
        password_label.place(x=240, y=160)


        password_entry = Entry(self.master, show="*", font=("Helvetica", 15), bg='#4065A4', fg='white')
        password_entry.place(x=240, y=190)


        validate_button = Button(self.master, text="Valider", font=("Helvetica", 17), bg='#4065A4', fg='white').place(x=250, y=250)

        back_button = Button(self.master, text="Retour", font=("Helvetica", 17), bg='#4065A4', fg='white').place(x=360, y=250)

def main():

    root = Tk()
    obj = Welcome(root) 
    root.mainloop()

if __name__ == '__main__':
    main()