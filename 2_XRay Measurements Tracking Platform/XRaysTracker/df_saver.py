###############################################################################
#               This Code imports all the packages, creates all the functions needed all along the Database creating - updating
#########################################################################################
from time import gmtime,strftime
import numpy as np
import os;import webbrowser
from pathlib import Path;
import datetime;
import pandas as pd;from pandastable import Table,TableModel;
from matplotlib import style;
import subprocess;
import tkinter as tk;from tkinter import ttk;from tkinter.ttk import Combobox;
import smtplib;
import atexit ;
bg_color='#EEF9FF';white_bg='#FFFFFF';
from datetime import date
from datetime import datetime
from openpyxl import Workbook, load_workbook
today=date.today();now=datetime.now()
Actual_datetime=strftime('%B %d, %Y %I:%M:%S %p')

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
      import PON_list_creator
def Refresh_CTJ():
    import CTJ_list_creator
def Refresh_NiH():
     import NiH_list_creator

def Refresh_MESA():
    import MESA_list_creator

def Refresh_PEED():
    import PEED_list_creator
def Refresh_ScoliRisk():
     import ScoliRisk_list_creator
def Refresh_PCD():
     import PCD_list_creator

#Executes the last seven functions to create the seven databases associated to the seven studies
Refresh_PON();Refresh_CTJ();Refresh_NiH();Refresh_MESA();Refresh_PCD();Refresh_PEED();Refresh_ScoliRisk()

#Returns the list of all Sites within all studies
Sites_list=unique(PON_sites_list+PEED_sites_list+ScoliRisk_sites_list+CTJ_sites_list+NiH_sites_list+MESA_sites_list+PCD_sites_list)



### WE DONT NEED THIS
##Saves all the databases of the available XRays into an Excel file with multiple Sheets
#with pd.ExcelWriter("XRays - Available.xlsx") as writer:
#        for i in range(len(Studies_list)):
#            Studies_list_df[i].to_excel(writer,sheet_name=Studies_list[i])  

