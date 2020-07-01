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


questions_1 = ["De quelle nationalié était le premier capitaine du Réal Madrid?",
             "Qui est le premier entraîneur nommé par Jean-Michel Aulas après sa prise de pouvoir à L'OL?",
             "Parmi les footballeurs ayant marqué au moins 50 buts en séléction nationale, quel joueur a le meilleur ratio but/selection?",
             "Quelle est la dérnière équipe anglaise à avoir remporté la C1 deux années de suite ?",
             "Quelle équipe est la plus titrée dans le championnat brésilien"]

options = [["Hongroise", "Irlandaise", "Espagnole", "Portugaise"],
           ["Denis Papa", "Raymond Domenech", "Robert Nouzaret", "Marcel Leborgne"],
           ["Pelé", "Poul Nielsen", "Gerd Muller", "Lionel Messi"],
           ["Nottingham Forest", "Aston villa", "Liverpool FC", "Manchester United"],
           ["Santos FC", "SC Corinthias", "CR Flamingo", "SE Palmeiras"]]

correct_answers = ["B", "A", "B", "A", "D"]

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

window.title("Quiz FOOTBALL")
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

Label(window, text="Bienvuenue sur le quiz football", font = ("Times New Roman", 18, "bold"), background = "#ffffff").pack(padx = 10, pady = 50)



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
