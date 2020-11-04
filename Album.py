import os
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("1080x1080")
root.minsize(1020,1080)
l1=Label(text="Album")
l1.pack()

for i in range(0,len(os.listdir('E:\My Pictures\Camera Roll'))):
    if i==0:
        continue
    else:
        a=os.listdir('E:\\My Pictures\\Camera Roll')[i]
        print(a)
        print(f'E:\\My Pictures\\Camera Roll\\{a}')
        Label(image=ImageTk.PhotoImage(Image.open(f'E:\\My Pictures\\Camera Roll\\{a}'))).pack()
root.mainloop()