import tkinter as tk
from tkinter import messagebox

#str converts the output to a "string" type"
#type prints the type of value

messagebox.showinfo("type(2)", str(type(2)))

messagebox.showinfo('type("Hi")', str(type("Hi")))

pi = 3.14
initial = "c"

messagebox.showinfo("type(pi)", str(type(pi)))

messagebox.showinfo("type(initial)", str(type(initial)))
