from Calculator import *

import tkinter as tk

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    result.set(float(num1.get()) / float(num2.get()))

root = tk.Tk()
root.title("Calculator")

num1 = tk.DoubleVar()
num2 = tk.DoubleVar()
result = tk.DoubleVar()

tk.Label(root, text="First Number").grid(row=0, column=0)
tk.Entry(root, textvariable=num1).grid(row=0, column=1)
tk.Label(root, text="Second Number").grid(row=1, column=0)
tk.Entry(root, textvariable=num2).grid(row=1, column=1)

tk.Button(root, text="+", command=add).grid(row=2, column=0)
tk.Button(root, text="-", command=subtract).grid(row=2, column=1)
tk.Button(root, text="*", command=multiply).grid(row=3, column=0)
tk.Button(root, text="/", command=divide).grid(row=3, column=1)

tk.Label(root, text="Result").grid(row=4, column=0)
tk.Label(root, textvariable=result).grid(row=4, column=1)

# Add a button for the square root function to the GUI
tk.Button(root, text="√", command=lambda: result.set(square_root(float(num1.get())))).grid(row=4, column=0)

root.mainloop()