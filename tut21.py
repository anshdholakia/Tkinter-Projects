from tkinter import *


root=Tk()
root.geometry("400x200")
root.title("Listbox Tutorial")

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1


i=0
lbx=Listbox(root)

lbx.pack()

lbx.insert(END,"First Item of the listbox")

Button(root,text="Add item!",command=add).pack()


root.mainloop()