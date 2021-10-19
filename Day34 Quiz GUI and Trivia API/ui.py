import tkinter as tk
from quiz_brain import QuizBrain

# constants
THEME_COLOUR = "#375362"
FONT = ("Ariel", 20, "italic")


class QuizInterface:

    def __init__(self, current_quiz: QuizBrain):
        self.current_quiz = current_quiz
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOUR, padx=20, pady=20)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Place holder", font=FONT, fill=THEME_COLOUR,
                                                     width=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.score_label = tk.Label(text=f"Score: {self.current_quiz.score}", bg=THEME_COLOUR, fg="white")
        self.score_label.grid(column=1, row=0)

        true_img = tk.PhotoImage(file="./images/true.png")
        self.guess_true = tk.Button(image=true_img, command=self.guess_true)
        self.guess_true.grid(column=0, row=2)

        false_img = tk.PhotoImage(file="./images/false.png")
        self.guess_false = tk.Button(image=false_img, command=self.guess_false)
        self.guess_false.grid(column=1, row=2)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.button_state(tk.ACTIVE)
        self.canvas.configure(bg="white")
        self.score_label.config(text=f"Score: {self.current_quiz.score}")
        if self.current_quiz.have_questions():
            q_text = self.current_quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="That's The end."
                                        f"You scored {self.current_quiz.score}/{len(self.current_quiz.question_list)}")
            self.button_state(tk.DISABLED)

    def button_state(self, state: str):
        self.guess_true.config(state=state)
        self.guess_false.config(state=state)

    def guess_true(self):
        is_right = self.current_quiz.check_answer("True")
        self.give_feedback(is_right)

    def guess_false(self):
        is_right = self.current_quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.button_state(tk.DISABLED)
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_question)
