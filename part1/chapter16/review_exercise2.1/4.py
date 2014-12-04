from Tkinter import *

window = Tk()
window.geometry("200x50")

frame = Frame()
frame.pack()

frame_left = Frame(bd=3, relief=SUNKEN)
frame_left.place(relx=0, relwidth=0.6, relheight=1)

frame_right = Frame(bd=3, relief=SUNKEN)
frame_right.place(relx=0.6, relwidth=0.4)

label_left = Label(frame_left, text="I've been framed!")
label_left.pack()

label_right = Label(frame_right, text="So have I!")
label_right.pack()


window.mainloop()
