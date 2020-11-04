from tkinter import *
root=Tk()

def ansh(event):
    print(f"You clicked on the button at {event.x},{event.y}")

def double(event):
    print(f"You double clicked on the button at {event.x}, {event.y}")

root.title("Events in Tkinter")
root.geometry("700x500")

widget=Button(root,text="Click my Please")
widget.pack()

widget.bind('<Button-1>',ansh)
widget.bind('<Double-1>',double)

root.mainloop()