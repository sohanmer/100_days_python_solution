import json
import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letter + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, password)


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
            try:
                messagebox.showinfo(message=f"Username: {data[website]['email']}\nPassword: {data[website]['password']}")
            except KeyError:
                messagebox.showinfo(message=f"No data found for {website}")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(message="Data file is empty.")
    except FileNotFoundError:
        messagebox.showinfo(message="No data file found.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwd():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) < 1 or len(password) < 1 or len(email) < 1:
        messagebox.showerror(message="Empty website or password is not allowed please try again.")
    else:
        try:
            with open('data.json') as data_file:
                data = json.load(data_file)
        except json.decoder.JSONDecodeError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, len(website))
            password_input.delete(0, len(password))
# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=0, columnspan=3)

website_label = tkinter.Label(text="Website: ")
website_label.grid(row=1, column=0)

website_input = tkinter.Entry(width=18)
website_input.grid(row=1, column=1, columnspan=1)

search_btn = tkinter.Button(text="Search", width=12, command=search)
search_btn.grid(row=1, column=2, columnspan=1)

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_input = tkinter.Entry(width=35)
email_input.insert(0, 'test@gmail.com')
email_input.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password: ")
password_label.grid(row=3, column=0)

password_input = tkinter.Entry(width=18)
password_input.grid(row=3, column=1)

generate_psswd_btn = tkinter.Button(text="Generate Password", width=12, command=generate_passwd)
generate_psswd_btn.grid(row=3, column=2)

add_btn = tkinter.Button(text="Add", width=35, command=save_passwd)
add_btn.grid(row=4, column=1, columnspan=3)


canvas.mainloop()