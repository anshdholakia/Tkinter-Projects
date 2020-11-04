from tkinter import *
root=Tk()


def resiz():
    l1=l.get()
    b1=b.get()
    root.geometry(f"{l1}x{b1}")



root.geometry("500x300")


root.title("GUI Window Resizer by Ansh Dholakia")

Label(text="Enter length of window: ",font="comicsansms 13 bold").grid(row=1,column=2)


Label(text="Enter breadth of window: ",font="comicsansms 13 bold").grid(row=2,column=2)


l=StringVar()
b=StringVar()

e1=Entry(root,textvariable=l).grid(row=1,column=3,pady=27,ipady=5)
e2=Entry(root,textvariable=b).grid(row=2,column=3,pady=7,ipady=5)

button=Button(root,text="Apply Changes",font="lucida 14 bold",relief=RIDGE,command=resiz).grid(row=3,column=2,pady=10)



root.mainloop()