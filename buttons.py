from tkinter import *


root = Tk()

def myClick():
    myLabel = Label(root, text='Look, I just clicked a button!')
    myLabel.pack()

myButton = Button(root, text='Click me!', command=myClick, fg='green', bg='red')
myButton.pack()


root.mainloop()