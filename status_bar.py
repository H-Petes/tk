from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learningtkinter.com')
root.iconbitmap('c:/Users/Pete/PycharmProjects/tkinter_tutorial/images/canna.ico')


my_img1 = ImageTk.PhotoImage(Image.open('c:/Users/Pete/PycharmProjects/tkinter_tutorial/images/1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('c:/Users/Pete/PycharmProjects/tkinter_tutorial/images/2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('c:/Users/Pete/PycharmProjects/tkinter_tutorial/images/3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('c:/Users/Pete/PycharmProjects/tkinter_tutorial/images/4.jpg'))



image_list = [my_img1,my_img2, my_img3, my_img4]

status = Label(root, text='image 1 out of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_Label = Label(image=my_img1)
my_Label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_Label
    global button_forward
    global button_back

    my_Label.grid_forget()
    my_Label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))

    if image_number == 4:
        button_forward = Button(root, text='>>', state=DISABLED)

    my_Label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text='image '+ str(image_number) + ' out of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)



def back(image_number):
    global my_Label
    global button_forward
    global button_back

    my_Label.grid_forget()
    my_Label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    my_Label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    status = Label(root, text='image '+ str(image_number) + ' out of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit Program', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)




root.mainloop()