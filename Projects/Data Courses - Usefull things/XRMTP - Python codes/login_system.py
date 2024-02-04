# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:03:23 2019

@author: lafagev
"""

from tkinter import *
import os


bg_color='#EEF9FF'


def register_user():
    username_info=username.get()
    password_info=password.get()
    
    file=open(username_info,"w")
    file.write(username_info+"/n") #Mettre lantislash a la place
    file.write(password_info)
    file.close()
    
    username_entry.delete(0,END)
    password_entry.delete(0,END) #Clears the field once the users registers 
    
    Label(register_screen,background=bg_color,text="Successful Registration",font=("Arial",11)).pack()
    
def login_verify():
    
    username1=username_verify.get()
    password1=password_verify.get()
    
    username_entry_v.delete(0,END)
    password_entry_v.delete(0,END)
    
    list_of_files=os.listdir() #opens all the files in the open folder
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        if password1 in verify:
            print("login success")
        else:
            print("Wrong password")
    else:
        print("User not found !")
        
    
def loginn():
    global login_screen
    login_screen=Toplevel(window)
    login_screen.title(("X-Rays Measurements Tracking Platform")
    
  #  login_screen.geometry("1000x600")
  #  login_screen.minsize(480,360)
  #  login_screen.maxsize(2000,1000)
   # login_screen.iconbitmap("HSS-monogram-logo_1400.ico")
    #login_screen.config(background=bg_color)
    
    #Label(login_screen,text="Login",bg=bg_color,font=("Arial",10)).pack()
    
   # global username_verify
    #global password_verify
    #global username_entry_v
    #global password_entry_v
    username_verify=StringVar()
    password_verify=StringVar()
    username_entry_v=StrinVar()
    password_entry_v=StringVar()
    
    Label(login_screen,text="Please enter details below to log in",background='#EEF9FF',font=("Arial",18)).pack()
    Entry(login_screen,textvariable=username)
    Label(login_screen,text="Username*",background=bg_color,font=("Arial",20)).pack()
    username_entry_v=Entry(login_screen,textvariable=username_verify)
    username_entry_v.pack()
    Label(login_screen,text="",background=bg_color,font=("Arial",20)).pack()    
    Label(login_screen,text="Password*",background=bg_color,font=("Arial",20)).pack()
    password_entry_v=Entry(login_screen,textvariable=password_verify)
    password_entry_v.pack()
    Label(login_screen,text="",background='#EEF9FF',font=("Arial",20)).pack() 
    Button(login_screen,text="Log in",font=("Arial",20),command=login_verify).pack()     

             

def register():
    global register_screen
    register_screen=Toplevel(window)
    register_screen.title("X-Rays Measurements Tracking Platform")
    register_screen.config(background=bg_color) #We can change the background color
    register_screen.geometry("1000x600")
    register_screen.minsize(480,360)
    register_screen.maxsize(2000,1000)
    register_screen.iconbitmap("HSS-monogram-logo_1400.ico")
    
    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()
    
    
    Label(register_screen,text="Please enter details below",background='#EEF9FF',font=("Arial",18)).pack()
    Entry(register_screen,textvariable=username)
    Label(register_screen,text="Username*",background=bg_color,font=("Arial",20)).pack()
    username_entry=Entry(register_screen,textvariable=username)
    username_entry.pack()
    Label(register_screen,text="",background=bg_color,font=("Arial",20)).pack()    
    Label(register_screen,text="Password*",background=bg_color,font=("Arial",20)).pack()
    password_entry=Entry(register_screen,textvariable=password)
    password_entry.pack()
    Label(register_screen,text="",background='#EEF9FF',font=("Arial",20)).pack() 
    Button(register_screen,text="Register",font=("Arial",20),command=register_user).pack()     
          

          

def main_screen():
    global window
    window=Tk()
    window.title("X-Rays Measurements Tracking Platform")
    #Couleur
    window.config(background=bg_color) #We can change the background color
    #Taille
    window.geometry("1000x600")
    window.minsize(480,360)
    window.maxsize(2000,1000)
    window.iconbitmap("HSS-monogram-logo_1400.ico")
    Label(window,text="X-Rays Measurements Tracking Platform",bg='#EEF9FF',font=("Arial",20)).pack()
    Label(window,text="User Acess",bg='#EEF9FF',font=("Arial",18)).pack()
    Label(window,text="",background='#EEF9FF',font=("Arial",16)).pack()
    Button(window,text="Login",command=login,font=("Arial",16)).pack()
    Label(window,text="",background='#EEF9FF',font=("Arial",16)).pack()
    Button(window,text="Register",command=register,font=("Arial",16)).pack()
    
    window.mainloop()

main_screen()
    