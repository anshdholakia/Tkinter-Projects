# from tkinter import *
#
#
# def getvalue():
#     print(f"Name: {userentry.get()}\nPassword: {passentry.get()}")
#
# root=Tk()
# root.geometry("400x500")
# root.title("Excel using Tkinter")
# user=Label(root,text="Username: ")
# password=Label(root,text="Password: ")
# user.grid(row=0,pady=5) # grid acts as a packing
# password.grid(row=1,pady=5)
#
# # Variable classes in tkinter
# # BooleanVar, doublevar,IntVar, StringVar
#
# uservalue=StringVar()
# passvalue=StringVar()
#
# userentry=Entry(root,textvariable=uservalue)
# passentry=Entry(root,textvariable=passvalue)
#
#
#
# userentry.grid(row=0, column=1)
# passentry.grid(row=1, column=1)
#
# Button(text="Submit",command=getvalue).grid()
#
# root.mainloop()

from tkinter import *

name_list=[]
dresses_list=[]
age_list=[]


def setitem():
    name_list.append(nameentry.get())
    age_list.append(ageentry.get())
    dresses_list.append(dressentry.get())
    print(f"Name: ",nameentry.get())
    print(f"Age: ",ageentry.get())
    print(f"Dress: ",dressentry.get())

root=Tk()

root.title("----Dancer Information----")

root.geometry("500x600")

Label(text="Name of the Dancer: ").grid(row=0,pady=5)
Label(text="Age of the Dancer: ").grid(row=1,pady=5)
Label(text="Dress of the Dancer: ").grid(row=2,pady=5)

nameget=StringVar
age=IntVar
dress=StringVar

nameentry=Entry(root,textvariable=nameget)
nameentry.grid(row=0,column=1)

ageentry=Entry(root,textvariable=age)
ageentry.grid(row=1,column=1)

dressentry=Entry(root,textvariable=dress)
dressentry.grid(row=2,column=1)

Button(root,text="Submit",padx=20,command=setitem).grid()


root.mainloop()
