#########################################################################
#       Python file to display databases - needed to construct the Database
#####################################################################

from tkinter import *
import tkinter as tk
from pandastable import Table, TableModel



class TestApp(Frame):
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Table app')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        self.table = pt = Table(f,dataframe=MESA_db_df,showtoolbar=True,showstatusbar=True)
        pt.show()
        tk.Button(self, text="Save",font=('Arial',20),bg=white_bg,command=pt.close()).pack(side="bottom")
        return
        
app = TestApp()
#launch the app
app.mainloop()