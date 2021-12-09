import tkinter as tk
from tkinter import messagebox

def show_entry():
    """Function to show input fields"""
    messagebox.showinfo("User Entry", str(type(text.get())))
    
window = tk.Tk()


tk.Label(window, text="Number: ").grid(row=0)
text = tk.Entry(window)
text.grid(row=0, column=1)

tk.Button(window, text='Show', command=show_entry).grid(row=1)





