############################################################################################################################################################
#Getting dates from the Excel Recovery file

#Last_update=pd.read_excel("XRays - Updated Database.xlsx",sheet_name=Studies_list[i],columns=['Patient ID','Date'])
#Last_updated=pd.concat([Last_update,Studies_list_df[i].loc[k,:]],axis=0)
#            

#Initialization of lists
MESA_sites_list=[];MESA_study_Op=[];MESA_XRperpat=[];MESA_XRondrive=[];
patients_files=[];MESA_sitename=[];MESA_sites_list=[];


MESA_path=('N:\\K2M - MESA Pro\\01- Database\\ARCHIVE')
#MESA_path=('Dossier test')
MESA_sites_list_all=listDir(MESA_path)

for i in range(len(MESA_sites_list_all)):
    if (MESA_sites_list_all[i][2]=='-'):
        MESA_sites_list.append(MESA_sites_list_all[i].upper())

#############################################################################################################################################################                
# SCREENING THE MESA DATABASE

for i in range(len(MESA_sites_list)): #Screening the list of Sites folder
    if ('.' in MESA_sites_list[i])==False:
        MESA_patfolder_path=MESA_sitepath=MESA_path+'\\'+MESA_sites_list[i]+'\\'
        MESA_patfolder=listDir(MESA_patfolder_path)
        
        if MESA_patfolder!=[]:           
            for j in range(len(MESA_patfolder)):#Screening the list of Patients per Sites folder
                if ('.' in MESA_patfolder[j])==False:
                    MESA_patfilepath=MESA_path+'\\'+MESA_sites_list[i]+'\\'+MESA_patfolder[j]+'\\'
                    MESA_patfile_list=listDir(MESA_patfilepath)
                    
                    MESA_befformat=[]
                    MESA_formatsex=[]
                    
                    for n in range(len(MESA_patfile_list)): #Screening the list of files per Patients
                        
                        if MESA_patfile_list[n].startswith(MESA_patfolder[j]):   
                            MESA_befformat.append(MESA_patfile_list[n][:-4])
                            MESA_formatsex.append([MESA_patfile_list[n][:-4],MESA_patfile_list[n][-3:]])
                    
                    MESA_befformat=unique(MESA_befformat)
    
                    for m in range(len(MESA_befformat)): #Screening each XRay per patient, and the files available per XRay
                            patient_line=[MESA_befformat[m]]
                            for o in range(len(MESA_formatsex)):
                                if MESA_befformat[m]==MESA_formatsex[o][0]:
                                    patient_line.append(MESA_formatsex[o][1])
                            
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
                                patient_view=patient_line[0].split('.',4)[-1]
                            if type(patient_view)==int:
                                patient_view=''
                            
                            if '(I-' in patient_line[0]:
                                time_index=patient_line[0][patient_line[0].index('(I-'):patient_line[0].index('(I-')+6]
                            else:
                                time_index='to define'
                                
                            OpNOp='OPERATIVE'
                            
                            MESA_XRondrive.append(['MESA',MESA_sites_list[i].upper(),OpNOp,patient_line[0].split(' ',2)[0],Status,patient_view,time_index,dcm,tif,num,xls,','.join(patient_line[0].split('.',1)[1].split('.',4)[0:3]),patient_line[0],MESA_patfilepath])

#Creating the data frame
global MESA_XRondrive_df
MESA_XRondrive_df=pd.DataFrame(MESA_XRondrive,columns=['Study','Site','OpNOp','Patient ID','Status','View','Time_index','dcm','tif','num','xls','Date','file name','Path'])
MESA_XRondrive_df=MESA_XRondrive_df.drop_duplicates() #Deletes all 

##################### MERGING DIRECTORY WITH LAST DATABASE
global MESA_csv_lu
global MESA_csv
MESA_csv_lu='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//MESA_ModifTable.csv'
MESA_csv='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//MESA.csv'

global MESA_db_df
MESA_lastupdate=pd.read_csv(MESA_csv_lu,sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
if 'Unnamed: 0' in MESA_lastupdate.columns:
    del MESA_lastupdate['Unnamed: 0']

MESA_db_df=pd.merge(MESA_lastupdate,MESA_XRondrive_df,how='outer',on='file name')

MESA_db_df=MESA_db_df[['Study','Site','OpNOp','Patient ID','Valid','Valid_comment','Status','View','Time_index','dcm','tif','num','xls','Date','Comment','file name','Path']]

MESA_db_df.to_csv(MESA_csv)

