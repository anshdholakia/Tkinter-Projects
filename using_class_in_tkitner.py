# this class creates a gui with button that when pressed updates the button

from tkinter import *
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("GUI for Updating Button text")
        Label(self,text="Type and click on Button",font="Helvetica 17 bold").pack()
        inputting=StringVar()
        self.e1=Entry(self,textvariable=input)
        self.e1.pack(pady=10)

    def create_button(self):
        self.b1=Button(self,text="Change Me!",font="Helvetica 10 bold",relief=RIDGE,command=self.update_it)
        self.b1.pack(pady=20)




    def update_it(self):
        self.b1.destroy()
        if self.e1.get()=="":
            self.b1=Button(self,text="Empty Button",relief=RIDGE,font="Helvetica 10 bold",command=self.update_it)
        else:
            self.b1=Button(self,text=self.e1.get(),font="Helvetica 10 bold",relief=RIDGE,command=self.update_it)
        self.b1.pack(pady=20)
        self.update()



window=GUI()
window.create_button()
window.mainloop()