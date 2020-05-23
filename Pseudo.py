import string
from tkinter import *
from tkinter import messagebox

class Pseudo:

    def __init__(self, pseudo, password, password_confirmation, emailadress):
        self.pseudo = pseudo
        self.password = password
        self.password_confirmation = password_confirmation
        self.emailadress = emailadress


    def pseudo(self):
        return self.pseudo

    def password(self):
        return self.password

    def password_confirmation(self):
        return self.password_confirmation

    def emailadress(self):
        return self.emailadress