"""
App that can generate password, store and retrieve data from json
"""

from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    password = "".join(password_list)
# ------------copy to clipboard------------
    pyperclip.copy(password)

    input_password.delete(0, END)
    input_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
        website_value = input_website.get()
        email_value = input_email.get()
        password_value = input_password.get()
        new_data = {
            website_value: {
                "email": email_value,
                "password": password_value,
            }
        }

        if len(website_value) == 0 or len(password_value) == 0:
            messagebox.showerror(title="Input error", message="Please fill all the inputs")
        else:
            try:
                with open("pass_data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("pass_data.json", "x") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("pass_data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                input_website.delete(0, END)
                input_password.delete(0, END)

# ---------------------------- FIND PASSWORD -------------------------- #

def find_password():
    searched_website = input_website.get()
    try:
        with open("pass_data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File not found", message="No data file found.")
    else:
        if searched_website in data:
            found_email = data[searched_website]["email"]
            found_password = data[searched_website]["password"]
            messagebox.showinfo(title=f"{searched_website}", message=f"email: {found_email}\npassword: {found_password}")
        else:
            messagebox.showwarning(title="Not found", message= "There is no such website registered.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Keeper")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="padlock.png")
padlock_img = padlock_img.subsample(3)
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# ---------------------------- LABELS ------------------------------- #
label_website = Label(text="Website:", font=("Arial", 12))
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:", font=("Arial", 12))
label_email.grid(column=0, row=2)
label_password = Label(text="Password:", font=("Arial", 12))
label_password.grid(column=0, row=3)
# ---------------------------- ENTRIES ------------------------------- #
input_website = Entry(width=32)
input_website.grid(column=1, row=1, columnspan=2, sticky=W)
input_website.focus()
input_email = Entry(width=52)
input_email.grid(column=1, row=2, columnspan=2, sticky=W)
input_email.insert(0, "mymail@gmail.com")
input_password = Entry(width=32)
input_password.grid(column=1, row=3, sticky=W)
# ---------------------------- BUTTONS ------------------------------- #
button_search = Button(text="Search", width=14, command=find_password)
button_search.grid(column=2, row=1, sticky=W)
button_generate = Button(text="Generate password", command=generate_password)
button_generate.grid(column=2, row=3, sticky=W)
button_add = Button(text="Add", width=44, command=save_password)
button_add.grid(column=1, row=4, columnspan=2, sticky=W)


window.mainloop()