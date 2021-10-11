from tkinter import *

# Create new window and window properties

window = Tk()
window.title("Widget Examples")
window.minsize(width=800, height=600)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()


# Buttons
def action():
    print("Do something")


# calls action() when button is pressed
button = Button(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=20)
# Entry starting text
entry.insert(END, string="Some starting text")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=20)
# Places cursor in text box
text.focus()
# Adds some starter text
text.insert(END, "Some more starting text in a different box")
# Gets current value in textbox at line1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # Gets current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Check button
def check_button_used():
    # print 1 if check, otherwise 0
    print(check_state.get())


# Variable to hold check state, 0 if off 1 is on
check_state = IntVar()

check_button = Checkbutton(text="Is On?", variable=check_state, command=check_button_used)
check_state.get()
check_button.pack()


# Radio Button

def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked

radio_state = IntVar()
radio_button_1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radio_button_2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radio_button_1.pack()
radio_button_2.pack()


# List box
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Orange", "Banana", "Strawberry"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()