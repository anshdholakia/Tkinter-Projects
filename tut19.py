# from tkinter import *
# import tkinter.messagebox as tsmg
# root=Tk()
# root.geometry("400x170")
#
# root.title("GUI By Ansh Dholakia")
#
# def get_dollar():
#     print(f"We have credited {myslider2.get()} dollars to your bank account")
#     tsmg.showinfo(title="Successful",message=f"We have credited {myslider2.get()} dollars to your bank account")
#
# # myslider=Scale(root,from_=0,to=100)
# # myslider.pack()
#
# Label(root,text="How many dollars do you want?").pack()
#
# myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,relief=RIDGE,tickinterval=25)
# myslider2.set(100)
# myslider2.pack()
#
# Button(text="Get Dollars!",pady_=10,command=get_dollar,relief=RIDGE).pack()
#
# root.mainloop()


from tkinter import *
import tkinter.messagebox as tsmg
root=Tk()
root.geometry("400x170")

root.title("Food Rating")

def get_dollar():
    with open("rating.txt","a") as f:
        f.write(f"Rating: {myslider2.get}/5")

    tsmg.showinfo(title="Successful",message=f"Thank you!, your rating is noted")

# myslider=Scale(root,from_=0,to=100)
# myslider.pack()

Label(root,text="Ratings for the Restaurant").pack()

myslider2=Scale(root,from_=0,to=5,orient=HORIZONTAL,relief=RIDGE,tickinterval=5)
myslider2.set(5)
myslider2.pack()

Button(text="Submit Ratings",pady_=10,command=get_dollar,relief=RIDGE).pack()

root.mainloop()
