import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_people():
    """Function to show input fields"""

    #print x as it is
    x = int(text.get())
    messagebox.showinfo("Print x",x)


    #convert x to integer and print type
    x = int(x)
    messagebox.showinfo("int(x)", str(type(x)))

    
    #print x + 3
    messagebox.showinfo("x + 3", x + 3)

    

    

#create the application window    
window = tk.Tk()


#ask a user for a number
tk.Label(window, text="Enter a number: ").grid(row=0, sticky=tk.E) #label for text
text = tk.Entry(window) #entry box
text.grid(row=0, column=1)  #entry box location



#button to show the input
tk.Button(window, text='Show', command=show_people).grid(row=1, column=1, sticky=tk.W, pady=4)





