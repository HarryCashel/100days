from tkinter import *

window = Tk()
window.title("Converters")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)


class Window:
    """Models our widgets"""

    def __init__(self, unit_to_convert, converted, column=0, row=0):
        self.column = column
        self.widgets = []
        self.sign = Label(text="=")
        self.sign.grid(column=column + 0, row=row + 1, padx=(20, 0))
        self.user_input = Entry(width=10)
        self.user_input.grid(column=column + 1, row=row + 0)
        self.default_value = Label(text="0")
        self.default_value.grid(column=column + 1, row=row + 1)

        if unit_to_convert == "km":
            self.button = Button(text="Calculate", command=self.calculate_km)
            self.button.grid(column=1, row=3)

        elif x:
            pass

        self.first_unit = Label(text=unit_to_convert)
        self.first_unit.grid(column=2, row=0)
        self.second_unit = Label(text=converted)
        self.second_unit.grid(column=2, row=1)

    def calculate_km(self):
        miles = float(self.user_input.get())

        km = round(miles * 1.60934, 2)

        self.default_value.config(text=km)


def current_selection(event):
    if listbox.get(listbox.curselection()) == "miles":
        x = Window("km", "m")


listbox = Listbox(height=4)
units = {"miles": "km", "F": "C", "lbs": "kg", "inch": "cm"}

for item in units.keys():
    listbox.insert(END, item)
listbox.bind("<<ListboxSelect>>", current_selection)
listbox.grid(column=5, row=5)

window.mainloop()
