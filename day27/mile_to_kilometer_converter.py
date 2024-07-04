from tkinter import *


def kilometer_converter():
    miles = textbox.get()
    km = int(miles) * 1.6
    label3.config(text=km)


window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

textbox = Entry()
textbox.insert(0, 0)
textbox.grid(row=0, column=1)

label1 = Label(window,text="Miles")
label1.grid(row=0, column=2)

label2 = Label(window, text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(window, text="0")
label3.grid(row=1, column=1)

label4 = Label(window, text="Km")
label4.grid(row=1, column=2)

button = Button(window, text="Calculate", command=kilometer_converter)
button.grid(row=2, column=1)

window.mainloop()
