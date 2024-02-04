from tkinter import *
import os
import webbrowser
from tkinter.ttk import Combobox
from pathlib import Path
import pandas as pd
import datetime
from pandastable import Table,TableModel
#import pandas.io.data as plt
from matplotlib import style
#style.use('ggplt')
bg_color='#EEF9FF'
white_bg='#FFFFFF'

import tkinter as tk
from tkinter import ttk
import smtplib


############################################################################################################################################################
#Getting dates from the Excel Recovery file

#CTJ_DateOp_df=pd.read_excel('file:///C:/Users/lafagev/.spyder-py3/XRay project/XRay Measure - copy.xlsx',sheet_name='Surgical',columns=['Patient ID','Date'])
#CTJ_Date1stE_df=pd.read_excel('file:///C:/Users/lafagev/.spyder-py3/XRay project/XRay Measure - copy.xlsx',sheet_name='Non-Op',columns=['Patient ID','Date'])
#Dates_Recover=pd.merge(CTJ_DateOp_df,CTJ_Date1stE_df,how='outer',on='Patient ID')


#Initialization of lists
CTJ_sites_list=[];CTJ_study_Op=[];CTJ_XRperpat=[];
CTJ_XRondrive=[];patients_files=[];CTJ_sitename=[];CTJ_sites_list=[];

CTJ_path=('M:\\CTJ\\01 - Database\\Clean')

#CTJ_path=('Dossier test')
CTJ_patfolder=listDir(CTJ_path)
for j in range(len(CTJ_patfolder)):
    if ('.' in CTJ_patfolder[j])==False:
        CTJ_patfilepath=CTJ_path+'\\'+CTJ_patfolder[j]+'\\'
        CTJ_patfile_list=listDir(CTJ_patfilepath)
        
        CTJ_befformat=[]; CTJ_formatsex=[]
        
        for n in range(len(CTJ_patfile_list)):
            if CTJ_patfile_list[n].startswith('NYU'.upper()):   
                CTJ_befformat.append(CTJ_patfile_list[n][:-4])
                CTJ_formatsex.append([CTJ_patfile_list[n][:-4],CTJ_patfile_list[n][-3:]])
        
        CTJ_befformat=unique(CTJ_befformat)

        for m in range(len(CTJ_befformat)):
            patient_line=[CTJ_befformat[m]]
            for o in range(len(CTJ_formatsex)):
                if CTJ_befformat[m]==CTJ_formatsex[o][0]:
                    patient_line.append(CTJ_formatsex[o][1])
                    
            xls=False;dcm=False;tif=False;num=False
            if 'xls' in patient_line:
                xls=True;
            if 'dcm' in patient_line:
                dcm=True
            if 'tif' in patient_line:
                tif=True;
            if 'num' in patient_line:
                num=True;
            
            if tif==False:
                Status='Missing tif file'
            elif tif==True and num==False and xls==False:
                Status='Ready for measure'
            elif tif==True and num==True and xls==False:
                Status='Ready to verify'
            elif tif==True and num==True and xls==True:
                Status='Complete'

            patient_view=patient_line[0].split('.',1)[-1]

            if '(I-' in patient_line[0]:
                time_index=patient_line[0][patient_line[0].index('(I-'):patient_line[0].index('(I-')+6]
            else:
                time_index='to define'
                
            CTJ_XRondrive.append(['CTJ','NYU','OPERATIVE',patient_line[0].split(' ',2)[0],Status,patient_view,time_index,dcm,tif,num,xls,patient_line[0],CTJ_patfilepath])
            #patient_line[0].split(' ',2)[0]
###################################################################################################################################  

#Creating the data frame
global CTJ_XRondrive_df
CTJ_XRondrive_df=pd.DataFrame(CTJ_XRondrive,columns=['Study','Site','OpNOp','Patient ID','Status','View','Time_index','dcm','tif','num','xls','file name','Path'])
CTJ_XRondrive_df=CTJ_XRondrive_df.drop_duplicates()  #A SAVOIR

######### UPDATING THE DIRECTORY WITH LAST UPDATE
global CTJ_csv_lu ; global CTJ_csv
global CTJ_db_df
CTJ_csv_lu='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//CTJ_ModifTable.csv'
CTJ_csv='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//CTJ.csv'

CTJ_lastupdate=pd.read_csv(CTJ_csv_lu,sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
if 'Unnamed: 0' in CTJ_lastupdate.columns:
    del CTJ_lastupdate['Unnamed: 0']
CTJ_lastupdate=CTJ_lastupdate.drop_duplicates()

CTJ_db_df=pd.merge(CTJ_lastupdate,CTJ_XRondrive_df,how='outer',on='file name')
CTJ_db_df=CTJ_db_df[['Study','Site','OpNOp','Patient ID','Valid','Valid_comment','Status','View','Time_index','dcm','tif','num','xls','Date','Comment','file name','Path']]



CTJ_db_df.to_csv(CTJ_csv)