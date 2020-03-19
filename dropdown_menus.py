from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Learningtkinter.com')
root.iconbitmap('c:/Users/Pete/PycharmProjects/tkinter_tutorial/images/canna.ico')
root.geometry('400x400')

#drop down menu

def show():
    mylabel = Label(root, text=clicked.get()).pack()

options = [
    'vegetable',
    'pepperoni',
    'cheese',
    'meatdylax',
    'chicken periperi'

]

clicked = StringVar()
clicked.set('PIZZA')

drop = OptionMenu(root, clicked, *options)
drop.pack()

mybutton = Button(root, text='Show Selection', command=show ).pack()

root.mainloop()