from tkinter import *

# Functions
def addition():
    result.set(float(num1.get()) + float(num2.get()))

def subtraction():
    result.set(float(num1.get()) - float(num2.get()))

def multiplication():
    result.set(float(num1.get()) * float(num2.get()))

def division():
    if float(num2.get()) != 0:
        result.set(float(num1.get()) / float(num2.get()))
    else:
        result.set("Cannot divide by zero")

# GUI Window
root = Tk()
root.title("Menu Driven Calculator")
root.geometry("300x250")

# Variables
num1 = StringVar()
num2 = StringVar()
result = StringVar()

# Labels and Entries
Label(root, text="First Number").pack()
Entry(root, textvariable=num1).pack()

Label(root, text="Second Number").pack()
Entry(root, textvariable=num2).pack()

# Buttons (Menu Options)
Button(root, text="Addition", command=addition).pack(pady=2)
Button(root, text="Subtraction", command=subtraction).pack(pady=2)
Button(root, text="Multiplication", command=multiplication).pack(pady=2)
Button(root, text="Division", command=division).pack(pady=2)

# Result
Label(root, text="Result").pack()
Entry(root, textvariable=result, state="readonly").pack()

root.mainloop()
