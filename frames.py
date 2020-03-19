from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learningtkinter.com')
root.iconbitmap('C:/Users/Pete/PycharmProjects/tkinter_tutorial/images/canna.ico')

frame = LabelFrame(root, text='This is my frame ', padx=5, pady=5)
frame.pack(padx=100, pady=100)

b = Button(frame, text='Do not click!')
b.pack()




root.mainloop()