from tkinter import *

KILOMETERS_IN_A_MILE = 1.609
FONT = ("Arial", 10, "bold")


def convert_miles_to_km():
    km = int(miles_input.get()) * KILOMETERS_IN_A_MILE
    kilometer_result_label.delete(0, END)
    kilometer_result_label.insert(END, string=f"{km}")

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize()
window.config(padx=20, pady=20)

# Enter widget for entering number of miles at 2, 1
miles_input = Entry(width=30)
# Add some text to begin with
miles_input.insert(END, string="20")
miles_input.grid(column=2, row=1)

# Place the label "miles" at 3, 1
miles_label = Label(text="miles", font=FONT)
miles_label.grid(column=3, row=1)

# Place the label "is equal to" at 1, 2
is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=1, row=2)

# Place a result entry window at 2, 2
kilometer_result_label = Entry(width=30)
# Add some text to begin with
kilometer_result_label.insert(END, string="x")
# Gets text in entry
kilometer_result_label.grid(column=2, row=2)

# "km" at 3, 2
kilometers_label = Label(text="kilometers", font=FONT)
kilometers_label.grid(column=3, row=2)

# Places button at 2, 3 and calls action() when pressed
button = Button(text="Calculate", command=convert_miles_to_km)
button.grid(column=2, row=3)


window.mainloop()
