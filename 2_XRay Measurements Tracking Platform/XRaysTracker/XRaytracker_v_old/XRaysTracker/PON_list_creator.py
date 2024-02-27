import numpy as np
############################################################################################################################################################
#Getting dates from the Excel Recovery file
PON_Dates_df=pd.read_excel('file:///Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//PON - Excel Dates Recovery.xlsx',sheet_name='All',columns=['Patient ID','Date'])


#Initialization of lists
PON_sites_list=[];PON_study_Op=[];PON_XRperpat=[];POn_XRondrive=[];Patients_files=[];PON_sitename=[];PON_sites_list=[];

PON_path=('M:\\ISSG\\02 - Prospective Study - PON\\01 - Radiographic database\\01 - Database')
PON_sites_list_all=listDir(PON_path)

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
                                        Valid='yes'
                                    
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
                                    
                                    path=PON_path+'\\'+PON_sites_list[i]+'\\'+PON_testempty[t]+'\\'+PON_study_Op[j]+'\\'+PON_patfolder[k]+'\\'

                                
                                    POn_XRondrive.append(['PON',PON_sites_list[i].upper(),patient_line[0].split(' ',2)[0],Status,PON_study_Op[j],patient_view,time_index,dcm,tif,num,xls,patient_line[0],PON_patfilepath])
                                    #patient_line[0].split(' ',2)[0]
                        
####################################################################################################################################
#Creating the data frame
global PON_db_df
POn_XRondrive_df=pd.DataFrame(POn_XRondrive,columns=['Study','Site','Patient ID','Status','OpNOp','View','Time_index','dcm','tif','num','xls','file name','Path'])
POn_XRondrive_df=POn_XRondrive_df.drop_duplicates()  #A SAVOIR
#PON_XROndrive_wd=pd.merge(POn_XRondrive_df,PON_Dates_df,how='outer',on='Patient ID') #On Drive with dates

############## MERGING DIRECTORY DB WITH LAST UPDATE
global PON_csv_lu ; global PON_csv
PON_csv_lu='Y:\\10 - Projects\\02-Database managment\\XRay Measurements Tracking Platform\\XRays - PON -  Updated Database.csv'
PON_csv='Y:\\10 - Projects\\02-Database managment\\XRay Measurements Tracking Platform\\PON.csv'


PON_lastupdate=pd.read_csv(PON_csv_lu,sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

PON_db_df=pd.merge(PON_lastupdate.dropna(subset=['file name']),POn_XRondrive_df,how='right',on='file name')




PON_db_df=PON_db_df[['Study','Site','OpNOp','Patient ID','Valid','Valid_comment','Status','View','Time_index','dcm','tif','num','xls','Comment','OR Date / Visit Date','file name','Path']]

#Saving into csv

PON_db_df.to_csv(PON_csv)










