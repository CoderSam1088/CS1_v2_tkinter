
"""
This program asks the user for a number. It then
prints the result when that number is multiplied
by two.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_twice():
    """Function to show input fields"""
    number = int(text.get())
    messagebox.showinfo("Sum", "Twice that number is: " +str(number*2)) #Shows the number times 2

    

    

#create the application window    
window = tk.Tk()

# Ask the user for a number
tk.Label(window, text="Enter a number: ").grid(row=0) #label for text
text = tk.Entry(window) #entry box
text.grid(row=0, column=1)  #entry box location


#button to show the input
tk.Button(window, text='Show', command=show_twice).grid(row=2, column=1, sticky=tk.W, pady=4)





