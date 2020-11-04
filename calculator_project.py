from tkinter import *
root=Tk()
root.title("Calculator | Ansh Dholakia")
root.wm_iconbitmap("icon.ico")
root.geometry("444x450")

count=0

def click(event):
    text=event.widget.cget("text")
    global scvalue
    global count
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
            count=1
        else:
            value=eval(screen.get())
            count=1

        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


def func(start=0,end=0,li=[]):
    if(start-end>0):
        f = Frame(root, bg="black")
        for i in range(len(li)):
            b = Button(f, text=li[i], padx=38, pady=6, font="lucida 10 bold", relief=RIDGE)
            b.pack(side=LEFT, padx=10, pady=12)
            b.bind("<Button-1>", click)
        f.pack()
    elif(start-end<=0):
        f = Frame(root, bg="black")
        for i in range(start, end + 1):
            b = Button(f, text=str(i), padx=38, pady=6, font="lucida 10 bold", relief=RIDGE)
            b.pack(side=LEFT, padx=10, pady=12)
            b.bind("<Button-1>", click)
        f.pack()





scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="montblanc 20 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

# f=Frame(root,bg="black")
# b=Button(f,text="0",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# b=Button(f,text="1",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
#
# b=Button(f,text="2",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# f.pack()

func(0,2)

func(3,5)
func(6,8)
func(5,-1,["9","+","-"])
func(5,-1,["*","/","%"])
func(5,-1,["C","="])
#
# f=Frame(root,bg="black")
# b=Button(f,text="3",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# b=Button(f,text="4",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
#
# b=Button(f,text="5",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# f.pack()

# f=Frame(root,bg="black")
# b=Button(f,text="6",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# b=Button(f,text="7",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
#
# b=Button(f,text="8",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# f.pack()
#
# f=Frame(root,bg="black")
# b=Button(f,text="9",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# b=Button(f,text="+",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
#
# b=Button(f,text="-",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# f.pack()
#
# f=Frame(root,bg="black")
# b=Button(f,text="*",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# b=Button(f,text="/",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
#
# b=Button(f,text="%",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# f.pack()
#
# f=Frame(root,bg="black")
# b=Button(f,text="=",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
# b=Button(f,text="C",padx=38,pady=6,font="lucida 10 bold",relief=RIDGE)
# b.pack(side=LEFT,padx=10,pady=12)
# b.bind("<Button-1>",click)
#
#
#
#
# f.pack()


root.mainloop()