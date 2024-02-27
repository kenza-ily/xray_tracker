############################################################################################################################################################
#Getting dates from the Excel Recovery file

#PEED_DateOp_df=pd.read_excel('file:///C:/Users/lafagev/.spyder-py3/XRay project/XRay Measure - copy.xlsx',sheet_name='Surgical',columns=['Patient ID','Date'])
#PEED_Date1stE_df=pd.read_excel('file:///C:/Users/lafagev/.spyder-py3/XRay project/XRay Measure - copy.xlsx',sheet_name='Non-Op',columns=['Patient ID','Date'])
#Dates_Recover=pd.merge(PEED_DateOp_df,PEED_Date1stE_df,how='outer',on='Patient ID')


#Initialization of lists
PEED_sites_list=[];PEED_study_Op=[];PEED_XRperpat=[];PEED_XRondrive=[];patients_files=[];PEED_sitename=[];PEED_sites_list=[];


PEED_path=('N:\\AO - PEEDS\\05 - Database')
PEED_sites_list_all=listDir(PEED_path)

for i in range(len(PEED_sites_list_all)):
    if (len(PEED_sites_list_all[i])<=3):
        PEED_sites_list.append(PEED_sites_list_all[i].upper())

#############################################################################################################################################################                
for i in range(len(PEED_sites_list)):
    
    if ('.' in PEED_sites_list[i])==False:
        PEED_patfolder_path=PEED_sitepath=PEED_path+'\\'+PEED_sites_list[i]+'\\'
        PEED_patfolder=listDir(PEED_patfolder_path)
        
        if PEED_patfolder!=[]:           
                for j in range(len(PEED_patfolder)):
                    if ('.' in PEED_patfolder[j])==False:
                        PEED_patfilepath=PEED_path+'\\'+PEED_sites_list[i]+'\\'+PEED_patfolder[j]+'\\'
                        PEED_patfile_list=listDir(PEED_patfilepath)
                        
                        PEED_befformat=[]
                        PEED_formatsex=[]
                        
                        for n in range(len(PEED_patfile_list)):
                            
                            if PEED_patfile_list[n].startswith(PEED_sites_list[i].upper()):   
                                PEED_befformat.append(PEED_patfile_list[n][:-4])
                                PEED_formatsex.append([PEED_patfile_list[n][:-4],PEED_patfile_list[n][-3:]])
                        
                        PEED_befformat=unique(PEED_befformat)
        
                        for m in range(len(PEED_befformat)):
                            patient_line=[PEED_befformat[m]]
                            for o in range(len(PEED_formatsex)):
                                if PEED_befformat[m]==PEED_formatsex[o][0]:
                                    patient_line.append(PEED_formatsex[o][1])
                            
                            xls=False;dcm=False;tif=False;num=False
                            if 'xls' in patient_line:
                                xls=True
                            if 'dcm' in patient_line:
                                dcm=True
                            if 'tif' in patient_line:
                                tif=True
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
                                patient_view=patient_line[0].split('.',4)[-1]
                            if type(patient_view)==int:
                                patient_view=''
                            
                            
                            if '(I-' in patient_line[0]:
                                time_index=patient_line[0][patient_line[0].index('(I-'):patient_line[0].index('(I-')+6]
                            else:
                                time_index='to define'

                            OpNOp='OPERATIVE'
                        
                            PEED_XRondrive.append(['PEED',PEED_sites_list[i].upper(),OpNOp,patient_line[0].split(' ',2)[0],Status,patient_view,time_index,dcm,tif,num,xls,','.join(patient_line[0].split('.',1)[1].split('.',4)[0:3]),patient_line[0],PEED_patfilepath])
                            #patient_line[0].split(' ',2)[0]
#####################################################################################################################################################################
#Creating the data frame
global PEED_XRondrive_df
PEED_XRondrive_df=pd.DataFrame(PEED_XRondrive,columns=['Study','Site','OpNOp','Patient ID','Status','View','Time_index','dcm','tif','num','xls','Date','file name','Path'])
PEED_XRondrive_df=PEED_XRondrive_df.drop_duplicates()  #A SAVOIR


######### UPDATING THE DIRECTORY WITH LAST UPDATE
global PEED_csv_lu ; global PEED_csv
global PEED_db_df
PEED_csv_lu='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//PEED_ModifTable.csv'
PEED_csv='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//PEED.csv'

PEED_lastupdate=pd.read_csv(PEED_csv_lu,sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

PEED_db_df=pd.merge(PEED_lastupdate,PEED_XRondrive_df,how='outer',on='file name')

PEED_db_df=PEED_db_df[['Study','Site','OpNOp','Patient ID','Valid','Valid_comment','Status','View','Time_index','dcm','tif','num','xls','Date','Comment','file name','Path']]

PEED_db_df.to_csv(PEED_csv)