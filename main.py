from tkinter import *
import turtle

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=30)

my_label = Label(text="I am a label", font=("Arial", 24))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked!")
    input_text = user_input.get()
    my_label.config(text=input_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

user_input = Entry(width=10)
user_input.get()
user_input.grid(row=2, column=3)

new_button = Button(text="Click me too")
new_button.grid(row=0, column=2)












window.mainloop()
