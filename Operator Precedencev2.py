import tkinter as tk
from tkinter import messagebox


x = 3
y = 7
z = x * - (y - 1) %  4


# Display a message
messagebox.showinfo("Operator Precedence",        
                    str(-5 + 4 * 2 % 3 - 1) \
                    +"\n" +str(-5 + 4 * 2 % (3 - 1))\
                    +"\n" + str(z))


