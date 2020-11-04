from tkinter import *

root=Tk()

# WidthxHeight
root.geometry("920x280")


# minsize argumetn: width,height
root.minsize(300,233)

root.maxsize(1000,200)


#label
label=Label(text="Ansh Dholakia GUI")
label.pack()


root.mainloop()
