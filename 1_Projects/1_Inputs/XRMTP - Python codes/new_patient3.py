# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:06:18 2019

@author: lafagev
"""

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
              
var = StringVar()
var.set("one")
data=("BNI", "BSC", "CED", "COL","HSS", "JHU", "KS_", "LOU","MGH", "NLS", "NYU", "OHS","RUM", "SDS", "UCA", "UCD","UFL", "UMF", "UMI", "UPM", "USF", "UVA", "WUN")
cb=Combobox(window, values=data)
cb.place(x=100, y=200)

#Gender

v0=IntVar()
v0.set(1)
gender_title =Label (window,text="Gender", font=("Arial", 10),bg='#EEF9FF',fg='#454545')
r1_gender=Radiobutton(window, text="Male",font=("Arial", 10), variable=v0,value=1,background='#EEF9FF')
r2_gender=Radiobutton(window, text="Female", font=("Arial", 10),variable=v0,value=2,background='#EEF9FF')
gender_title.place(x=50,y=50)
r1_gender.place(x=100,y=50)
r2_gender.place(x=180, y=50)
               
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Cricket", variable = v1,background='#EEF9FF')
C2 = Checkbutton(window, text = "Tennis", variable = v2,background='#EEF9FF')
C1.place(x=100, y=100)
C2.place(x=180, y=100)

patientID_title=Label (window,text="Patient ID", font=("Arial", 10),bg='#EEF9FF',fg='#454545')
patient_number=Entry(window,bd=5)
patientID_title.place(x=20,y=0)
patient_number.place(x=100,y=0)

frame=Frame(window,bg='#EEF9FF')
Quit_bttn=Button(frame,text="Quit", font=("Arial",10),bg='#E7E7E7',fg='#FE4E4E',command=window.destroy)
Quit_bttn.pack(pady=25)
frame.pack(expand=YES)

window.mainloop()