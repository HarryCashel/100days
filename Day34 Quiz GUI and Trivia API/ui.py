import tkinter as tk

# constants
THEME_COLOUR = "#375362"
FONT = ("Ariel", 20, "italic")

def guess_true():
    pass


class QuizInterface:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOUR, padx=20, pady=20)

        self.canvas = tk.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Place holder", font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.score_label = tk.Label(text=f"Score: 0", bg=THEME_COLOUR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.true_img = tk.PhotoImage(file="./images/true.png")
        self.guess_true = tk.Button(image=self.true_img, command=guess_true())
        self.guess_true.grid(column=0, row=2)

        self.false_img = tk.PhotoImage(file="./images/false.png")
        self.guess_false = tk.Button(image=self.false_img, command=guess_true())
        self.guess_false.grid(column=1, row=2)

        self.window.mainloop()
