import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_entry():
    """Function to show input fields"""
    messagebox.showinfo("User Entry", text.get())

    

    

#create the application window    
window = tk.Tk()


#ask for user entry
tk.Label(window, text="Enter something: ").grid(row=0, sticky=tk.E) #label for text
text = tk.Entry(window) #entry box
text.grid(row=0, column=1)  #entry box location


#button to show the input
tk.Button(window, text='Show', command=show_entry).grid(row=1, column=1, sticky=tk.W, pady=4)





