from tkinter import *

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Bonne réponse!")
            right += 1
        else:
            label = Label(view, text="Mauvaise réponse.")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))

    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Merci d'avoir répondu aux questions. " + str(right) + " sur " + str(number_of_questions) + "\n de bonnes réponses").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()


questions_1 = ["Lequel de ces joueurs est devenu le numéro un mondial en 2004 ?",
             "Lequel de ses joueurs est devenu le numéro un mondial en 2008 ?",
             "Lequel de ces joueurs est l'actuel numéro un mondial ?",
             "Combien y a t-il de grands Chelem ?",
             "Quel est le seul grand tournoi gagné par Yannick Noah ?"]

options = [["Warwinka", "Monfils", "Federer", "Nadal"],
           ["Nadal", "Federer", "Djokovic", "Murray"],
           ["Murray", "Djokovic", "Tsonga", "Nadal"],
           ["3", "4", "5", "6"],
           ["Roland Garros", "Wimbledon", "Open d'Australie", "US open"]]

correct_answers = ["C", "A", "B", "B", "A"]

questions = []
for i in range(len(questions_1)):
    questionString = questions_1[i]
    answers = []
    for j in range(4):
        answers.append(options[i][j])
    correctLetter = correct_answers[i]
    questions.append(Question(questionString, answers, correctLetter))
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()

window.title("Quiz Window")
window.geometry("500x500")
window.config(background = "#ffffff")
window.resizable(0,0)

label_heading = Label(
    window,
    text = "QUIZ",
    font = ("Times New Roman", 24, "bold"),
    background = "#ffffff"
    )
label_heading.pack()

Label(window, text="Bienvenue sur le quiz de Tennis", font = ("Times New Roman", 18, "bold"), background = "#ffffff").pack(padx = 10, pady = 50)



button = Button(
    window,
    text = "Commencer le quizz",
    font = ("Times New Roman", 16),
    relief = FLAT,
    border = 0,
    command = askQuestion
    )
button.pack(padx = 10, pady = 50)
window.mainloop()
