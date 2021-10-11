import tkinter



window = tkinter.Tk()

window.title("Multiple Converters")

#window.minsize(width=270, height=250)

window.config(padx=20, pady=20)





class LittleWindow:

    def __init__(self, to_be_converted, converted, c=0, r=0):

        self.equal_label = tkinter.Label(text="=", font=("Arial", 14))

        self.equal_label.grid(column=c+0, row=r+1, padx=(20, 0))

        self.user_input = tkinter.Entry(width=10)

        self.user_input.grid(column=c+1, row=r+0)

        self.km_label = tkinter.Label(text="0", font=("Arial", 12))

        self.km_label.grid(column=c+1, row=r+1)

        if to_be_converted == "Miles":

            self.button = tkinter.Button(text="Calculate", command=self.calculate_km)

            self.button.grid(column=c+1, row=r+2, pady=(0, 20))

        elif to_be_converted == "F":

            self.button = tkinter.Button(text="Calculate", command=self.calculate_temp)

            self.button.grid(column=c + 1, row=r + 2, pady=(0, 20))

        elif to_be_converted == "lbs":

            self.button = tkinter.Button(text="Calculate", command=self.calculate_kg)

            self.button.grid(column=c + 1, row=r + 2, pady=(0, 20))

        elif to_be_converted == "inch":

            self.button = tkinter.Button(text="Calculate", command=self.calculate_cm)

            self.button.grid(column=c + 1, row=r + 2, pady=(0, 20))

        self.miles_label = tkinter.Label(text=to_be_converted, font=("Arial", 12))

        self.miles_label.grid(column=c+2, row=r+0)

        self.km_unit_label = tkinter.Label(text=converted, font=("Arial", 12))

        self.km_unit_label.grid(column=c+2, row=r+1)



    def calculate_km(self):

        miles = float(self.user_input.get())

        km = round(miles * 1.60934, 2)

        self.km_label.config(text=km)



    def calculate_temp(self):

        temp_F = float(self.user_input.get())

        temp_C = round((temp_F-32)*5/9, 2)

        self.km_label.config(text=temp_C)



    def calculate_kg(self):

        pounds = float(self.user_input.get())

        kg = round(pounds * 0.453592, 2)

        self.km_label.config(text=kg)



    def calculate_cm(self):

        inch = float(self.user_input.get())

        cm = round(inch * 2.54, 2)

        self.km_label.config(text=cm)





little_window_km = LittleWindow("Miles", "km")

little_window_temp = LittleWindow("F", "C", c=3)

little_window_kg = LittleWindow("lbs", "kg", r=3)

little_window_cm = LittleWindow("inch", "cm", c=3, r=3)



window.mainloop()