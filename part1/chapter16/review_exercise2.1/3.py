from Tkinter import *

window = Tk()

frame = Frame()
frame.pack()

top_label = Label(frame, text="top bar", bg="red")
top_label.pack(fill=X)

left_label = Label(frame, text="left", bg="yellow")
left_label.pack(side=LEFT)

middle_label = Label(frame, text="middle", bg="green")
middle_label.pack(side=LEFT)

right_label = Label(frame, text="right", bg="blue")
right_label.pack(side=LEFT)

window.mainloop()
