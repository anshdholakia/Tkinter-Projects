from tkinter import *
root=Tk()
root.geometry("500x300")
root.title("Status bar tutorial")

def upload():
    import time
    status_var.set("Busy...")
    sbar.update()
    time.sleep(4)
    status_var.set("Ready")

status_var=StringVar()
status_var.set("Ready")
sbar=Label(root,textvariable=status_var,relief=SUNKEN,anchor=W)
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=upload,relief=RIDGE).pack()


root.mainloop()
