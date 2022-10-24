from tkinter import *
import pandas
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
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
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text=current_card["French"], fill="black")
    canvas.itemconfig(language_text, text ="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text=current_card["English"], fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)


def is_known():
    global current_card, data
    print(current_card)
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(400, 150, font=LANGUAGE_FONT)
card_title = canvas.create_text(400, 263, font=WORD_FONT)

card_back_image = PhotoImage(file="images/card_back.png")

unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)
known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

print(to_learn)
window.mainloop()
