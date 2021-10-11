from tkinter import *


def calculate():
    miles = u_input.get()
    result = round(float(miles) * 1.609, 3)
    label4.config(text=result)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=100, pady=100)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to aprrox.")
label2.grid(column=0, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

label4 = Label(text="0")
label4.grid(column=1, row=1)

u_input = Entry(width=5)
u_input.grid(column=1, row=0)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)



window.mainloop()
