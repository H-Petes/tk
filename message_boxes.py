from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learningtkinter.com')
root.iconbitmap('C:/Users/Pete/PycharmProjects/tkinter_tutorial/images/canna.ico')



def Popup():
     response = messagebox.askquestion('This is my popup', 'Hello World!')
     #Label(root, text=response).pack()
     if response == 'yes':
        Label(root, text='You clicked yes!').pack()
     else:
         Label(root, text='You clicked no!').pack()

Button(root, text='Popup', command=Popup).pack()


root.mainloop()