import tkinter as tk
from tkinter import messagebox


# Display a message
messagebox.showinfo("Operators and Strings",        
                    "hello " + ", world!" \
                    +"\na" + "b" + "c"\
                    +"\n" + "hi" * 3\
                    +"\nhi" + str(3)\
                    +"\nMy bike has " +str(6) + " gears.")


