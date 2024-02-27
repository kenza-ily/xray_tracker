# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:48:07 2019

@author: lafagev
"""

from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
window.title("New Patient")
window.config(background='#EEF9FF')
window.geometry("1000x600")
window.minsize(480,360)
window.maxsize(2000,1000)
window.iconbitmap("HSS-monogram-logo_1400.ico")              

#Title of the window
title_frame=frame(window,bg='#EEF9FF')
window_title =Label (title_frame,text="Patient details", font=("Arial", 25),bg='#EEF9FF',fg='#454545')
                     
                     
#Study              
var = StringVar()
var.set("one")
data=("BNI", "BSC", "CED", "COL","HSS", "JHU", "KS_", "LOU","MGH", "NLS", "NYU", "OHS","RUM", "SDS", "UCA", "UCD","UFL", "UMF", "UMI", "UPM", "USF", "UVA", "WUN")
study_frame=Frame(window,bg='#EEF9FF')
study_title =Label (study_frame,text="Study", font=("Arial", 10),bg='#EEF9FF',fg='#454545')
cb=Combobox(study_frame, values=data)
study_title.grid(row=0,column=1);cb.grid(row=0,column=2)
study_frame.grid(row=0,column=0,rowspan = 1, columnspan = 3)
study_frame.pack(expand=YES)

#Gender
gender_frame=Frame(window,bg='#EEF9FF')
v0=IntVar()
v0.set(1)
gender_title =Label (gender_frame,text="Gender", font=("Arial", 10),bg='#EEF9FF',fg='#454545')
r1_gender=Radiobutton(gender_frame, text="Male", variable=v0,value=1,background='#EEF9FF')
r2_gender=Radiobutton(gender_frame, text="Female", variable=v0,value=2,background='#EEF9FF')
gender_title.grid(row=0,column=1); r1_gender.grid(row=0,column=2);r2_gender.grid(row=0,column=3)
study_frame.grid(row=0,column=1,rowspan = 1, columnspan = 3)
gender_frame.pack(expand=YES)
               
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Cricket", variable = v1,background='#EEF9FF')
C2 = Checkbutton(window, text = "Tennis", variable = v2,background='#EEF9FF')
C1.place(x=100, y=100)
C2.place(x=180, y=100)

patient_number=Entry(window,bd=5)
patient_number.place(x=100,y=50)


window.mainloop()