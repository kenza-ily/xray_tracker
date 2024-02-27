#Python program enabling the Xrays centralizing platform

from tkinter import *
import webbrowser

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

