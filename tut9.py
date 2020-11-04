from tkinter import *
root=Tk()
frame=Frame(root,borderwidth=8,relief=SUNKEN,bg="red")
frame.pack(side=LEFT, anchor="nw")

def hello():
    print("My First name")

def surname():
    print("Second name")

def surname2():
    print("Last name")

def channel():
    print("This is my Channel")

b1=Button(frame,text="Haris",fg="blue",command=hello)
b1.pack(side=LEFT,padx=14,pady=6)

b2=Button(frame,text="Ali",fg="blue",command=surname)
b2.pack(side=LEFT,padx=14,pady=6)

b3=Button(frame,text="Khan",fg="blue",command=surname2)
b3.pack(side=LEFT,padx=14,pady=6)

b4=Button(frame,text="CodeWithHarry",fg="blue",command=channel)
b4.pack(side=LEFT,padx=14,pady=6)

root.mainloop()
