from tkinter import *

class GUI(Tk):
    # window is the self now as it is the object
    def __init__(self):
        super().__init__()
        self.geometry("500x300")

    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvar=self.var,relief=RIDGE,anchor=W)
        self.statusbar.pack(side=BOTTOM,fill=X)

    def click(self):
        print("Button click")

    def createbutton(self,inptext):
        Button(self,text=inptext,command=self.click).pack()
if __name__ == '__main__':
    # root is now window
    window=GUI()
    window.status()
    window.createbutton("Click now")
    window.mainloop()
