# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:59:10 2019

@author: lafagev
"""

"""
Application: Youtube Player with choice to show desired number of results.
Creator: Bibek Bhandari
Date: 2018/02/17
Licence: Open Source 
"""

from tkinter import *

import tkinter.messagebox
import webbrowser
# building the window

class Application:
    def __init__(self, master):
        self.master = master

        # menubar
        menubar = Menu(master)
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        master.config(menu=menubar)
        # heading
        self.heading = Label(master, text="Youtube Player", font=("verdana 25 bold"), bg='#FF0000', fg='white')
        self.heading.place(x=330, y=0)
        
        def open_hsswebsite():
            webbrowser.open_new("www.hss.edu")

        #Create a first window
        window=Tk()
    
        #Creer la frame
        frame=Frame(window,bg='#EEF9FF')
            
        #Personnalisation
        window.title("X-Rays Measurements Tracking Platform")
        #Couleur
        window.config(background='#EEF9FF') #We can change the background color
        #Taille
        window.geometry("1000x600")
        window.minsize(480,360)
        window.maxsize(2000,1000)
        window.iconbitmap("HSS-monogram-logo_1400.ico")
                              
                              
        #width=300
        height=300
        #hss_logo=PhotoImage(file="HSS-monogram-logo_1400.png").zoom(35).subsample(32)
        #canvas=Canvas(frame,width=width, height=height,bg='#EEF9FF')
        #canvas.create_image(width/2,height/2,image=hss_logo)
        #canvas.pack(expand=YES)
        #canvas.grid(row=0,column=0)
                              
                              
                              
            
        #Titre
        label_title =Label (frame,text="X-Rays Measurements Tracking Platform", font=("Arial", 25),bg='#EEF9FF',fg='#454545') #Choisi le titrem sa taille, police et couleur
        #label_title.grid(row=0,column=1,sticky=W)
        label_title.pack()
                                  
        #Buttons
        Studies_bttn=Button(frame,text="Studies", font=("Arial",20),bg='#454545',fg='white')
        #Studies_bttn.grid(row=0,column=1,sticky=W)
        Studies_bttn.pack(pady=25,fill=X)
                                                        
        Patients_bttn=Button(frame,text="Patients", font=("Arial",20),bg='#454545',fg='white')
        #Patients_bttn.grid(row=0,column=1,sticky=W)
        Patients_bttn.pack(pady=25,fill=X)
                                                                             
        Images_bttn=Button(frame,text="Images", font=("Arial",20),bg='#454545',fg='white')
         #Images_bttn.grid(row=0,column=1,sticky=W)
        Images_bttn.pack(pady=25,fill=X)

        HSSWebsite_bttn=Button(frame,text="HSS Website", font=("Arial",20),bg='#454545',fg='white',command=open_hsswebsite)
        #HSSWebsite_bttn.grid(row=0,column=1,sticky=W)
        HSSWebsite_bttn.pack(pady=25,fill=X)

        Quit_bttn=Button(frame,text="Quit", font=("Arial",10),bg='#E7E7E7',fg='#FE4E4E',command=window.destroy)
        Quit_bttn.pack(pady=25)
                 
        frame.pack(expand=YES)

        #Menu bar creation
        menu_bar=Menu(window)
        file_menu=Menu(menu_bar,tearoff=0)
        edit_menu=Menu(menu_bar,tearoff=0)
        edit_menu.add_command(label="New Patient",font=("Arial",8))
        file_menu.add_command(label="New",font=("Arial",8)) #command=
        file_menu.add_command(label="Quit",font=("Arial",8),command=window.quit)
        menu_bar.add_cascade(label="File",font=("Arial",10),menu=file_menu)
        menu_bar.add_cascade(label="Edit",font=("Arial",10),menu=edit_menu)

        #window configuration to add the menu
        window.config(menu=menu_bar)


        #Affichage
        window.mainloop()

        # labels and entries for the window
        # ask
        self.video_title = Label(master, text="Enter Video Name: ", font=("arial 10"), bg='#FF0000', fg='white')
        self.video_title.place(x=0, y=38)

        # entries
        self.name = StringVar()
        self.ent = Entry(master, width=25, textvariable=self.name)
        self.ent.place(x=150, y=40)

        # ask2
        self.resn = Label(master, text="No. of desired results", font=("arial 10"), bg='#FF0000', fg='white')
        self.resn.place(x=0, y=80)

        # ent2
        result = StringVar()
        self.w = Entry(master, width=8, textvariable=result)
        self.w.place(x=150, y=80)

        # BUTTONS AND INSTRUCTIONS
        self.btn = Button(master, text="Search Videos", command=self.find)
        self.btn.place(x=10, y=110)

        self.ins = Label(master, text="1. Search May take some time depending on your internet speed.", font=('arial 10'), bg='#FF0000',fg='white')
        self.ins.place(x=0, y=170)

        self.ins2 = Label(master, text="2. More number of desired results, More time it takes.", font=('arial 10'), bg='#FF0000',fg='white')
        self.ins2.place(x=0, y=200)

        self.ins2 = Label(master, text="3. High Number of results might lead to 'NOT RESPONDING', which is ok.", font=('arial 10'), bg='#FF0000',fg='white')
        self.ins2.place(x=0, y=230)

        # search results box and label
        self.r = Label(master, text="Search Results", font=("arial 10 bold"), bg='#FF0000', fg='white')
        self.r.place(x=400, y=40)

        # List Box
        self.listbox = Listbox(master, width=50)
        self.listbox.place(x=400, y=60)

        self.label = Label(master, text="",bg='#FF0000')
        self.label.place(x=250, y=110)
    def youtube(self, *args, **kwargs):
        selected = self.listbox.curselection()
        webbrowser.open(final_url[selected[0]])

    def clear_results(self):
        self.listbox.delete(0, END)
        del(final_name[:])
        del(final_url[:])
    def find(self, *args, **kwargs):

        if (self.listbox.size()) == 0:
            if int(self.w.get()) <= 10:
                # loading screen
                self.label.config(text = "Searching Youtube", fg='white', bg='#FF0000')
                self.label.update_idletasks()
                # crawling ht esite
                crawl(self.ent.get(), int(self.w.get()))
                self.label.config(text = "Completed", fg='white', bg='#FF0000')

                # buttons
                self.op = Button(self.master, text="Open Video", command=self.youtube)
                self.op.place(x=720, y=60)
                    
                self.op2 = Button(self.master, text="Clear Results", command=self.clear_results)
                self.op2.place(x=720, y=100)

                for item in range(len(final_name)):
                    self.listbox.insert(END, final_name[item])
            else:
                tkinter.messagebox.showinfo("Limit Exceeded", "You can get results only upto 10")


        else:
            tkinter.messagebox.showinfo("Warning", "Please clear the previous results.")

root = Tk()
obj = Application(root)
root.title("Youtube Player")
root.geometry("900x270")
root.resizable(False, False)
root.configure(background='#FF0000')
root.mainloop()