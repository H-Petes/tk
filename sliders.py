from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Learningtkinter.com')
root.iconbitmap('c:/Users/Pete/PycharmProjects/tkinter_tutorial/images/canna.ico')
root.geometry('400x400')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide():
    my_Label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()

#my_Label = Label(root, text=horizontal.get()).pack()


my_btn = Button(root, text='click me!', command=slide).pack()

root.mainloop()