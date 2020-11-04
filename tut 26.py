from tkinter import *
import webbrowser

def gotoweb():
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(f'https://arcticrobotchallenge.com/')

root=Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry(f"{width-300}x{height-300}")
root.maxsize(height=height,width=width)

root.title("   Arctic Robotics")
root.wm_iconbitmap("icon.ico")
root.configure(bg="gray")


print(f"Height: {height}")
print(f"Widht: {width}")

Button(text="Go to Website",command=gotoweb,relief=RIDGE).pack(pady=100)




root.mainloop()