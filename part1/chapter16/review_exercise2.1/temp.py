from Tkinter import *

def calculate_temp():
    number = celsius_entry.get()
    try:
        fahrenheit = float(number) * 9/5 + 32
        fahrenheit = round(fahrenheit, 3)
        result.config(text=fahrenheit)
    except ValueError:
        result.config(fahrenheit="Invalid input")

window = Tk()
window.title("Celcius to Fahrenheit")
window.geometry("300x60")

frame = Frame()
frame.grid(padx=10, pady=10)

celsius_label = Label(frame, text="Celcius Temperature:")
celsius_label.grid(row=1, column=1, sticky=S+E)

result_label = Label(frame, text="Fahrenheit Temperature:")
result_label.grid(row=2, column=1, sticky=S+E)

celsius_entry = Entry(frame, width=3)
celsius_entry.grid(row=1, column=2)
celsius_entry.insert(0,0)

calculate_button = Button(frame, text="Calcualte", command=calculate_temp)
calculate_button.grid(row=1, column=3, rowspan=2)

result = Label(frame)
result.grid(row=2, column=2)

calculate_temp()
window.mainloop()
