from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("Ansh Dholakia's GUI")
f1=Frame(root,bg="grey",borderwidth=7, relief=SUNKEN)

f2=Frame(root,bg="blue",borderwidth=7,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
f1.pack(side=LEFT,fill=Y)
l=Label(f1,text="Project Tkinter - Pycharm")
l.pack(pady=134)
l=Label(f2,text="Welcome to Sublime Text", font="Helvatica 23 bold",fg="red")
l.pack(pady=34)


root.mainloop()
