from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learningtkinter.com')
root.iconbitmap('C:/Users/Pete/PycharmProjects/tkinter_tutorial/images/canna.ico')

#r =IntVar()
#r.set(2)

TOPPINGS =[
    ('pepperoni','pepperoni'),
    ('cheese','cheese'),
    ('mushrooms','mushrooms'),
    ('onions','onions'),
]

pizza = StringVar()
pizza.set('pepperoni')

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

#Radiobutton(root, text='option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text='option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text='click me!', command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()