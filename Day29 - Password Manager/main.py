import tkinter as tk
from tkinter import messagebox


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
    password = random.choices(password, k=8)
    random.shuffle(password)
    new_password = "".join(password)
    password_entry.insert(0, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    def check(check_file, string):
        with open(check_file) as f:
            datafile = f.readlines()
        found = False  # This isn't really necessary
        for line in datafile:
            if string in line:
                # found = True # Not necessary
                return True
        return False  # Because you finished the search without finding

    website = website_entry.get()
    password = password_entry.get()
    email = username_entry.get()

    empty_pop = messagebox.showinfo("Error", "Please fill out all fields.")

    if len(email) or len(password) or len(website) < 1:
        empty_pop
    else:
        save_bool = messagebox.askyesno(title=website, message=f"Save these details?\nEmail: {email}")

        if save_bool:

            formatted_str = f"{website} | {email} | {password}\n"

            with open("data.txt", mode="a") as file:
                if not check("data.txt", formatted_str):
                    file.write(formatted_str)

            messagebox.showinfo("Saved", "Your password has been saved")
        website_entry.delete(0, tk.END)
        # username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


def check_password():
    pass


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
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW", )

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

window.mainloop()
