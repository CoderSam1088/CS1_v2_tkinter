import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_people():
    """Function to show input fields"""
    num_people= int(text.get())  #get text from text entry box
    num_teams = int(text1.get()) #get text from text1 entry box

    # The // is the floor division operator. Do some research to see how it differs
    # from the / divison operator.
    people_per_team = num_people // num_teams
    left_over = num_people % num_teams
    
    messagebox.showinfo("Team Sizes", "If there are " +str(num_teams)+ " teams, there will be " + \
                        str(people_per_team) + " on each team, with " +str(left_over)+ " left over.") #Shows the number times 2

    

    

#create the application window    
window = tk.Tk()


tk.Label(window, text="How many people are playing?: ").grid(row=0, sticky=tk.E) #label for text
text = tk.Entry(window) #entry box
text.grid(row=0, column=1)  #entry box location

tk.Label(window, text="How many teams?: ").grid(row=1, sticky=tk.E) #label for text
text1 = tk.Entry(window) #entry box
text1.grid(row=1, column=1)  #entry box location


#button to show the input
tk.Button(window, text='Show', command=show_people).grid(row=2, column=1, sticky=tk.W, pady=4)





