from tkinter import *


root = Tk()
e = Entry(root, width=50)
e.pack()

def myClick():
    myLabel = Label(root, text='Look, I just clicked a button!')
    myLabel.pack()

myButton = Button(root, text='Click me!', command=myClick, fg='blue', bg='white')
myButton.pack()


root.mainloop()