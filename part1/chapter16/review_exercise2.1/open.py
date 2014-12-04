from Tkinter import *
import tkFileDialog

window = Tk()

frame = Frame()
frame.pack()

def save_file(): # ask user to choose a file tand update label
    type_list = [("Python scripts", "*,py"), ("Text files", "*.txt")]
    file_name = tkFileDialog.asksaveasfilename(filetypes=type_list,
                                               defaultextension=".py")
    file_name = tkFileDialog.asksaveasfilename(filetypes=type_list,
                                               defaultextension=".py")
    my_text = "I will save: " + file_name
    label_file.config(text=my_text)

label_file = Label(frame)
label_file.pack()

button_open = Button(frame, text="Choose a file...",
                     command=save_file)
button_open.pack()

window.mainloop()
