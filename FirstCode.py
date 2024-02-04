

###############################################################################
#               This Code imports all the packages, creates all the functions needed all along the Database creating - updating
#########################################################################################
from numpy import *

from time import strftime
import os;import webbrowser
import datetime;
import pandas as pd;from pandastable import Table;
import subprocess;
import tkinter as tk;from tkinter import ttk;
import smtplib;
from datetime import date
today=date.today();now=datetime.now()
Actual_datetime=strftime('%B %d, %Y %I:%M:%S %p')
import datetime
#style.use('ggplt')
bg_color='#EEF9FF'
white_bg='#FFFFFF'



def unique(list1):  # This function eliminates the duplicates of a list
    # intilize a null list 
    unique_list = [] 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    return unique_list

def listDir(dir): #this function returns the files/folders inside a directory
    fileNames=os.listdir(dir)
    return fileNames  

##############################################################################################################################
#                                           DIRECTORY
##############################################################################################################################
#UPDATES DIRECTORY

#Refresh/Download directories functions for the 7 Studies
    
def Refresh_PON():
    ############################################################################################################################################################
    #Getting dates from the Excel Recovery file
#    PON_Dates_df=pd.read_excel(r'Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//PON - Excel Dates Recovery.xlsx',sheet_name='All',columns=['Patient ID','Date'])

    #Initialization of lists
    PON_study_Op=[];POn_XRondrive=[];
    
    PON_path= r'M:\\ISSG\\02 - Prospective Study - PON\\01 - Radiographic database\\01 - Database'
    PON_sites_list_all=listDir(PON_path)
    
    global PON_sites_list
    PON_sites_list=[];
    for i in range(len(PON_sites_list_all)):
        if (len(PON_sites_list_all[i])<=3):
            PON_sites_list.append(PON_sites_list_all[i].upper())
    
    #############################################################################################################################################################                
    for i in range(len(PON_sites_list)):
        if ('.' in PON_sites_list[i])==False: #Only takes sites pages
            PON_testempty_path=PON_sitepath=PON_path+'\\'+PON_sites_list[i]+'\\'
            PON_testempty=listDir(PON_testempty_path)
            
            if PON_testempty!=[]: #Only takes 'PON', non empty folders          
                for t in range(len(PON_testempty)):
                    if ('.' in PON_testempty[t])==False:
                        PON_sitepath=PON_path+'\\'+PON_sites_list[i]+'\\'+PON_testempty[t]+'\\'
                        PON_study_Op=listDir(PON_sitepath)
                        
                        for j in range(len(PON_study_Op)):
                            PON_patientpath=PON_path+'\\'+PON_sites_list[i]+'\\'+PON_testempty[t]+'\\'+PON_study_Op[j]
                            PON_patfolder=listDir(PON_patientpath)
                            
                            for k in range(len(PON_patfolder)):
                                if ('.' in PON_patfolder[k])==False:
                                    PON_patfilepath=PON_path+'\\'+PON_sites_list[i]+'\\'+PON_testempty[t]+'\\'+PON_study_Op[j]+'\\'+PON_patfolder[k]+'\\'
                                    PON_patfile_list=listDir(PON_patfilepath)
                                    
                                    PON_befformat=[]
                                    PON_formatsex=[]
                                    
                                    for n in range(len(PON_patfile_list)):
                                        
                                        if PON_patfile_list[n].startswith(PON_sites_list[i].upper()) or PON_patfile_list[n].startswith('KS-'):   
                                            PON_befformat.append(PON_patfile_list[n][:-4])
                                            PON_formatsex.append([PON_patfile_list[n][:-4],PON_patfile_list[n][-3:]])
                                    
                                    PON_befformat=unique(PON_befformat)
                    
                                    for m in range(len(PON_befformat)):
                                        patient_line=[PON_befformat[m]]
                                        for o in range(len(PON_formatsex)):
                                            if PON_befformat[m]==PON_formatsex[o][0]:
                                                patient_line.append(PON_formatsex[o][1])
                                        
                                        xls=False;dcm=False;tif=False;num=False
                                        if 'xls' in patient_line:
                                            xls=True
                                        if 'dcm' in patient_line:
                                            dcm=True     
                                        if 'tif' in patient_line:
                                            tif=True
                                        if 'num' in patient_line:
                                            num=True
                                        
                                        if tif==False:
                                            Status='Missing tif file'
                                        elif tif==True and num==False and xls==False:
                                            Status='Ready for measure'
                                        elif tif==True and num==True and xls==False:
                                            Status='Ready to verify'
                                        elif tif==True and num==True and xls==True:
                                            Status='Complete'
                                        
                                        if ('lat'  in patient_line[0]) or ('LAT' in patient_line[0]) or ('Lat' in patient_line[0]):
                                            patient_view='LAT'
                                        elif ('ap' in patient_line[0]) or ('AP' in patient_line[0]) or ('Ap' in patient_line[0]):
                                            patient_view='AP'
                                        else:
                                            patient_view=patient_line[0].split('.',1)[-1]
                                        if type(patient_view)==int:
                                            patient_view=''
                                        
                                        
                                        if '(I-' in patient_line[0]:
                                            time_index=patient_line[0][patient_line[0].index('(I-'):patient_line[0].index('(I-')+6]
                                        else:
                                            time_index='to define'
                                        
                                        POn_XRondrive.append(['PON',PON_sites_list[i].upper(),patient_line[0].split(' ',2)[0],Status,PON_study_Op[j],patient_view,time_index,dcm,tif,num,xls,patient_line[0],PON_patfilepath])
                            
    ####################################################################################################################################
    #Creating the data frame
    global PON_db_df
    POn_XRondrive_df=pd.DataFrame(POn_XRondrive,columns=['Study','Site','Patient ID','Status','OpNOp','View','Time_index','dcm','tif','num','xls','file name','Path'])
    POn_XRondrive_df=POn_XRondrive_df.drop_duplicates()  #A SAVOIR
    #PON_XROndrive_wd=pd.merge(POn_XRondrive_df,PON_Dates_df,how='outer',on='Patient ID') #On Drive with dates
    
    ############## MERGING DIRECTORY DB WITH LAST UPDATE
    global PON_csv_lu ; global PON_csv
#    PON_csv_lu= r'Y:\\10 - Projects\\02-Database managment\\XRay Measurements Tracking Platform\\PON_ModifTable.csv'
#    PON_csv= r'Y:\\10 - Projects\\02-Database managment\\XRay Measurements Tracking Platform\\PON.csv'
    PON_csv_lu='Y:/10 - Projects/02-Database managment/XRay Measurements Tracking Platform/PON_ModifTable.csv'
    PON_csv='Y:/10 - Projects/02-Database managment/XRay Measurements Tracking Platform/PON.csv'
    
    PON_lastupdate=pd.read_csv(PON_csv_lu,sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
    PON_db_df=pd.merge(PON_lastupdate.dropna(subset=['file name']),POn_XRondrive_df,how='right',on='file name')
    PON_db_df=PON_db_df[['Study','Site','OpNOp','Patient ID','Valid','Valid_comment','Status','View','Time_index','dcm','tif','num','xls','Comment','OR Date / Visit Date','file name','Path']]
    #Saving into csv
    PON_db_df.to_csv(PON_csv)
    

###################################################################################################################################################################
#########################################################################################################################################################
#                                            XRAYS MEASUREMENTS TRACKING PLATFORM
#########################################################################################################################################################
###################################################################################################################################################################

#List for the studies --> makes it more manageable 
################################################################################################################################################################
TITLE_FONT = ("Arial", 25, "bold")
bg_color='#EEF9FF'
white_bg='#FFFFFF'
global username1
username1=''
username_folder= r'Y:\10 - Projects\02-Database managment\XRay Measurements Tracking Platform\usernames'

def open_hsswebsite():
    webbrowser.open_new("www.hss.edu")
    
#####################################################################################################################
#                       APP CREATING
###############################################################################################################################################################
############################################################# 1 - Creating the App 
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #Template : PON_Database_Page,PON_Sites_Page, Raw_PON_Database,PON_ToMeasure_Page,PON_ToVerif_Page,PON_Complete_Page,PON_Missingtif_Page,PON_Complete_Page
        Pages_List=[StartPage, Session_Page, Patients_Page,NewPatient_Page,PON_Database_Page,PON_Sites_Page, Raw_PON_Database,PON_ToMeasure_Page,PON_ToVerif_Page,PON_Complete_Page,PON_Missingtif_Page,Studies_Page,PCD_Database_Page,Raw_PCD_Database,PCD_ToMeasure_Page,PCD_ToVerif_Page,PCD_Complete_Page,PCD_Missingtif_Page,PCD_Sites_Page,PEED_Database_Page,PEED_Sites_Page, Raw_PEED_Database,PEED_ToMeasure_Page,PEED_ToVerif_Page,PEED_Complete_Page,PEED_Missingtif_Page,ScoliRisk_Database_Page,ScoliRisk_Sites_Page, Raw_ScoliRisk_Database,ScoliRisk_ToMeasure_Page,ScoliRisk_ToVerif_Page,ScoliRisk_Complete_Page,ScoliRisk_Missingtif_Page,NiH_Database_Page,NiH_Sites_Page, Raw_NiH_Database,NiH_ToMeasure_Page,NiH_ToVerif_Page,NiH_Complete_Page,NiH_Missingtif_Page,NiH_Complete_Page,CTJ_Database_Page,CTJ_Sites_Page, Raw_CTJ_Database,CTJ_ToMeasure_Page,CTJ_ToVerif_Page,CTJ_Complete_Page,CTJ_Missingtif_Page,CTJ_Complete_Page,MESA_Database_Page,MESA_Sites_Page, Raw_MESA_Database,MESA_ToMeasure_Page,MESA_ToVerif_Page,MESA_Complete_Page,MESA_Missingtif_Page,MESA_Complete_Page,MESA_NotValidPage]
#        Register_Page,PageOne
        self.frames = {}
        for F in Pages_List: #dont forget to add the different pages
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        
        frame = self.frames[c]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg=bg_color)
        StartPage_frame=tk.Frame(self,bg=bg_color)
        label = tk.Label(StartPage_frame, text="X-Rays Measurements Tracking Platform", font=("Arial", 30, "bold"),bg=bg_color) #foreground = "Red"
        label.pack(side="top")
        sublabel = tk.Label(StartPage_frame,bg=bg_color, text="Welcome to the 2019 Software enabling you to track X-Rays measurements",font=("Arial", 15))
        sublabel.pack()
        button1 = tk.Button(StartPage_frame, text="Enter",font=('Arial',14,'bold'),bg=white_bg,command=lambda: controller.show_frame(Session_Page))
        HSS_Button = tk.Button(StartPage_frame, text = "HSS Website",command=open_hsswebsite)
        StartPage_frame.pack(expand=True)

        button1.pack(side="top",expand=True,fill='x',pady=10)
        HSS_Button.pack(side="bottom")
        

#        

###################################################################################################################################################################      
#                                   SESSION AND DATA
###################################################################################################################################################################
#############################################################
class Session_Page(tk.Frame): 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
                 
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack()
#        tk.Label(self, text="Welcome to you session "+username1+" !",bg=bg_color,font=('Arial',11,'italic')).pack(fill='x',side='top')
        tk.Label(self, text="Home",bg=bg_color, font=TITLE_FONT).pack(side="top", fill="x", pady=10)
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side="top", fill="x", pady=10)
        
        
        Numbers_session=tk.Frame(self,bg=bg_color)
        Studies_num=tk.Frame(Numbers_session,bg=white_bg)

        
        tk.Label(Numbers_session, text="   ",bg=bg_color,font=('Arial',14,'bold')).pack(side='left')
        

        
        tk.Label(Numbers_session, text="\n \n",bg=bg_color,font=('Arial',25,)).pack();Numbers_session.pack()
        
        tk.Button(self, text = "Studies",font=('Arial',16),bg=white_bg,command=lambda: controller.show_frame(Studies_Page)).pack(pady=10,padx=10)
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(pady=10)
        tk.Button(self, text = "Patients",bg=white_bg,font=('Arial',16), command=lambda: controller.show_frame(Patients_Page)).pack(pady=10,padx=10)
        label = tk.Label(self, text="",bg=bg_color,font=('Arial',11)) 
        label.pack(side="top", fill="x", pady=10)
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")


############################################################################################################################################################        

#                                   STUDIES 

############################################################################################################################################################ 
############################################################ 


#######################################################################   1 -  PON_Database
class PON_Database_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        df=Studies_list_df[0]
        
        PON_Database_frame=tk.Frame(self,bg=bg_color)
        PON_Database_frame_bottom=tk.Frame(self,bg=bg_color)
        tk.Label(self, text="Home > Studies > PON ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(PON_Database_frame,text='PON DataBase Page',bg=bg_color,font=TITLE_FONT).pack()
        tk.Label(PON_Database_frame,text='\n',bg=bg_color,font=TITLE_FONT).pack()
        
        AllXRays_frame=tk.Frame(PON_Database_frame,bg=white_bg)
        tk.Label(AllXRays_frame, text="Total number of XRays",bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
        tk.Label(AllXRays_frame, text=df['Patient ID'].describe()[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
        AllXRays_frame.pack()
        
        tk.Label(PON_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PON_Database_frame)
        
        Numbers_frame=tk.Frame(PON_Database_frame,bg=bg_color)

        PON_Database_frame.pack(expand=True,side='top');PON_Database_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="All Studies",bg=white_bg,command=lambda: controller.show_frame(Studies_Page)).pack(side="bottom")
        


class Raw_PON_Database(tk.Frame): #Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PON > Whole Database ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PON - Whole Database",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        
        df=Studies_list_df[0]
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        
        def Refresh_callback():
            Refresh_PON()
            Actual_datetime=strftime('%B %d, %Y %I:%M:%S %p')
            pt.importCSV(PON_csv)
            print('refreshed')
        
        def Save_callback():
#            pt['file name','Valid','Valid_comment','Comment','OR Date / Visit Date'].doExport(PON_csv_lu)
            pt.doExport('ephemere.csv') #Exports the whole database to the csv file
            pt.importCSV('ephemere.csv')
            saver=pd.read_csv('ephemere.csv')
            saver[['file name','Valid','Valid_comment','Comment','OR Date / Visit Date']].dropna(subset=['file name']).to_csv(PON_csv_lu)
            print('saved')
            
        self.table = pt = Table(f,dataframe=df) 
        pt.show()      
       
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="PON Database",bg=white_bg,command=lambda: controller.show_frame(PON_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="Refresh",font=('Arial',10),bg=white_bg,command=lambda:Refresh_callback()).pack(side="bottom")
        tk.Button(self, text="Save changes to the Table",font=('Arial',10),bg=white_bg,command=lambda:Save_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        
        return
    
class PON_Missingtif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        tk.Label(self, text="Home > Studies > PON > Missing tif ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PON - Missing tif Database",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        
        df=Studies_list_df[0]
        dataframe=df.loc[df['Status']=='Missing tif file']
        
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="PON Database",bg=white_bg,command=lambda: controller.show_frame(PON_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        
        return
    
class PON_ToMeasure_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PON > To Measure ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PON - XRays To Measure ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
#        dataframe_creator_ff()
#
        df=Studies_list_df[0]
        dataframe=Studies_list_df[0].loc[Studies_list_df[0]['Status']=='Ready for measure']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) # , showstatusbar=True
        pt.show()
        
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="PON Database",bg=white_bg,command=lambda: controller.show_frame(PON_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color) 
        if dataframe.shape[0]!=0:
            path_to_open="explorer "+df['Path'][dataframe.index[0]]
            def Verify_callback():
                pt.redraw()
                global j
                j=0
                path_to_open="explorer "+df['Path'][dataframe.index[0]]
                subprocess.Popen(path_to_open,shell=True)
    
            def Next_callback():
                pt.redraw()
                global next_path_to_open
                global j
                if j==0:
                    p=subprocess.Popen(path_to_open,shell=True)
                else:
                    p=subprocess.Popen(next_path_to_open,shell=True)
                p.kill()
                j+=1
                if j<=df['Path'].describe()[0]:
                    next_path_to_open="explorer "+df['Path'][dataframe.index[j]]
                    p=subprocess.Popen(next_path_to_open)
                    p
    
                else:
                    tk.Label(self, text="All files are measured",bg=bg_color,font=('Arial',11)).pack()
            tk.Button(Image_treating, text="Measure",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
            tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
            tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
            Image_treating.pack(side='bottom')
        
        return
    
class PON_ToVerif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PON > To Verify ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PON - XRays To Verify ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        
        df=Studies_list_df[0]
        dataframe=df.loc[df['Status']=='Ready to verify']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) # , showstatusbar=True
        pt.show()
        
        

        
        tk.Label(self, text="",bg=bg_color,font=('Arial',13)).pack(side='bottom')
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="PON Database",bg=white_bg,command=lambda: controller.show_frame(PON_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')

        if dataframe.shape[0]!=0:
            path_to_open="explorer "+df['Path'][dataframe.index[0]]
            def Verify_callback():
                pt.redraw()
                global j
                j=0
                path_to_open="explorer "+df['Path'][dataframe.index[0]]
                subprocess.Popen(path_to_open,shell=True)
    
            def Next_callback():
                pt.redraw()
                global next_path_to_open
                global j
                if j==0:
                    p=subprocess.Popen(path_to_open,shell=True)
                else:
                    p=subprocess.Popen(next_path_to_open,shell=True)
                p.kill()
                j+=1
                if j<=df['Path'].describe()[0]:
                    next_path_to_open="explorer "+df['Path'][dataframe.index[j]]
                    p=subprocess.Popen(next_path_to_open)
                    p
    
                else:
                    tk.Label(self, text="All files are measured",bg=bg_color,font=('Arial',11)).pack()
                
         
            Image_treating=tk.Frame(self,bg=bg_color)        
            tk.Button(Image_treating, text="Verify",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
            tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
            tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
            Image_treating.pack(side='bottom')
            
        return

    

class PON_Complete_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PON > Completed ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PON - Completed XRays Measurment Tracking ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        
        df=Studies_list_df[0]
        dataframe=Studies_list_df[0].loc[Studies_list_df[0]['Status']=='Complete']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) # , showstatusbar=True
        pt.show()
        
        def Save_callback():
            pt.redraw()
            df[['file name','Valid','Valid_comment','Comment']].to_csv('PON_ModifTable.csv')
            print('saved')
#        

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="PON Database",bg=white_bg,command=lambda: controller.show_frame(PON_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
    
        
        return
    



###############################################################################################################
#
        #                                  SITES PER STUDY
#
#       
############################################################  1 - PON
class PON_Sites_Page(tk.Frame): #Should, from each Site, show only  the XRays corresponding to this Site. Plots sheet is an option too.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        tk.Label(self, text="Choose the site you want the data from :",bg=bg_color, font=TITLE_FONT).pack(side="top", fill="x", pady=10)

        Sites_frame=tk.Frame(self,bg=bg_color)
        Sites_frame_bottom=tk.Frame(self,bg=bg_color)
        for i in range(len(PON_sites_list)):
            if len(PON_sites_list[i])<=3:
                label = tk.Label(Sites_frame, text="",bg=bg_color,font=('Arial',11))
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn=tk.Button(Sites_frame, text=PON_sites_list[i].upper(),bg=white_bg,font=('Arial',14))
#                Site_Bttn.grid(row=r,column=c)
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn.pack(in_=Sites_frame,side='left')
        
        Sites_frame.pack(expand=True,side='top')
        Sites_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
       
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PON Database Page ",bg=white_bg,command=lambda: controller.show_frame(PON_Database_Page)).pack(side="bottom")
        
 
########################################################################################################################################################## 
##############################################################################################################################################################
##############################################################################################################################################################
##############################################################################################################################################################
if __name__ == "__main__":
    app = SampleApp()
#    app.config(background=bg_color) #We can change the background color
    app.title("X-Rays Measurements Tracking Platform")
    app.geometry("1000x600")
    app.minsize(1500,800)
    app.maxsize(2000,1000)
    app.iconbitmap(r"Y:\10 - Projects\02-Database managment\XRay Measurements Tracking Platform\HSS-monogram-logo_1400.ico")
    app.mainloop()
