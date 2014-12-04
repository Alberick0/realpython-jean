from Tkinter import *

window = Tk()

frame = Frame()
frame.grid()

label_top = Label(frame, text="I'm at (1,1)")
label_top.grid(row=1, column=1)

label_bottom = Label(frame, text="I'm at (2,1)")
label_bottom.grid(row=2,column=1)

button_bottom = Button(frame, text="I'm at (3,2)")
button_bottom.grid(row=3, column=2)

window.mainloop()
