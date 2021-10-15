import tkinter as tk

BACKGROUND_COLOUR = "#B1DDC6"
FONT1 = ("Ariel", 40, "italic")
FONT2 = ("Ariel", 60, "bold")


class MainUi:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(width=800, height=526)
        self.image = tk.PhotoImage(file="./images/card_front.png")
        self.canvas.create_image(400, 263, image=self.image)
        self.canvas.config(bg=BACKGROUND_COLOUR, highlightthickness=0)
        self.canvas.grid(row=0, column=0)
        self.canvas.create_text(400, 150, text="Title", font=FONT1)
        self.canvas.create_text(400, 263, text="J_word", font=FONT2)
        self.u_input = tk.Entry(self.canvas, )
        self.canvas.create_window(400, 400, window=self.u_input, height=25, width=100)
        self.submit_button = tk.Button(self.canvas, text="Submit", command=self.button_click)
        self.canvas.create_window(400, 425, window=self.submit_button, height=25, width=50)

    def button_click(self):
        pass


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
