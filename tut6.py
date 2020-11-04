from tkinter import *
root=Tk()
root.geometry("444x233")
root.title("My GUI with Harry")

# Important Labels
# text-adds the text
# bg-background
# fg-foreground
# font-sets font # font=("Leckli_One",23,"bold")
# padx - padding x
# pady- padding y
# relief- border styling- SUNKEN, RAISED, GROOVE, RIDGE

title_label=Label(text="Ansh is a really good boy as he makes python projects for real life events",
                  bg="green",fg="blue",padx=20,pady=20,font=("Leckli_One 23 bold"),borderwidth=4,relief=SUNKEN)

# Important Pack Options
# anchor-nw,we,se,sw
# side- botton, top, left, right
# fill- BOTH, X or Y
# padx-
# pady-



title_label.pack(side=RIGHT,anchor="nw",fill=BOTH)
root.mainloop()


# from tkinter import *
# root=Tk()
# root.geometry("500x400")
# label=Label(text="Ready",borderwidth=5,relief=SUNKEN,font="sansserif 28 bold", bg="yellow", fg="blue", padx=20, pady=12)
# label.pack(side=BOTTOM,fill=X)
# root.mainloop()
