import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_people():
    """Function to show input fields"""
    # Ask for the length of the two
    # parallel sides - base and top
    base = int(text.get())
    top = int(text1.get())

    # Ask for the height
    height= int(text2.get())

    # Compute and print the area of the
    # trapezoid.
    area = 0.5 * (base + top) * height

    #Show the trapezoid area
    messagebox.showinfo("Trapezoid", "Area: " +str(area))

    

    

#create the application window    
window = tk.Tk()


#ask a user for a number
tk.Label(window, text="Base: ").grid(row=0, sticky=tk.E) #label for text
text = tk.Entry(window) #entry box
text.grid(row=0, column=1)  #entry box location

#ask a user for a number
tk.Label(window, text="Top: ").grid(row=1, sticky=tk.E) #label for text
text1 = tk.Entry(window) #entry box
text1.grid(row=1, column=1)  #entry box location

#ask a user for a number
tk.Label(window, text="Height: ").grid(row=2, sticky=tk.E) #label for text
text2 = tk.Entry(window) #entry box
text2.grid(row=2, column=1)  #entry box location


#button to show the input
tk.Button(window, text='Show', command=show_people).grid(row=3, column=1, sticky=tk.W, pady=4)





