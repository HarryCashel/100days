import json
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import pyperclip


class CustomDialog(simpledialog.Dialog):

    def __init__(self, parent, title=None, text=None):
        super().__init__(parent, title)
        self.data = text
        simpledialog.Dialog.__init__(self, parent, title=title)

    def body(self, parent):

        self.text = tk.Text(self, width=40, height=4)
        self.text.pack(fill="both", expand=True)

        self.text.insert("1.0", self.data)

        return self.text


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, tk.END)
    import random
    import string
    characters = string.printable[:-2]
    numbers = characters[:10]
    letters = characters[10:62]
    symbols = characters[-36:-4]

    password = letters + numbers + symbols
    password = random.choices(password, k=10)
    random.shuffle(password)
    new_password = "".join(password)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    def check(check_file, key):
        try:
            with open(check_file, "r") as file:
                data = json.load(file)
                in_dict = key in data
                return in_dict
        except FileNotFoundError:
            with open(check_file, "w") as file:
                json.dump(new_data, file, indent=4)

    website = website_entry.get()
    password = password_entry.get()
    email = username_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(email) < 1 or len(password) < 1 or len(website) < 1:
        messagebox.showinfo("Error", "Please fill out all fields.")
    else:

        try:
            if check("data.json", website):
                save_bool = messagebox.askyesno(title=website, message=f"Overwrite Password?\nEmail: {email}")

                if save_bool:
                    with open("data.json", "r") as file:
                        data = json.load(file)
                        data.update(new_data)
                    with open("data.json", mode="w") as file:
                        json.dump(data, file, indent=4)
                    messagebox.showinfo("Success", f"Saved {website} credentials.")
                else:
                    pass

            else:
                try:
                    with open("data.json", "r") as file:
                        data = json.load(file)
                        data.update(new_data)
                    with open("data.json", mode="w") as file:
                        json.dump(data, file, indent=4)
                        messagebox.showinfo("Success", f"Saved {website} credentials.")
                except IOError:
                    with open("data.json", "w") as file:
                        json.dump(new_data, file, indent=4)
        except json.decoder.JSONDecodeError:
            # print("Key not inside")
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            except IOError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            # username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


def search_cred():
    website = website_entry.get()
    # try:
    with open("data.json", "r") as file:
        data = json.load(file)
        in_dict = website in data
        if in_dict:
            email = data[website]["email"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(website, f"Email: {email}\nPassword: {password}\nPassword copied to clipboard")

        else:
            messagebox.showinfo(website, f"There is no credentials stored for {website}")
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
# Window properties
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, )

# Image canvas widget
canvas = tk.Canvas(width=200, height=200, )
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = tk.Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=1, sticky="EW", )

website_entry.focus()

username_entry = tk.Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(tk.END, "cashel.harry@gmail.com")

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons

generate_pw_button = tk.Button(text="Generate Password", command=password_generator)
generate_pw_button.grid(column=2, row=3, sticky="EW")

add_credentials_button = tk.Button(text="Add", width=36, command=save_password)
add_credentials_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = tk.Button(text="Search", command=search_cred)
search_button.grid(column=2, row=1, sticky="EW")
window.mainloop()
