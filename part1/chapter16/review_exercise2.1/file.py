from Tkinter import *
import tkFileDialog

window = Tk()

frame = Frame()
frame.pack()

def open_file(): # ask user to choose a file and update label
    type_list = [("Python scripts", "*.py"), ("Text files", "*.txt")]
    file_name = tkFileDialog.askopenfilename(filetypes=type_list)
    label_file.config(text=file_name)

# blank label to hold name of chosen file
label_file = Label(frame)
label_file.pack()

# button to click on ofr 'OPen' file dialog
button_open = Button(frame, text="Choose a file...", command=open_file)
button_open.pack()

window.mainloop()
