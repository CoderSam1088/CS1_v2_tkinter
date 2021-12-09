import tkinter as tk
from tkinter import messagebox

# should print the value 2
int_division1 = 4 // 2


# Should print the float 2.0
real_division1 = 4 / 2


# 2 divided by 4 is 0.5, but it gets truncated to 0
int_division2 = 2 // 4


# Since this is returning a float, it prints 0.5
real_division2 = 2 / 4


messagebox.showinfo("This is the title",        #you put a comma after the title
                    str(int_division1)\
                    +"\n"+str(real_division1)\  #add "\n" to start a new line.
                    +"\n"+str(int_division2)\
                    +"\n"+str(real_division2))


