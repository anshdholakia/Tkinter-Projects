from tkinter import *
root=Tk()
root.geometry("400x200")
root.title("Scrollbar tutorial")
# TODO: for connecting a scroll bar to a widget:
# 1) widget(yscrollcommand=scrollbar.set)
# 2) scrollbar.config(command=widget.yview)

scrollbar=Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)

# listbox=Listbox(root,yscrollcommand=scrollbar.set)
# for i in range(344):
#     listbox.insert(END,f"Item {i}")

# listbox.pack(fill=BOTH,padx=22)
# text=Text(root,yscrollcommand=scrollbar.set)
# text.pack(fill=BOTH,padx=22)


# scrollbar.config(command=listbox.yview)
# scrollbar.config(command=text.yview)


root.mainloop()

'''
from tkinter import *
root=Tk()
frame=Frame(root,width=300,height=300)
frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
hbar=Scrollbar(frame,orient=HORIZONTAL)
label=Label(canvas,text="H\ne\nl\nl\no\n \nW\no\nr\nl\nd\n",font="Helvetica 70 bold")
label.pack(side="top")
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

root.mainloop()
'''