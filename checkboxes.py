from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Learningtkinter.com')
root.iconbitmap('c:/Users/Pete/PycharmProjects/tkinter_tutorial/images/canna.ico')
root.geometry('400x400')

def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text='PIZZA', variable=var, onvalue='supersize', offvalue='regular')
c.deselect()
c.pack()



mybutton = Button(root, text='Show Selection', command=show).pack()


root.mainloop()