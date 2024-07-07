import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwd():
    website = website_input.get()
    username = email_input.get()
    passwd = password_input.get()

    if len(website) < 1 or len(passwd) < 1 or len(username) < 1:
        messagebox.showerror(message="Empty website or passwd is not allowed please try again.")
    else:
        confirmation = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername: {username}\nPassword:{passwd}")

        if confirmation:
            with open('password.txt', 'a') as passwd_file:
                passwd_file.write(f"{website} | {username} | {passwd} \n")

            website_input.delete(0, len(website))
            password_input.delete(0, len(passwd))
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

website_input = tkinter.Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

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