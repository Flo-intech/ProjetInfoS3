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


questions_1 = ["Quel est le record de France de saut à la perche?",
             "Quel est le record du Monde du lancer de javelot",
             "Quel est le record du monde sur 100m ?",
             "Quel est le meilleur français sur 100m ?",
             "De quels pays sont les meilleurs sprinters"]

options = [["6,00m", "6,01m", "6,02m", "6,03m"],
           ["98, 48m", "96, 48m", "94, 48m", "92, 48m"],
           ["9s58", "9s57", "19s19", "9s92"],
           ["Jimmy Vicault", "Christophe Lemaitre", "Emmanuel Biron", "Teddy Tinmar"],
           ["La France", "Les USA", "La Jamaique", "Les Sud Africain"]]

correct_answers = ["B", "A", "A", "B", "C"]

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

Label(window, text="Bienvenue sur le quiz d'Athlétisme", font = ("Times New Roman", 18, "bold"), background = "#ffffff").pack(padx = 10, pady = 50)



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
