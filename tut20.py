from tkinter import *
import tkinter.messagebox as tsmg

root=Tk()
root.geometry("400x300")
root.title("Radio Buttons")

def order():
    tsmg.showinfo(title="Order Successful",message=f"We have received your order for {var.get()}.\nThanks for Ordering")

# var=IntVar()
var=StringVar()
var.set("Radio")
# var.set(1)
Label(root,text="What do you like to have sir?",font="Leckerli_One 19 bold",justify=LEFT,padx=14).pack()

radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Idli",padx=14,variable=var,value="Idli").pack(anchor="w")
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value="Samosa").pack(anchor="w")
radio=Radiobutton(root,text="Naan",padx=14,variable=var,value="Naan").pack(anchor="w")

Button(root,text="Order Now!",padx=14,relief=RIDGE,command=order).pack()


root.mainloop()
