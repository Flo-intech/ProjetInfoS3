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


questions_1 = ["Quel joueur mythique marquait encore 15 points de moyenne par match à 40 ans?",
             "Quel est l'entraîneur le plus titré de l'histoire?",
             "Qui est le recordman du plus grand nombre de points marqués en NBA ?",
             " Quel est le seul joueur de NBA à avoir marqué 100 points dans un match?",
             "Quel fut le surnom donné à l’équipe de basket qui a participé aux Jeux olympiques de 1992 à Barcelone"]

options = [["Micheal Jordan", "Kareem Abdul-Jabbar", "Shaquille O'Neal", "Kevin Garnett"],
           [" Phil Jackson", "Gregg Popovich", "Alex Hannum", "Steve Kerr"],
           ["Kareem Abdul-Jabbar", "Michael Jordan", "Magic Johnson", "Kobe Bryant"],
           ["Kobe Bryant", "Wilt Chamberlain", "David Robinson", "Stephen Curry"],
           ["Dream Team", "Golden Team", "Best Team", "Amazing Team"]]

correct_answers = ["B", "A", "B", "A", "A"]

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

window.title("Quiz Basketball")
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

Label(window, text="Bienvenue sur le quiz Basketball", font = ("Times New Roman", 18, "bold"), background = "#ffffff").pack(padx = 10, pady = 50)



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
