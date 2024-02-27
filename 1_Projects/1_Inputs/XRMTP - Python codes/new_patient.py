# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:31:23 2019

@author: lafagev
"""

from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
var = StringVar()
var.set("one")
data=("one", "BSC", "CED", "HSS")
cb=Combobox(window, values=data)
cb.place(x=60, y=150)

lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=250, y=150)

v0=IntVar()
v0.set(1)
r1_gender=Radiobutton(window, text="Male", variable=v0,value=1)
r2_gender=Radiobutton(window, text="Female", variable=v0,value=2)
r1_gender.place(x=100,y=50)
r2_gender.place(x=180, y=50)
                
v1 = IntVar()
v1.set(1)
v2 = IntVar()
r1_study = Radiobutton(window, text = "BNI", variable = v1,value=1）
r2_study = Radiobutton(window, text = "BSC", variable = v2,value=1)
#r3_study = Radiobutton(window, text = "CED", variable = v3)
#r4_study = Radiobutton(window, text = "COL", variable = v4)
#r5_study = Radiobutton(window, text = "HSS", variable = v5)
#r6_study = Radiobutton(window, text = "JHU", variable = v6)
#r7_study = Radiobutton(window, text = "KS_", variable = v7)
#r8_study = Radiobutton(window, text = "LOU", variable = v8)
#r9_study = Radiobutton(window, text = "MGH", variable = v9)
#r10_study = Radiobutton(window, text = "NLS", variable = v10)
#r11_study = Radiobutton(window, text = "NYU", variable = v11)
#r12_study = Radiobutton(window, text = "OHS", variable = v12)
#r13_study = Radiobutton(window, text = "RUM", variable = v13)
#r14_study = Radiobutton(window, text = "SDS", variable = v14)
#r15_study = Radiobutton(window, text = "UCA", variable = v15)
#r16_study = Radiobutton(window, text = "UCD", variable = v16)
#r17_study = Radiobutton(window, text = "UFL", variable = v17)
#r18_study = Radiobutton(window, text = "UMF", variable = v18)
#r19_study = Radiobutton(window, text = "UMI", variable = v19)
#r20_study = Radiobutton(window, text = "UPM", variable = v20)
#r21_study = Radiobutton(window, text = "USF", variable = v21)
#r22_study = Radiobutton(window, text = "UVA", variable = v22)
#r23_study = Radiobutton(window, text = "WUN", variable = v23)
r1_study.place(x=100, y=100)
r2_study.place(x=180, y=100)

window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()