from tkinter import *


# button function
def button_clicked():
    input_text = u_input.get()
    my_label.config(text=input_text)
    print(my_label["text"])


window = Tk()
window.title("GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="Mr Label", font=("Ariel", 24, "italic"))
my_label.config(text="new_text")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)
# my_label.pack()

# Buttons
button = Button(text="Click", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click me too")
button2.grid(column=2, row=0)

# Entry
u_input = Entry(width=10)
u_input.grid(column=3, row=3)


# Always at the end of the tkinter program
window.mainloop()
