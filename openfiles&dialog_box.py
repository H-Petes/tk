from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Learningtkinter.com')
root.iconbitmap('c:/Users/Pete/PycharmProjects/tkinter_tutorial/images/canna.ico')



def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='c:/Users/Pete/PycharmProjects/tkinter_tutorial/images', title='Select A File', filetypes=(('JPG files', '*.jpg'), ('all files', '*.*')))
    my_Label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text='Open file', command=open).pack()


root.mainloop()