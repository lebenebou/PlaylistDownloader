
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# main window initiation ====================
mw = Tk()
mw.title('Window Title')
mw_width, mw_height = 300, 200
mw.minsize(mw_width, mw_height)
mw.geometry('+400+200')
# mw.iconbitmap("path/icon.png")
mw.resizable(False, False)

# variables =================================
my_string = StringVar()
my_string.set("I am a string var, use get() to get my value")

# functions =================================
def my_func():

    print("You pressed me!")

# frames - widgets - buttons ================
search_btn = ttk.Button(mw,text="Click me!", command=my_func)
search_btn.place(x=mw_width-93,y=mw_height-35)


# ===========================================
if __name__=="__main__":
    mw.mainloop()