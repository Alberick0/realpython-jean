from Tkinter import *

window = Tk()
frame = Frame()
frame.grid()

label_top = Label(frame, text="I'm at (1,1)", relief=SUNKEN)
label_top.grid(row=1, column=1, padx=100, pady=30)

label_bottom = Label(frame, bd=3,  text="I'm at (2,1)", relief=SUNKEN)
label_bottom.grid(row=2, column=1, sticky=E)

button = Button(frame, text="I span 2 rows", height=5)
button.grid(row=1, column=2, rowspan=2)

window.mainloop()
