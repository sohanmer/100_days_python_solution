import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_image, image=card_front_image)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()


window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526)
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="red")
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="red")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tkinter.PhotoImage(file="images/wrong.png")
unknown_button = tkinter.Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

tick_image = tkinter.PhotoImage(file="images/right.png")
known_button = tkinter.Button(image=tick_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

card_back_image = tkinter.PhotoImage(file="images/card_back.png")


next_card()

window.mainloop()
