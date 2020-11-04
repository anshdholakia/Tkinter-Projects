from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()

root.geometry("700x300")
root.title("PyCharm")


def funct():
    print("I am a really good function")

def help():
    print("I will help you")
    tmsg.showinfo(title="Help",message="PyCharm will help you with this GUI")
    # tmsg.askyesno(title="Do you really want Help?",message="The GUI will send people to help you at your location")

def rate():
    print("Rate us")
    output=tmsg.askquestion(title="Was your experience good?",message="Was your experience good?")
    print(output)
    if output=="yes":
        tmsg._show("Thank you","You may win a Google Pixel if you follow the next step!")
        msg="Great rate us on the PlayStore please"
    else:
        tmsg.showerror("Not possible","It cannot be possible to dislike our GUI!")
        msg="Tell you what went wrong we will call you soon!"
    tmsg.showinfo(title="Experience with the GUI",message=msg)

def uninstall():
    print("Uninstall")
    ans=tmsg.askretrycancel(title="Uninstall",message="Do you really want to uninstall the GUI?")

    if ans:
        tmsg.showwarning("Are you sure!",message="This can cause a serious imbalance in the system environment!")
        tmsg.askyesnocancel("Confirm","Are you sure?")

        print("Done!")
    else:
        print("Welcome back to the GUI. Happy to see that you changed your mind! :)")


# to create a non-drop down menu
# mymenu=Menu(root)
# mymenu.add_command(label="File",command=funct)
# mymenu.add_command(label="Quit",command=quit)
# root.config(menu=mymenu)

mainmenu=Menu(root)
# to remove the dotted line for making the menu in a different window
m1=Menu(mainmenu,tearoff=0)

m1.add_command(label="New Project",command=funct)
m1.add_command(label="Save",command=funct)
# to add a line in the menu
m1.add_separator()
m1.add_command(label="Save As",command=funct)
m1.add_command(label="Print",command=funct)



m2=Menu(mainmenu,tearoff=0)

m2.add_command(label="Cut",command=funct)
m2.add_command(label="Copy",command=funct)

m2.add_command(label="Paste",command=funct)
m2.add_command(label="Delete",command=funct)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate Us",command=rate)
m3.add_command(label="Uninstall",command=uninstall)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="File",menu=m1)
mainmenu.add_cascade(label="Edit",menu=m2)
mainmenu.add_cascade(label="Help",menu=m3)


root.mainloop()