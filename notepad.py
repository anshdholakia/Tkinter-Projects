from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            # Save as a new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad made By Ansh Dholakia")

if __name__ == '__main__':
    # Basic tkitner setup
    root=Tk()
    root.wm_iconbitmap("iconn.ico")
    root.geometry("600x500")
    root.title("Notepad by Ansh Dholakia")

    # Text Area
    TextArea=Text(root,font="Montblanc 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)

    # Menu Bar
    Menubar=Menu(root)

    # File menu starts
    Filemenu=Menu(Menubar, tearoff=0)

    # Open new file
    Filemenu.add_command(label="New",command=newFile)

    # To open existing file
    Filemenu.add_command(label="Open",command=openFile)

    # To save the current file
    Filemenu.add_command(label="Save",command=saveFile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit",command=quitApp)
    Menubar.add_cascade(label="File",menu=Filemenu)
    # File menu ends

    # Edit Menu starts
    EditMenu=Menu(Menubar,tearoff=0)
    # To cut
    EditMenu.add_command(label="Cut", command=cut)

    # To copy
    EditMenu.add_command(label="Copy", command=copy)

    # To Paste
    EditMenu.add_command(label="Paste", command=paste)

    Menubar.add_cascade(label="Edit",menu=EditMenu)

    # Edit Menu ends

    # Help menu starts
    HelpMenu=Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=HelpMenu)

    # Help menu Ends

    root.config(menu=Menubar)

    # Adding scrollbar
    scroll=Scrollbar(TextArea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)

    root.mainloop()