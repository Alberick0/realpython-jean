from Tkinter import *

window = Tk()

entry1 = Entry()
entry2 = Entry()
entry1.pack()
entry2.pack()

entry1.insert(0, "This is a test")

text = "Another entry"
entry2.insert(0, text)
entry2.insert(13, " for testing")

window.mainloop()
