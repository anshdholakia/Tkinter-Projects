from tkinter import *

root=Tk()

root.title("Tutorial 13")

canvas_height=400
canvas_widht=800

root.geometry(f"{canvas_widht}x{canvas_height}")

can_widget=Canvas(root,height=canvas_height,width=canvas_widht)
can_widget.pack()

# line goes to the point form x1,y1 to x2,y2
can_widget.create_line(0, 0 ,800, 400,fill="blue")
can_widget.create_line(0, 400 ,800, 0,fill="red")

# creating rectangle - syntax .create_rectangle(coordinates of top-left, coordinates of bottom-right)
# can_widget.create_rectangle(1,1,799,799,fill="green")
can_widget.create_rectangle(200,200,400,400,fill="green")


# to fit text in gui
can_widget.create_text(200,200,text="Python GUI")

# creating an oval
can_widget.create_oval(200,200,400,400) # an oval in tkinter requires coordinates similar to rectangle, those coordinates are of a rectangle that encompasses the oval


# can_widget.create_polygon(200,200,400,400,300,300,100,100,200,200,fill="blue")
# can_widget.create_arc(300,300,700,700)





root.mainloop()
