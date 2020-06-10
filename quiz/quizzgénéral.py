#!/usr/bin/env python3

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as messagebox
import json

class VerticalScrolledFrame:
    def __init__(self, master, **kwargs):
        self.outer = tk.Frame(master)

        self.vsb = tk.Scrollbar(self.outer, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        self.canvas = tk.Canvas(self.outer, highlightthickness=0, **kwargs)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas['yscrollcommand'] = self.vsb.set
        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)
        self.vsb['command'] = self.canvas.yview

        self.inner = tk.Frame(self.canvas)
        self.canvas.create_window(4, 4, window=self.inner, anchor='nw')
        self.inner.bind("<Configure>", self._on_frame_configure)

        self.outer_attr = set(dir(tk.Widget))

    def __getattr__(self, item):
        if item in self.outer_attr:
            return getattr(self.outer, item)
        else:
            return getattr(self.inner, item)

    def _on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        
        if event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units" )
        elif event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units" )

root=tk.Tk()
root.geometry('1900x1080')
root.title('Quiz Program')
img_label = tk.Label(root)
img_label.img = tk.PhotoImage(file='logoprojet.png')
'''Le logo est peut-être un peu trop gros'''
img_label.config(image=img_label.img)
img_label.pack()

welcom=tk.Label(root,text="Bienvenue sur ce quizz")
welcom.pack()

score = 0

def mquit():
    mexit=messagebox.askyesno(title="Quitter",message="Quitter le quizz ?")
    if mexit > 0:
        root.destroy()
        return

def finished():
    mexit=messagebox.askyesno(title="Répondre",message="Etes-vous sûrs ?")
    if mexit > 0:
        score = 0
        for i in user_answers:
            if user_answers[i].get() == database[i]['answer']:
                score = score + 1

        lc.config(text="Tu as {} questions sur {} correcte(s)!".format(score, len(user_answers)))

with open('database.json') as f:
    database = json.load(f)

labels = {}
user_answers = {}
question_frame = VerticalScrolledFrame(root, height=500)
question_frame.pack(fill=tk.X)

for i in range(50):
    user_answers[i] = tk.IntVar(value=-1)
    labels[i] = tk.Label(question_frame, text=database[i]['question'])
    labels[i].pack(anchor=tk.W)
    for j in range(4):
        btn = tk.Radiobutton(question_frame,
            text=database[i]['options'][j],
            value=j,
            variable=user_answers[i])
        btn.pack(anchor=tk.W)


mbutton=tk.Button(root,text='Quitter',command=mquit,fg='white',bg='black')
mbutton.pack()


lc = tk.Label(root) # the score will be displayed here.
lc.pack()

fbutton=tk.Button(root,text='Répondre',command=finished,fg='white',bg='black')
fbutton.pack()


root.mainloop()
