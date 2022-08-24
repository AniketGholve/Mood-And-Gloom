import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
import emotion_1 as validate
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="yellow")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Automatic Mood And Gloom Detection Through Visual Inputs")

# 430
#######lbl = tk.Label(root, text="Diabetic Retinopathy Detection System", font=('times', 35,' bold '), height=1, width=30,bg="seashell2",fg="indian red")
########lbl.place(x=350, y=5)
# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('2.jpg')
image2 = image2.resize((1800, 800), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

img=ImageTk.PhotoImage(Image.open("2.jpg"))


img2=ImageTk.PhotoImage(Image.open("4.jpg"))


#img3=ImageTk.PhotoImage(Image.open("4.jpg"))

logo_label=tk.Label()
logo_label.place(x=0,y=50)

x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img)
	elif x == 2:
		logo_label.config(image=img2)
#	elif x == 3:
#		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()
# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Automatic Mood And Gloom Detection Through Visual Input", font=("Times New Roman", 25, 'bold'),
                    background="black", fg="white", width=100, height=2)
label_l1.place(x=0, y=0)

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)

def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=50, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=500, y=500)
#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



def evaluation():
        # from subprocess import call
        # call(['python','detection_emotion_practice.py'])
        validate.upload()
        

def prediction_emotion():
    #clear_img()
    #update_label("Model Training Start...............")

    start = time.time()

    result = validate.files_count()
    #validate.files_count()
    end = time.time()
    #print("---" + result)
    ET = "Execution Time: {0:.4} seconds \n".format(end - start)

    msg = "Mood Detected " + '\n' + str(result) + '\n'+ ET

    update_label(msg)
#################################################################################################################
def window():
    root.destroy()



button3 = tk.Button(root, text="Find Evaluation",command=evaluation,width=22, height=1,font=('times', 15, ' bold '), bg="cornsilk2", fg="black")
button3.place(x=825, y=180)

button4 = tk.Button(root, text="Prediction",command=prediction_emotion, width=22, height=1, bg="cornsilk2", fg="black",font=('times', 15, ' bold '))
button4.place(x=825, y=240)

exit = tk.Button(root, text="Exit", command=window, width=10, height=1, font=('times', 15, ' bold '), bg="red",fg="white")
exit.place(x=892, y=300)

root.mainloop()