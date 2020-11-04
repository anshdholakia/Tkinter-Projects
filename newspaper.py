from tkinter import *
from PIL import Image,ImageTk

root=Tk()

root.geometry("800x600")

def every_100(text):
    final_text=""
    for i in range(0,len(final_text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+='\n'

    return final_text



texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt","r") as f:
        texts.append(every_100(f.read()))


    image=Image.open(f"{i+1}.png")
    # TODO: resize these images
    image=image.resize((225,225),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0=Frame(root,width=300, height=160)
Label(f0,text="Ansh Dholakia News",font="lucida 15 bold").pack()
f0.pack()

f1=Frame(root,width=200,height=100, pady=34)
Label(f1,text=texts[0],font="lucida 9 bold",padx=30,pady=30).pack(side=LEFT)
Label(f1,image=photos[0],anchor="e").pack(side=LEFT)
f1.pack(anchor="w")

f2=Frame(root,width=200,height=100, pady=34)
Label(f2,text=texts[1],font="lucida 9 bold",padx=30,pady=30).pack(side=LEFT)
Label(f2,image=photos[1],anchor="e").pack(side=LEFT)
f2.pack(anchor="w")

f3=Frame(root,width=200,height=100, pady=34)
Label(f3,text=texts[2],font="lucida 9 bold",padx=30,pady=30).pack(side=LEFT)
Label(f3,image=photos[2],anchor="e").pack(side=LEFT)
f3.pack(anchor="w")







root.mainloop()