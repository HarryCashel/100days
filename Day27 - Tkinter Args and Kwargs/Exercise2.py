"""Keyword Arguments"""

"""Tkinter gui exercises"""

from tkinter import *

# Creates window object
window = Tk()

# Give title
window.title("Hello")

# Window properties
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am cool", font=("Ariel", 24, "italic"))
my_label["text"] = "New Text"
my_label.config(text="new_text")

# Places a label and centers it
my_label.pack(side="bottom", expand="True")


# button function
def button_clicked():
    input_text = u_input.get()
    my_label.config(text=input_text)
    print(my_label["text"])


# what happens when button is clicked
button = Button(text="Click", command=button_clicked)
button.pack()

# Entry
u_input = Entry(width=10)
u_input.pack()

print(u_input.get())

# Always at the end of the tkinter program
window.mainloop()
