from tkinter import *

root=Tk()

root.geometry("800x600")

def getvals():
    print("It works")

# text for our form
Label(root,text="Welcome to Ansh Travels",font="comicsansms 13 bold").grid(row=0,column=3,pady=10)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Contact")
payment=Label(root,text="Payment Mode")

# pack text for our form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)

# Tkinter variables for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentvalue=StringVar()
foodcheckvalue=IntVar()  # check box

# Entries for our form
nameentry=Entry(root,textvariable=namevalue,relief=SUNKEN)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymententry=Entry(root,textvariable=paymentvalue)
foodcheckentry=Entry(root,textvariable=foodcheckvalue)

# packing our entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

# check box
foodservice=Checkbutton(text="Want to prebook your meals?",variable=foodcheckvalue,relief=SUNKEN)
foodservice.grid(row=6,column=3)

# button and packing it and assigning it a command
Button(root,text="Submit to Ansh Travels",command=getvals).grid(row=7,column=3)

root.mainloop()