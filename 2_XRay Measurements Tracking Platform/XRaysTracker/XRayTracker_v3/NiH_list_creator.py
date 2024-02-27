############################################################################################################################################################
#Getting dates from the Excel Recovery file

#NiH_DateOp_df=pd.read_excel('file:///C:/Users/lafagev/.spyder-py3/XRay project/XRay Measure - copy.xlsx',sheet_name='Surgical',columns=['Patient ID','Date'])
#NiH_Date1stE_df=pd.read_excel('file:///C:/Users/lafagev/.spyder-py3/XRay project/XRay Measure - copy.xlsx',sheet_name='Non-Op',columns=['Patient ID','Date'])
#Dates_Recover=pd.merge(NiH_DateOp_df,NiH_Date1stE_df,how='outer',on='Patient ID')


#Initialization of lists
NiH_sites_list=[];NiH_study_Op=[];NiH_XRperpat=[];NiH_XRondrive=[];patients_files=[];
NiH_sitename=[];NiH_sites_list=[];



NiH_path=('M:\\NiH\\10-database Spineview')
#NiH_path=('Dossier test')
NiH_sites_list_all=listDir(NiH_path)

for i in range(len(NiH_sites_list_all)):
    if (len(NiH_sites_list_all[i])<=3):
        NiH_sites_list.append(NiH_sites_list_all[i].upper())

#############################################################################################################################################################                
for i in range(len(NiH_sites_list)):
    if ('.' in NiH_sites_list[i])==False:
        NiH_patfolder_path=NiH_sitepath=NiH_path+'\\'+NiH_sites_list[i]+'\\'
        NiH_patfolder=listDir(NiH_patfolder_path)
        
        if NiH_patfolder!=[]:           
                        for j in range(len(NiH_patfolder)):
                            if ('.' in NiH_patfolder[j])==False:
                                NiH_patfilepath=NiH_path+'\\'+NiH_sites_list[i]+'\\'+NiH_patfolder[j]+'\\'
                                NiH_patfile_list=listDir(NiH_patfilepath)
                                
                                NiH_befformat=[]
                                NiH_formatsex=[]
                                
                                for n in range(len(NiH_patfile_list)):
                                    
                                    if NiH_patfile_list[n].startswith(NiH_sites_list[i].upper()):   
                                        NiH_befformat.append(NiH_patfile_list[n][:-4])
                                        NiH_formatsex.append([NiH_patfile_list[n][:-4],NiH_patfile_list[n][-3:]])
                                
                                NiH_befformat=unique(NiH_befformat)
                
                                for m in range(len(NiH_befformat)):
                                    patient_line=[NiH_befformat[m]]
                                    for o in range(len(NiH_formatsex)):
                                        if NiH_befformat[m]==NiH_formatsex[o][0]:
                                            patient_line.append(NiH_formatsex[o][1])
                                    
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
                                        Valid='yes'
                                    
                                    if ('lat'  in patient_line[0]) or ('LAT' in patient_line[0]) or ('Lat' in patient_line[0]):
                                        patient_view='LAT'
                                    elif ('ap' in patient_line[0]) or ('AP' in patient_line[0]) or ('Ap' in patient_line[0]):
                                        patient_view='AP'
                                    else:
                                        patient_view=patient_line[0].split(' ',4)[4]
                                    
                                    
                                    if '(I-' in patient_line[0]:
                                        time_index=patient_line[0][patient_line[0].index('(I-'):patient_line[0].index('(I-')+6]
                                    else:
                                        time_index='to define'
                                        

                                    
                                    OpNOp='OPERATIVE'
                                
                                    NiH_XRondrive.append(['NiH',NiH_sites_list[i].upper(),OpNOp,patient_line[0].split(' ',2)[0],Status,patient_view,time_index,dcm,tif,num,xls,patient_line[0].split(' ',4)[3],patient_line[0],NiH_patfilepath])
                                    #patient_line[0].split(' ',2)[0]
                        
#################################################################################################################################
#Creating the data frame
global NiH_XRondrive_df
NiH_XRondrive_df=pd.DataFrame(NiH_XRondrive,columns=['Study','Site','OpNOp','Patient ID','Status','View','Time_index','dcm','tif','num','xls','Date','file name','Path'])
NiH_XRondrive_df=NiH_XRondrive_df.drop_duplicates()  #A SAVOIR


######### UPDATING THE DIRECTORY WITH LAST UPDATE
global NiH_csv_lu ; global NiH_csv
global NiH_db_df
NiH_csv_lu='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//NiH_ModifTable.csv'
NiH_csv='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//NiH.csv'

NiH_lastupdate=pd.read_csv(NiH_csv_lu,sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
if 'Unnamed: 0' in NiH_lastupdate.columns:
    del NiH_lastupdate['Unnamed: 0']


NiH_db_df=pd.merge(NiH_lastupdate,NiH_XRondrive_df,how='outer',on='file name')

NiH_db_df=NiH_db_df[['Study','Site','OpNOp','Patient ID','Valid','Valid_comment','Status','View','Time_index','dcm','tif','num','xls','Date','Comment','file name','Path']]

NiH_db_df.to_csv(NiH_csv)

