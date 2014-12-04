from Tkinter import *

window = Tk()
window.title("Here's a window")
window.geometry("300x100")

frame = Frame()
frame.pack()

message = Label(frame, text="I've been framed", bg='red', fg='yellow')
message.pack()

window.mainloop()

