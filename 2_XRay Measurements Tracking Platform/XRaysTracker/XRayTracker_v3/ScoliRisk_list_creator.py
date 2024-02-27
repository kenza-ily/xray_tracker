############################################################################################################################################################
#Getting dates from the Excel Recovery file

#ScoliRisk_DateOp_df=pd.read_excel('file:///C:/Users/lafagev/.spyder-py3/XRay project/XRay Measure - copy.xlsx',sheet_name='Surgical',columns=['Patient ID','Date'])
#ScoliRisk_Date1stE_df=pd.read_excel('file:///C:/Users/lafagev/.spyder-py3/XRay project/XRay Measure - copy.xlsx',sheet_name='Non-Op',columns=['Patient ID','Date'])
#Dates_Recover=pd.merge(ScoliRisk_DateOp_df,ScoliRisk_Date1stE_df,how='outer',on='Patient ID')


#Initialization of lists
ScoliRisk_sites_list=[];ScoliRisk_study_Op=[];ScoliRisk_XRperpat=[];ScoliRisk_XRondrive=[];
patients_files=[];ScoliRisk_sitename=[];ScoliRisk_sites_list=[];

ScoliRisk_path=('M:\\AOScoliRisk\\10 - Database')
#ScoliRisk_path=('Dossier test')
ScoliRisk_sites_list_all=listDir(ScoliRisk_path)

for i in range(len(ScoliRisk_sites_list_all)):
    if (len(ScoliRisk_sites_list_all[i])<=3):
        ScoliRisk_sites_list.append(ScoliRisk_sites_list_all[i].upper())

#############################################################################################################################################################                
for i in range(len(ScoliRisk_sites_list)):
    if ('.' in ScoliRisk_sites_list[i])==False:
        
        ScoliRisk_patfolder_path=ScoliRisk_sitepath=ScoliRisk_path+'\\'+ScoliRisk_sites_list[i]+'\\'
        ScoliRisk_patfolder=listDir(ScoliRisk_patfolder_path)
        
        if ScoliRisk_patfolder!=[]:           
            for j in range(len(ScoliRisk_patfolder)):
                if ('.' in ScoliRisk_patfolder[j])==False:
                    ScoliRisk_patfilepath=ScoliRisk_path+'\\'+ScoliRisk_sites_list[i]+'\\'+ScoliRisk_patfolder[j]+'\\'
                    ScoliRisk_patfile_list=listDir(ScoliRisk_patfilepath)
                    
                    ScoliRisk_befformat=[]
                    ScoliRisk_formatsex=[]
                    
                    for n in range(len(ScoliRisk_patfile_list)):
                        
                        if ScoliRisk_patfile_list[n].startswith(ScoliRisk_sites_list[i].upper()):   
                            ScoliRisk_befformat.append(ScoliRisk_patfile_list[n][:-4])
                            ScoliRisk_formatsex.append([ScoliRisk_patfile_list[n][:-4],ScoliRisk_patfile_list[n][-3:]])
                    
                    ScoliRisk_befformat=unique(ScoliRisk_befformat)
    
                    for m in range(len(ScoliRisk_befformat)):
                        patient_line=[ScoliRisk_befformat[m]]
                        for o in range(len(ScoliRisk_formatsex)):
                            if ScoliRisk_befformat[m]==ScoliRisk_formatsex[o][0]:
                                patient_line.append(ScoliRisk_formatsex[o][1])
                        
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
                        elif ('base' in patient_line[0]) or ('I-0'in patient_line[0]) or ('I-O' in patient_line[0]):
                            time_index='(I-00)'
                        elif ('6w'in patient_line[0]) or ('6W'in patient_line[0]) or ('I-01'in patient_line[0]) or ('I-1' in patient_line[0]):
                            time_index='(I-01)'
                        elif ('3m'in patient_line[0]) or ('3M'in patient_line[0]) or ('I-02' in patient_line[0]) or ('I-2' in patient_line[0]):
                            time_index='(I-02)'
                        elif ('6m'in patient_line[0]) or ('6M'in patient_line[0]) or ('I-03' in patient_line[0]) or ('I-3' in patient_line[0]):
                            time_index='(I-03)'
                        elif ('9m'in patient_line[0]) or ('9M'in patient_line[0]) or ('I-04' in patient_line[0]) or ('I-4' in patient_line[0]):
                            time_index='(I-04)'
                        elif ('1y'in patient_line[0]) or ('1Y'in patient_line[0]) or ('12m' in patient_line[0]) or ('12M' in patient_line[0]) or ('I-05' in patient_line[0]) or ('I-5' in patient_line[0]):
                            time_index='(I-05)'
                        elif ('18m'in patient_line[0]) or ('18M'in patient_line[0]) or ('I-06' in patient_line[0]) or ('I-6' in patient_line[0]):
                            time_index='(I-06)'
                        elif ('2y'in patient_line[0]) or ('2Y'in patient_line[0]) or ('I-07' in patient_line[0]) or ('I-7' in patient_line[0]):
                            time_index='(I-07)'
                        elif ('3y'in patient_line[0]) or ('3Y'in patient_line[0]) or ('I-08' in patient_line[0]) or ('I-8' in patient_line[0]):
                            time_index='(I-08)'
                        else:
                            time_index='to define'

                    
                        ScoliRisk_XRondrive.append(['ScoliRisk',ScoliRisk_sites_list[i].upper(),'OPERATIVE',patient_line[0].split(' ',2)[0],Status,patient_view,time_index,dcm,tif,num,xls,','.join(patient_line[0].split('.',1)[1].split('.',4)[0:3]),patient_line[0],ScoliRisk_patfilepath])
                        #patient_line[0].split(' ',2)[0]
                        
####################################################################################################################################
#Creating the data frame
global ScoliRisk_XRondrive_df
ScoliRisk_XRondrive_df=pd.DataFrame(ScoliRisk_XRondrive,columns=['Study','Site','OpNOp','Patient ID','Status','View','Time_index','dcm','tif','num','xls','Date','file name','Path'])
ScoliRisk_XRondrive_df=ScoliRisk_XRondrive_df.drop_duplicates()  #A SAVOIR

######### UPDATING THE DIRECTORY WITH LAST UPDATE
global ScoliRisk_csv_lu ; global ScoliRisk_csv
global ScoliRisk_db_df
ScoliRisk_csv_lu='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//ScoliRisk_ModifTable.csv'
ScoliRisk_csv='Y://10 - Projects//02-Database managment//XRay Measurements Tracking Platform//ScoliRisk.csv'

ScoliRisk_lastupdate=pd.read_csv(ScoliRisk_csv_lu,sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
if 'Unnamed: 0' in ScoliRisk_lastupdate.columns:
    del ScoliRisk_lastupdate['Unnamed: 0']

ScoliRisk_db_df=pd.merge(ScoliRisk_lastupdate,ScoliRisk_XRondrive_df,how='outer',on='file name')

ScoliRisk_db_df=ScoliRisk_db_df[['Study','Site','OpNOp','Patient ID','Valid','Valid_comment','Status','View','Time_index','dcm','tif','num','xls','Date','Comment','file name','Path']]

ScoliRisk_db_df.to_csv(ScoliRisk_csv)