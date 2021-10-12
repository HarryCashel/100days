from tkinter import *

window = Tk()
window.title("Converters")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)


class Window:
    """Models our widgets"""

    def __init__(self, unit_to_convert, converted, column=0, row=0):

        self.widgetss = []
        self.sign = Label(text="=")
        self.sign.grid(column=column + 0, row=row + 1, padx=(20, 0))
        self.user_input = Entry(width=10)
        self.user_input.grid(column=column + 1, row=row + 0)
        self.default_value = Label(text="0")
        self.default_value.grid(column=column + 1, row=row + 1)

        if unit_to_convert == "km":
            self.button = Button(text="Calculate", command=self.calculate_km)
            self.button.grid(column=1, row=3)

        elif unit_to_convert == "c":
            self.button = Button(text="Calculate", command=self.calculate_c)
            self.button.grid(column=1, row=3)

        elif unit_to_convert == "kg":
            self.button = Button(text="Calculate", command=self.calculate_kg)
            self.button.grid(column=1, row=3)

        elif unit_to_convert == "cm":
            self.button = Button(text="Calculate", command=self.calculate_cm)
            self.button.grid(column=1, row=3)

        self.first_unit = Label(text=unit_to_convert)
        self.first_unit.grid(column=2, row=0)
        self.second_unit = Label(text=converted)
        self.second_unit.grid(column=2, row=1)

        self.widgetss.extend([self.default_value,
                              self.first_unit,
                              self.second_unit,
                              # self.button,
                              self.user_input
                              ])

    def reset_all(self):
        for widget in self.widgetss:
            widget.destroy()

    def calculate_km(self):
        miles = float(self.user_input.get())

        km = round(miles * 1.60934, 2)

        self.default_value.config(text=km)

    def calculate_c(self):
        f = float(self.user_input.get())

        c = round((f - 32) * 5 / 9, 2)

        self.default_value.config(text=c)

    def calculate_kg(self):
        lbs = float(self.user_input.get())

        kg = round(lbs / 2.205, 2)

        self.default_value.config(text=kg)

    def calculate_cm(self):
        inch = float(self.user_input.get())

        cm = round(inch * 2.54, 2)

        self.default_value.config(text=cm)


def current_selection(event):
    if listbox.get(listbox.curselection()) == "miles":
        x = Window("km", "m")
    elif listbox.get(listbox.curselection()) == "F":
        y = Window("F ", "C")
    elif listbox.get(listbox.curselection()) == "lbs":
        z = Window("lbs", "kg")
    elif listbox.get(listbox.curselection()) == "inch":
        q = Window("inch", "cm")


listbox = Listbox(height=4)
units = {"miles": "km", "F": "C", "lbs": "kg", "inch": "cm"}

for item in units.keys():
    listbox.insert(END, item)
listbox.bind("<<ListboxSelect>>", current_selection)
listbox.grid(column=5, row=5)

window.mainloop()
