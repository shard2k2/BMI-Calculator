import tkinter as tk

#main window

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300")

#adding label
label = tk.Label(window, text="Hello! This is a tkinter window!", font=("Arial", 14))
label.pack(pady=20)

#button
def button_click():
    label.config(text="Button was clicked!")

button = tk.Button(window, text="Click Me!", command=button_click)
button.pack()

#start the app
window.mainloop()