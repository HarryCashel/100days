"""Tkinter gui exercises"""

import tkinter

# Creates window object
window = tkinter.Tk()

# Give title
window.title("Hello")

# Window properties
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am cool", font=("Ariel", 24, "italic"))

# Places a label and centers it
my_label.pack(side="bottom", expand="True")



# Always at the end of the tkinter program
window.mainloop()
