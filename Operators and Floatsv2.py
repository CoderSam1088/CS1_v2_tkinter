import tkinter as tk
from tkinter import messagebox


x = 4.1
y = 5.2
z = 6


# Display a message
messagebox.showinfo("Operators and Floats",        
                    "x + y: " + str(x + y) \
                    +"\nz * 3: " +str(z*3)\
                    +"\nx - z: " + str(x - z)\
                    +"\nz / x: " + str(z/x)\
                    +"\ny ** x: " +str(y**x)\
                    +"\nz * y: " + str(z%y)\
                    +"\n-x: " +str(-x))


