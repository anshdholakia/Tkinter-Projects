from tkinter import *
root=Tk()

root.geometry("700x300")
root.title("PyCharm")


def funct():
    print("I am a really good function")

# to create a non-drop down menu
# mymenu=Menu(root)
# mymenu.add_command(label="File",command=funct)
# mymenu.add_command(label="Quit",command=quit)
# root.config(menu=mymenu)

mainmenu=Menu(root)
# to remove the dotted line for making the menu in a different window
m1=Menu(mainmenu,tearoff=0)

m1.add_command(label="New Project",command=funct)
m1.add_command(label="Save",command=funct)
# to add a line in the menu
m1.add_separator()
m1.add_command(label="Save As",command=funct)
m1.add_command(label="Print",command=funct)
root.config(menu=mainmenu)


m2=Menu(mainmenu,tearoff=0)

m2.add_command(label="Cut",command=funct)
m2.add_command(label="Copy",command=funct)

m2.add_command(label="Paste",command=funct)
m2.add_command(label="Delete",command=funct)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="File",menu=m1)
mainmenu.add_cascade(label="Edit",menu=m2)


root.mainloop()