############################################################################################################################################################
#Getting dates from the Excel Recovery file

#PCD_DateOp_df=pd.read_excel('file:///C:/Users/lafagev/.spyder-py3/XRay project/XRay Measure - copy.xlsx',sheet_name='Surgical',columns=['Patient ID','Date'])
#PCD_Date1stE_df=pd.read_excel('file:///C:/Users/lafagev/.spyder-py3/XRay project/XRay Measure - copy.xlsx',sheet_name='Non-Op',columns=['Patient ID','Date'])
#Dates_Recover=pd.merge(PCD_DateOp_df,PCD_Date1stE_df,how='outer',on='Patient ID')


#Initialization of lists
PCD_sites_list=[];PCD_study_Op=[];PCD_XRperpat=[];PCD_XRondrive=[];
patients_files=[];PCD_sitename=[];PCD_sites_list=[];


PCD_path=('M:\\ISSG\\02 - Prospective Study 2012 - Cervical\\05_Database - Landmark v2')
#PCD_path=('Dossier test')
PCD_sites_list_all=listDir(PCD_path)

for i in range(len(PCD_sites_list_all)):
    if (len(PCD_sites_list_all[i])<=3):
        PCD_sites_list.append(PCD_sites_list_all[i].upper())


#############################################################################################################################################################                
for i in range(len(PCD_sites_list)):
    
    if ('.' in PCD_sites_list[i])==False:
        PCD_patfolder_path=PCD_sitepath=PCD_path+'\\'+PCD_sites_list[i]+'\\'
        PCD_patfolder=listDir(PCD_patfolder_path)
        
        if PCD_patfolder!=[]:           
                        for j in range(len(PCD_patfolder)):
                            if ('.' in PCD_patfolder[j])==False:
                                PCD_patfilepath=PCD_path+'\\'+PCD_sites_list[i]+'\\'+PCD_patfolder[j]+'\\'
                                PCD_patfile_list=listDir(PCD_patfilepath)
                                
                                PCD_befformat=[]; PCD_formatsex=[]
                                
                                for n in range(len(PCD_patfile_list)):
                                    
                                    if PCD_patfile_list[n].startswith(PCD_sites_list[i].upper()):   
                                        PCD_befformat.append(PCD_patfile_list[n][:-4])
                                        PCD_formatsex.append([PCD_patfile_list[n][:-4],PCD_patfile_list[n][-3:]])
                                
                                PCD_befformat=unique(PCD_befformat)
                
                                for m in range(len(PCD_befformat)):
                                    patient_line=[PCD_befformat[m]]
                                    for o in range(len(PCD_formatsex)):
                                        if PCD_befformat[m]==PCD_formatsex[o][0]:
                                            patient_line.append(PCD_formatsex[o][1])
                                            
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
                                        
#
                                    
                                
                                    PCD_XRondrive.append(['PCD',PCD_sites_list[i].upper(),'OPERATIVE',patient_line[0].split(' ',2)[0],Status,patient_view,time_index,dcm,tif,num,xls,patient_line[0],PCD_patfilepath])
                                    #patient_line[0].split(' ',2)[0]
###################################################################################################################################  

#Creating the data frame
global PCD_XRondrive_df
PCD_XRondrive_df=pd.DataFrame(PCD_XRondrive,columns=['Study','Site','OpNOp','Patient ID','Status','View','Time_index','dcm','tif','num','xls','file name','Path'])
PCD_XRondrive_df=PCD_XRondrive_df.drop_duplicates()  #A SAVOIR


######### UPDATING THE DIRECTORY WITH LAST UPDATE
global PCD_csv_lu ; global PCD_csv
global PCD_db_df
PCD_csv_lu='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//PCD_ModifTable.csv'
PCD_csv='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//PCD.csv'

PCD_lastupdate=pd.read_csv(PCD_csv_lu,sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
if 'Unnamed: 0' in PCD_lastupdate.columns:
    del PCD_lastupdate['Unnamed: 0']


PCD_db_df=pd.merge(PCD_lastupdate,PCD_XRondrive_df,how='outer',on='file name')

PCD_db_df=PCD_db_df[['Study','Site','OpNOp','Patient ID','Valid','Valid_comment','Status','View','Time_index','dcm','tif','num','xls','Date','Comment','file name','Path']]

PCD_db_df.to_csv(PCD_csv)