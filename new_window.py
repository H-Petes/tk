from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Learningtkinter.com')
root.iconbitmap('C:/Users/Pete/PycharmProjects/tkinter_tutorial/images/canna.ico')

def open():
    global my_img
    top = Toplevel()
    top.title('my second window')
    top.iconbitmap('C:/Users/Pete/PycharmProjects/tkinter_tutorial/images/canna.ico')
    my_img = ImageTk.PhotoImage(Image.open('images/2.jpg`'))
    my_Label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='close window', command=top.destroy).pack()



btn = Button(root, text='open second window', command=open).pack()





root.mainloop()