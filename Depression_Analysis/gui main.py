from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.title("Automatic Mood And Depression Detection Through Visual Input")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

bg = Image.open(r"D:\\Depression_Analysis\\Depression_Analysis\\y8.jpg")
bg.resize((1900,900),Image.ANTIALIAS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="Automatic Mood And Gloom Detection Through Visual Input",width=130,background="cornsilk1",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="slategray4")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login1.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


wlcm=tk.Label(root,text="......Welcome To Mood And Gloom Detection Using Visual Input ......",width=120,height=2,background="cornsilk1",foreground="black",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=650)




d2=tk.Button(root,text="Login",command=Login,width=9,height=2,bd=0,background="skyblue",foreground="black",font=("times new roman",14,"bold"))
d2.place(x=1600,y=18)


d3=tk.Button(root,text="Register",command=Register,width=9,height=2,bd=0,background="skyblue",foreground="black",font=("times new roman",14,"bold"))
d3.place(x=1700,y=18)



root.mainloop()
