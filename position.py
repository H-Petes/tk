from tkinter import *


root = Tk()

# creating a label widget
myLabel = Label(root, text='hello world!')
myLabel2 = Label(root, text='My name is petes')

# shoving on the screen
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()