from Tkinter import *

window = Tk()
window.title("Practice exercise 2")

frame = Frame()
frame.grid(padx=10, pady=10)

def click_me():
    button.config(text=entry.get())
    pass

button = Button(frame, text="click me", command=click_me)
button.grid(row=1, column=1, sticky=E)

entry = Entry(frame, width=12)
entry.grid(row=1, column=2)
entry.insert(0, "Type something")


window.mainloop()
