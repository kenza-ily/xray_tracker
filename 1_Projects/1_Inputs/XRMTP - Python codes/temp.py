#Python program enabling the Xrays centralizing platform

from tkinter import *

#Create a first window
window=Tk()

#Personnalisation
window.title("XR centralizing platform")
window.geometry("500x500")
window.minsize(480,360)
window.maxsize(800,800)
window.iconbitmap("C:\Users\lafagev\Desktop\HSS images\HSS-monogram-logo_1400.png")

#Ajouter du texte
label_title =Label (window,text="Welcome to the 2019 version")
label_title.pack()

#Affichage
window.mainloop()

