from tkinter import *
root=Tk()
root.geometry("500x300")

def set():
    print("Value Submitted")
root.title("Enter Username and Password")
Label(root,text="Username and Password Program",font="comicsansms 22 bold").grid(row=0,column=4)

namevalue=StringVar()
passwordvalue=StringVar()
value1=IntVar()
value2=IntVar()

nameentry=Label(root,text="Enter Username: ",relief=SUNKEN,borderwidth=4)
passwordentry=Label(root,text="Enter Password: ",relief=SUNKEN,borderwidth=4)


nameentry.grid(row=1,column=2)
passwordentry.grid(row=2,column=2)


namee=Entry(textvariable=namevalue)
passe=Entry(textvariable=passwordvalue)


namee.grid(row=1,column=3)
passe.grid(row=2,column=3)

Button(root,text="Submit Username and Password",command=set).grid(row=4,column=3)







root.mainloop()
