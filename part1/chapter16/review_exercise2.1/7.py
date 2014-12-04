from Tkinter import *

window = Tk()

frame = Frame()

def increment_number():
    number = 1 + button.cget("text")
    button.config(text=number)

button = Button(text=1, command=increment_number)
button.pack()

window.mainloop()

