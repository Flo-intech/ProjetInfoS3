import string
from tkinter import *
from tkinter import messagebox

class Personne:

    def __init__(self, pseudo = StringVar(), password = StringVar(), password_confirmation = StringVar(), emailadress = StringVar()):
        self._pseudo = pseudo
        self.pseudo = Personne()
        self._password = password
        self._password_confirmation = password_confirmation
        self._emailadress = emailadress


    def pseudo(self):
            return self._pseudo

    def password(self):
        return self._password

    def password_confirmation(self):
        return self._password_confirmation

    def emailadress(self): 
        return self._emailadress



    def validPseudo(self, pseudo):
            
        i = 0 

        if i < len(pseudo):
            if self.pseudo[i] in string.punctuation:
                return True
            return False
            
        else:
            messagebox.showinfo('Information', 'This is not a valid Pseudo')
            return False    