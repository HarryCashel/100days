import tkinter as tk
from tkinter import messagebox
import pandas
import json

# Constants
BACKGROUND_COLOUR = "#B1DDC6"
SECONDARY_COLOUR = "#DDB1C8"
FONT1 = ("Ariel", 40, "italic")
FONT2 = ("Ariel", 60, "bold")
RIGHT = "./images/right.png"
WRONG = "./images/wrong.png"

# Files
japanese_data = pandas.read_csv("./data/Japanese_top_1000.csv")
jd = japanese_data.to_dict()


def create_score():
    try:
        with open("./data/score.txt", mode="r") as file:
            content = file.read()
            content = int(content)
            file.flush()
    except FileNotFoundError:
        with open("./data/score.txt", mode="w") as file:
            file.write("0")
            content = 0
            file.flush()
    return content


def read_words():
    try:
        with open("./data/known.json", mode="r") as file:
            data = json.load(file)
            file.flush()
            return data
    except FileNotFoundError:
        data = {}
        with open("./data/known.json", mode="w") as file:
            json.dump(data, file, indent=4)
            file.flush()
            return data


class MainUi:
    def __init__(self, master):
        self.score = 0
        self.high_score = create_score()
        self.word_list = jd
        self.known_words = read_words()
        self.starting_word = self.random_word()
        self.master = master
        self.canvas = tk.Canvas(width=800, height=526)
        self.image = tk.PhotoImage(file="./images/card_front.png")
        self.b_image = tk.PhotoImage(file="./images/card_back.png")
        self.background = self.canvas.create_image(400, 263, image=self.image)
        self.canvas.config(bg=BACKGROUND_COLOUR, highlightthickness=0)
        self.canvas.grid(row=0, column=0)
        self.title = self.canvas.create_text(400, 150, text="Japanese", font=FONT1)
        self.language = self.canvas.create_text(400, 263, text=self.starting_word[0], font=FONT2)
        self.u_input = tk.Entry(self.canvas, )
        self.canvas.create_window(400, 400, window=self.u_input, height=25, width=100)
        self.submit_button = tk.Button(self.canvas, text="Submit", command=self.button_click)
        self.canvas.create_window(400, 425, window=self.submit_button, height=25, width=50)
        self.current_score = self.canvas.create_text(400, 50, text=str(self.score), font=FONT1)

    def next_card(self):
        self.canvas.itemconfig(self.background, image=self.b_image)
        self.canvas.itemconfig(self.title, text="English", fill="white")
        self.canvas.itemconfig(self.language, text=self.starting_word[1], font=FONT2, fill="white")

    def button_click(self):
        if self.check_word():
            self.score += 1
            self.update_canvas()
            if self.score > self.high_score:
                self.high_score = self.score
                self.update_score()

        else:
            self.next_card()
            self.master.after(2000, func=self.update_canvas)
        # self.update_canvas()

    def stop_play(self):
        if self.high_score > self.score:
            messagebox.showinfo("High Score", f"The High Score is {self.high_score}")
        else:
            messagebox.showinfo("High Score", f"Nice! New High Score of {self.score}")

    def random_word(self):
        import random
        data = self.word_list
        r_index = random.randint(1, 1000)
        j_word = data["Japanese"][r_index]
        e_word = data["English"][r_index]
        return j_word, e_word

    def check_word(self):
        guess = self.u_input.get().lower()
        if guess == self.starting_word[1].lower():
            self.move_word()
            return True
        return False

    def move_word(self):
        word = self.starting_word[1]
        if word in self.known_words.keys():
            self.known_words[word] += 1
        else:
            self.known_words[word] = 1

        self.dump_known(self.known_words)

    def dump_known(self, new_data):
        with open("./data/known.json", "r") as file:
            data = json.load(file)
            data.update(new_data)
        with open("./data/known.json", mode="w") as file:
            json.dump(data, file, indent=4)


    def update_canvas(self):
        self.canvas.itemconfig(self.background, image=self.image, )
        self.u_input.delete(0, tk.END)
        self.starting_word = self.random_word()
        self.canvas.itemconfig(self.title, text="Japanese", font=FONT1, fill="black")
        self.canvas.itemconfig(self.language, text=self.starting_word[0], font=FONT2, fill="black")
        self.canvas.itemconfig(self.current_score, text=str(self.score))
        print(self.starting_word)

    def show_right(self):
        correct = self.canvas.create_window()

    def update_score(self):
        with open("./data/score.txt", "w") as file:
            data = self.high_score
            file.write(str(data))


class PracticeWindow:
    def __init__(self, master):
        pass

    def submit(self):
        pass


class CorrectWindow:
    def __init__(self, master):
        pass


class WrongWindow:
    def __init__(self, master):
        pass


# UI Config
root = tk.Tk()
root.title("Flash Card")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOUR)
app = MainUi(root)

root.mainloop()



