from tkinter import *
FONT = ("Arial", 24)


def calculate():
    miles = int(miles_input.get())
    km = miles * 1.60934
    km_output.config(text=km)


# def update_km_value():
#     km_output.config(text=calculate())


window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=100, pady=100)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(row=1, column=0)

calc = Button(text="Calculate", font=FONT, command=calculate)
calc.grid(row=2, column=1)

miles_input = Entry(width=10, font=FONT)
miles_input.grid(row=0, column=1)

km_output = Label(text=0, font=FONT)
km_output.grid(row=1, column=1)

window.mainloop()