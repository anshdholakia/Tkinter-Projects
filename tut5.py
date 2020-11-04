# hwo to show image in tkinter

from tkinter import *
from PIL import ImageTk,Image
root = Tk()

root.geometry("455x244")

# photo = PhotoImage(file="C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\VAR\\goal.png")
# for jpg images
image=Image.open('filename')
photo=ImageTk.PhotoImage(image)
label_of_image=Label(image=photo)
label_of_image.pack()



root.mainloop()