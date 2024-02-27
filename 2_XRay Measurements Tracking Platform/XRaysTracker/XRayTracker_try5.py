###################################################################################################################################################################
#########################################################################################################################################################
#                                            XRAYS MEASUREMENTS TRACKING PLATFORM
#########################################################################################################################################################
###################################################################################################################################################################
import df_saver




from pandastable import Table #,TableModel
#from matplotlib import style
import subprocess
import os

#List for the studies --> makes it more manageable 
Studies_list_df=[PON_db_df,PEED_db_df,ScoliRisk_db_df,CTJ_db_df,NiH_db_df,MESA_db_df,PCD_db_df]
Studies_list=['PON','PEED','ScoliRisk','CTJ','NiH','MESA','PCD']
Poss_status=['Complete','Missing tif file','Ready for measure','Ready to verify']
################################################################################################################################################################
TITLE_FONT = ("Arial", 25, "bold")
bg_color='#EEF9FF'
white_bg='#FFFFFF'
username1=''
username_folder= 'Y:\\10 - Projects\\02-Database managment\\XRay Measurements Tracking Platform\\usernames'

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
        Pages_List=[StartPage, PageOne, Session_Page, Patients_Page, Register_Page,NewPatient_Page,PON_Database_Page,PON_Sites_Page, Raw_PON_Database,PON_ToMeasure_Page,PON_ToVerif_Page,PON_Complete_Page,PON_Missingtif_Page,Studies_Page,PCD_Database_Page,Raw_PCD_Database,PCD_ToMeasure_Page,PCD_ToVerif_Page,PCD_Complete_Page,PCD_Missingtif_Page,PCD_Sites_Page,PEED_Database_Page,PEED_Sites_Page, Raw_PEED_Database,PEED_ToMeasure_Page,PEED_ToVerif_Page,PEED_Complete_Page,PEED_Missingtif_Page,ScoliRisk_Database_Page,ScoliRisk_Sites_Page, Raw_ScoliRisk_Database,ScoliRisk_ToMeasure_Page,ScoliRisk_ToVerif_Page,ScoliRisk_Complete_Page,ScoliRisk_Missingtif_Page,NiH_Database_Page,NiH_Sites_Page, Raw_NiH_Database,NiH_ToMeasure_Page,NiH_ToVerif_Page,NiH_Complete_Page,NiH_Missingtif_Page,NiH_Complete_Page,CTJ_Database_Page,CTJ_Sites_Page, Raw_CTJ_Database,CTJ_ToMeasure_Page,CTJ_ToVerif_Page,CTJ_Complete_Page,CTJ_Missingtif_Page,CTJ_Complete_Page,MESA_Database_Page,MESA_Sites_Page, Raw_MESA_Database,MESA_ToMeasure_Page,MESA_ToVerif_Page,MESA_Complete_Page,MESA_Missingtif_Page,MESA_Complete_Page,MESA_NotValidPage]
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
        button1 = tk.Button(StartPage_frame, text="Login",font=('Arial',14,'bold'),bg=white_bg,command=lambda: controller.show_frame(PageOne))
        button2 = tk.Button(StartPage_frame,text="Register", font=('Arial',14,'bold'),bg=white_bg,command=lambda: controller.show_frame(Register_Page))
        HSS_Button = tk.Button(StartPage_frame, text = "HSS Website",command=open_hsswebsite)
        StartPage_frame.pack(expand=True)

        button1.pack(side="top",expand=True,fill='x',pady=10)
        button2.pack(expand=True,fill='x',pady=10)
        HSS_Button.pack(side="bottom")
        
############################################################# 2 - Login   
class PageOne(tk.Frame): #Login page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg=bg_color)
        self.controller=controller
        
        global PageOne_frame
        PageOne_frame=tk.Frame(self,bg=bg_color)
        
        label = tk.Label(PageOne_frame, text="Personal Informations", font=TITLE_FONT,bg=bg_color)
        label.pack(side="top", fill="x", pady=10)
        global optionv
        self.optionv = tk.StringVar()
        t1 = tk.Label(PageOne_frame, text="Account: ",font=('Arial',11,'bold'),bg=bg_color)
        self.v = tk.StringVar()
        self.v.set("")
        global entry1
        entry1 = tk.Entry(PageOne_frame, textvariable=self.v)
        t2 = tk.Label(PageOne_frame,text="\nPassword: ",font=('Arial',11,'bold'),bg=bg_color)
        self.pwd = tk.StringVar()
        self.pwd.set("")
        global entry2
        entry2 = tk.Entry(PageOne_frame, textvariable=self.pwd)
        entry2.config(show="*")
        
        t1.pack();entry1.pack();
        t2.pack();entry2.pack();
        tk.Label(PageOne_frame, text="",bg=bg_color,font=('Arial',11)) .pack();
        tk.Button(PageOne_frame, text="Log In", font=('Arial',11,'bold'),command=self.login,bg=white_bg) .pack();
        PageOne_frame.pack(expand=True);
        tk.Button(self, text="Go to the Welcome Page",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")

    def login(self):
        pwd_value = tk.Label(self, text="Invalid password", font=("Courier", 15, "bold"),bg=bg_color, foreground="red")
        usern_value = tk.Label(self, text="Invalid username ", font=("Courier", 15, "bold"),bg=bg_color, foreground="red")
        
        global username1
        username1 = self.v.get();password1 = self.pwd.get()
        entry1.delete(0,END); entry2.delete(0,END)
        
        file_to_verify=username_folder+'\\'+username1;list_of_files = os.listdir(username_folder)
        if username1 in list_of_files:
            file1 = open(file_to_verify, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.controller.show_frame(Session_Page)
            else:
                pwd_value.pack()
        else:
            usern_value.pack()
############################################################# 3 - Register          
class Register_Page(tk.Frame): #Register page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg=bg_color)
        self.controller=controller
        
        label = tk.Label(self, text="Register Page", font=TITLE_FONT,bg=bg_color)
        label.pack(side="top", fill="x", pady=10)
        sublabel = tk.Label(self,bg=bg_color, text="Please enter the wanted info for your account",
                            font=("Arial", 15))
        sublabel.pack()
        
        global r_optionv
        self.r_optionv = tk.StringVar()
        r_t1 = tk.Label(self, text="Account: ",font=('Arial',11,'bold'),bg=bg_color)
        self.v2 = tk.StringVar()
        self.v2.set("")
        global r_entry
        r_entry = tk.Entry(self, textvariable=self.v2)
        r_t2 = tk.Label(self,text="\nPassword: ",font=('Arial',11,'bold'),bg=bg_color)
        self.r_pwd = tk.StringVar()
        self.r_pwd.set("")
        global r_entry2
        r_entry2 = tk.Entry(self, textvariable=self.r_pwd)
        r_entry2.config(show="*")
        lgbutton=tk.Button(self, text="Register", font=('Arial',11,'bold'),command=self.register,bg=white_bg) 
       
        r_t1.pack()
        r_entry.pack()
        r_t2.pack()
        r_entry2.pack()
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)) .pack()
        lgbutton.pack()
        Logoff_button = tk.Button(self, text="Go to the Welcome Page",bg=white_bg,
                           command=lambda: controller.show_frame(StartPage))
        Logoff_button.pack(side="bottom")

    def register(self):
         usern_taken = tk.Label(self, text="Username already taken \n Registration unsuccesfull", font=("Courier", 15, "bold"),bg=bg_color, foreground="red")
         r_success_label = tk.Label(self, text="Register was Successful \n (Click ""Continue"" to access database)",bg=bg_color, font=("Courier", 15, "bold"), foreground="blue")
         cbutton = tk.Button(self, text="Continue",bg=white_bg, command=lambda: self.controller.show_frame(PageOne))
         
         global username_info #Nows which session it is 
         username_info = self.v2.get()
         password_info = self.r_pwd.get()
 
         list_of_files = os.listdir(username_folder) #A modifier quand on mettra les usernames sur le Drive
         if username_info in list_of_files:
            usern_taken.pack()
         else:    
            file_to_open=username_folder+'\\'+username_info
            file=open(file_to_open, "w")
            file.write(username_info+"\n")
            file.write(password_info)
            file.close()
      
            r_entry.delete(0, END)
            r_entry2.delete(0, END)

            r_success_label.pack()
            cbutton.pack()
        

###################################################################################################################################################################      
#                                   SESSION AND DATA
###################################################################################################################################################################
#############################################################
class Session_Page(tk.Frame): 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
                 
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack()
        tk.Label(self, text="Welcome to you session "+username1+" !",bg=bg_color,font=('Arial',11,'italic')).pack(fill='x',side='top')
        tk.Label(self, text="Home",bg=bg_color, font=TITLE_FONT).pack(side="top", fill="x", pady=10)
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side="top", fill="x", pady=10)
        
        
        Numbers_session=tk.Frame(self,bg=bg_color)

        Studies_num=tk.Frame(Numbers_session,bg=white_bg)
        tk.Label(Studies_num, text="Number of Studies",bg=white_bg,font=('Arial',14,'bold')).pack( fill="x", pady=10)
        tk.Label(Studies_num, text=len(Studies_list),bg=white_bg,font=('Arial',11)).pack( fill="x", pady=10)
        Studies_num.pack(side='left')
        
        tk.Label(Numbers_session, text="   ",bg=bg_color,font=('Arial',14,'bold')).pack(side='left')
        
        Sites_num=tk.Frame(Numbers_session,bg=white_bg)
        tk.Label(Sites_num, text="Number of Sites",bg=white_bg,font=('Arial',14,'bold')).pack( fill="x", pady=10)
        tk.Label(Sites_num, text=len(Sites_list),bg=white_bg,font=('Arial',11)).pack( fill="x", pady=10) #A MODIFIER 
        Sites_num.pack(side='left')
        
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
class Studies_Page(tk.Frame): #Should, from each Site, show only  the XRays corresponding to this Site. Plots sheet is an option too.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        label = tk.Label(self, text="Choose the Study you want the data from :",bg=bg_color, font=TITLE_FONT) 
        label.pack(side="top", fill="x", pady=10)

        Studies_frame=tk.Frame(self,bg=bg_color)
        Studies_frame_bottom=tk.Frame(self,bg=bg_color)

        ############ Studies Buttons 
        tk.Label(Studies_frame, text=" ",bg=bg_color,font=('Arial',11)).pack(in_=Studies_frame,side='left')
        tk.Button(Studies_frame, text='PON'.upper()+' Database',bg=white_bg,font=('Arial',13),command=lambda: controller.show_frame(PON_Database_Page)).pack(in_=Studies_frame)
        tk.Label(Studies_frame, text=" ",bg=bg_color,font=('Arial',11,)).pack()
        tk.Button(Studies_frame, text='PCD'.upper()+' Database',bg=white_bg,font=('Arial',13),command=lambda: controller.show_frame(PCD_Database_Page)).pack(in_=Studies_frame)
        tk.Label(Studies_frame, text=" ",bg=bg_color,font=('Arial',11,)).pack()
        tk.Button(Studies_frame, text='PEED'.upper()+' Database',bg=white_bg,font=('Arial',13),command=lambda: controller.show_frame(PEED_Database_Page)).pack(in_=Studies_frame)
        tk.Label(Studies_frame, text=" ",bg=bg_color,font=('Arial',11,)).pack()
        tk.Button(Studies_frame, text='ScoliRisk'.upper()+' Database',bg=white_bg,font=('Arial',13),command=lambda:controller.show_frame(ScoliRisk_Database_Page)).pack(in_=Studies_frame)
        tk.Label(Studies_frame, text=" ",bg=bg_color,font=('Arial',11,)).pack()
        tk.Button(Studies_frame, text='NiH'.upper()+' Database',bg=white_bg,font=('Arial',13),command=lambda: controller.show_frame(NiH_Database_Page)).pack(in_=Studies_frame)
        tk.Label(Studies_frame, text=" ",bg=bg_color,font=('Arial',11)).pack()
        tk.Button(Studies_frame, text='CTJ'.upper()+' Database',bg=white_bg,font=('Arial',13),command=lambda: controller.show_frame(CTJ_Database_Page)).pack(in_=Studies_frame)
        tk.Label(Studies_frame, text=" ",bg=bg_color,font=('Arial',11,)).pack()
        tk.Button(Studies_frame, text='MESA'.upper()+' Database',bg=white_bg,font=('Arial',13),command=lambda: controller.show_frame(MESA_Database_Page)).pack(in_=Studies_frame)

        Studies_frame.pack(expand=True,side='top')
        Studies_frame_bottom.pack(side='bottom',fill='both')
       
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        
################################################################################ 3 - Patients        
class Patients_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Patients ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        Patients_Frame=tk.Frame(self,background=bg_color)
        
        tk.Button(Patients_Frame, text="New Patient ",font=('Arial',15,'bold'),bg=white_bg,command=lambda: self.controller.show_frame(NewPatient_Page)).pack()
        tk.Label(Patients_Frame, text="",bg=bg_color,font=('Arial',11)) .pack()
        
        
        self.p = tk.StringVar()
        self.p.set("")
        global patient_entry
        patient_entry = tk.Entry(Patients_Frame, textvariable=self.p)
        
        validate_button=tk.Button(Patients_Frame, text="Validate", font=('Arial',11),command=self.patient_display,bg=white_bg) 
        button = tk.Button(Patients_Frame, text="Log off",bg=white_bg,
                           command=lambda: controller.show_frame(StartPage))
        tk.Label(Patients_Frame, text="Patient ID: ",font=('Arial',11,'bold'),bg=bg_color).pack()
        tk.Label(Patients_Frame, text="",bg=bg_color,font=('Arial',11)) .pack()
        patient_entry.pack()
        tk.Label(Patients_Frame, text="",bg=bg_color,font=('Arial',20)) .pack()
        validate_button.pack()
        Patients_Frame.pack(expand=True)
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        
    def patient_display(self):
         NoData_label = tk.Label(self, text="Patient not found \n Please enter Site+PON+N or Y+Number+ \n Example : mok", font=("Courier", 15, "bold"),bg=bg_color, foreground="red")
         r_success_label = tk.Label(self, text="Register was Successful \n (Click ""Continue"" to access database)",bg=bg_color, font=("Courier", 15, "bold"), foreground="blue")
         cbutton = tk.Button(self, text="Continue",bg=white_bg, command=lambda: self.controller.show_frame(PageOne))
         empty=tk.Label(self, text="",bg=bg_color,font=('Arial',11)) 
         
class NewPatient_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        tk.Label(self, text="New Patient",bg=bg_color,font=TITLE_FONT).pack()                    
        
        NP_Study_frame=tk.Frame(self,background=bg_color)
        global site
        self.site = tk.StringVar(); 
        data=PON_sites_list;
        tk.Label(NP_Study_frame, text="Study", font=("Arial", 12),bg=bg_color,fg='#000000').pack(in_=NP_Study_frame,side='left')
        tk.Label(NP_Study_frame, text="", font=("Arial", 12),bg=bg_color,fg='#000000').pack(in_=NP_Study_frame,side='left')
        cb=Combobox(NP_Study_frame, textvariable=self.site,values=data)
        cb.pack(in_=NP_Study_frame,side='left')
        tk.Label(NP_Study_frame, text="", font=("Arial", 15),bg=bg_color,fg='#000000').pack()
        NP_Study_frame.pack()
        
        NP_Gender_frame=tk.Frame(self,background=bg_color)
        global v0
        self.v0=tk.StringVar()
        gender_title =tk.Label (NP_Gender_frame,text="\n Gender", font=("Arial", 12),bg=bg_color,fg='#000000')
        gender_title.pack(in_=NP_Gender_frame,side='left')
        tk.Label(NP_Gender_frame, text="", font=("Arial", 12),bg=bg_color,fg='#000000').pack(in_=NP_Gender_frame,side='left')
        r1_gender=tk.Radiobutton(NP_Gender_frame, text="Male", textvariable=self.v0,value='M',font=("Arial", 12),bg=bg_color)
        r2_gender=tk.Radiobutton(NP_Gender_frame, text="Female", textvariable=self.v0,value='F',font=("Arial", 12),bg=bg_color)
        r1_gender.pack(); r2_gender.pack(in_=NP_Gender_frame,side='left')
        tk.Label(NP_Gender_frame, text="", font=("Arial", 15),bg=bg_color,fg='#000000').pack()
        NP_Gender_frame.pack()
        
        
        NP_OpNOp_frame=tk.Frame(self,background=bg_color)
        global v3
        self.v3=tk.StringVar()
        op_title =tk.Label (NP_OpNOp_frame,text="\n Operative", font=("Arial", 12),bg=bg_color,fg='#000000')
        op_title.pack(side='left')
        tk.Label(NP_OpNOp_frame, text="", font=("Arial", 12),bg=bg_color,fg='#000000').pack(in_=NP_OpNOp_frame,side='left')
        r1_op=tk.Radiobutton(NP_OpNOp_frame, text="Operative", textvariable=self.v3,value='Op',background=bg_color)
        r2_op=tk.Radiobutton(NP_OpNOp_frame, text="Non Operative", textvariable=self.v3,value='Non Op',background=bg_color)
        r1_op.pack(in_=NP_OpNOp_frame,side='left');  r2_op.pack(in_=NP_OpNOp_frame,side='left')
        tk.Label(NP_OpNOp_frame, text="", font=("Arial", 15),bg=bg_color,fg='#000000').pack()
        NP_OpNOp_frame.pack()
                       
        
        NP_PatNumber_frame=tk.Frame(self,background=bg_color)
        tk.Label(NP_PatNumber_frame,text="\n Patient ID", font=("Arial", 12),bg=bg_color,fg='#000000').pack(in_=NP_PatNumber_frame,side='left')
        tk.Label(NP_PatNumber_frame, text="", font=("Arial", 12),bg=bg_color,fg='#000000').pack(in_=NP_PatNumber_frame,side='left')
        global v4
        self.v4=tk.StringVar()
        patient_number=tk.Entry(NP_PatNumber_frame,bd=5,textvariable=self.v4)
        patient_number.pack(in_=NP_PatNumber_frame,side='left')
        tk.Label(NP_PatNumber_frame, text="", font=("Arial", 15),bg=bg_color,fg='#000000').pack()
        NP_PatNumber_frame.pack()
        
        
        NP_OpDate_frame=tk.Frame(self,background=bg_color)
#        NP_OpDate_frame.grid(row=3,column=0)
        tk.Label(NP_OpDate_frame,text="\n Date of Operation", font=("Arial", 12),bg=bg_color,fg='#000000').pack(in_=NP_OpDate_frame,side='left')
        tk.Label(NP_OpDate_frame, text = "",background=bg_color).pack(in_=NP_OpDate_frame,side='left')
        global DateOfOp_entry
        self.DateOfOp_entry=tk.StringVar()
        DateOfOp=tk.Entry(NP_OpDate_frame,bd=5,textvariable=self.DateOfOp_entry)
        DateOfOp.pack(in_=NP_OpDate_frame,side='left')
        tk.Label(NP_OpDate_frame, text = "",background=bg_color).pack()
        NP_OpDate_frame.pack()
        
        tk.Label(self, text = "",background=bg_color).pack()
        tk.Button(self, text = "Save", width = 10, height = 1,bg=white_bg,command=self.save_patient).pack(expand=True)
        
        
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',15)).pack(side='bottom')
        tk.Button(self, text="Return to Patients Page",bg=white_bg,command=lambda: controller.show_frame(Patients_Page)).pack(side="bottom")
        
    def save_patient(self):
        global site_l ; global gender_l ; global OpNOp_l ; global patient_num_l ; global Date_l ;
        site_l=self.site.get()
        gender_l=self.v0.get()
        OpNOp_l=self.v3.get()
        patient_num_l=self.v4.get()
        Date_l=self.DateOfOp_entry.get()
        global NP_list ; global NP_df
        NP_list=[site_l,gender_l , OpNOp_l, patient_num_l,Date_l]
        NP_df=pd.DataFrame(NP_list) #,columns=['Site','Op Or Non Op', 'Patient ID', 'Date of Op']
        tk.Label(self, text = "Patient Saved",bg=bg_color).pack()
        print('NP OK')
        
####################################################################################################################################
#                                 

#                                         STUDIES ONE BY ONE 
        
        
        
####################################################################################################################################  


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
        
        for i in range(len(Poss_status)):
            frame=tk.Frame(Numbers_frame,bg=white_bg)
            tk.Label(frame, text=Poss_status[i],bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x")
            tk.Label(frame, text=df[(df['Status']==Poss_status[i])&(df['Valid']!='no')].shape[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
            frame.pack(side='left')
            tk.Label(Numbers_frame,text='   ',bg=bg_color).pack(side='left')
        Numbers_frame.pack()
        
        tk.Label(PON_Database_frame,text='   ',bg=bg_color).pack(side='left');tk.Label(PON_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PON_Database_frame)
        tk.Button(PON_Database_frame, text='Whole PON Database',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(Raw_PON_Database)).pack()
        tk.Label(PON_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PON_Database_frame)

 #Complete
        tk.Label(PON_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PON_Database_frame,side='left')
        tk.Button(PON_Database_frame, text='Completed Track',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PON_Complete_Page)).pack(in_=PON_Database_frame,side='left')

        #Missing tif
        tk.Label(PON_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PON_Database_frame,side='left')
        tk.Button(PON_Database_frame, text='Missing tif file',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PON_Missingtif_Page)).pack(in_=PON_Database_frame,side='left')
        
        #Ready for Measure
        tk.Label(PON_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PON_Database_frame,side='left')
        tk.Button(PON_Database_frame, text='Ready for measure',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PON_ToMeasure_Page)).pack(in_=PON_Database_frame,side='left')
        
        #Ready for Check
        tk.Label(PON_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PON_Database_frame,side='left')
        tk.Button(PON_Database_frame, text='Ready to verify',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PON_ToVerif_Page)).pack(in_=PON_Database_frame,side='left')
        
       
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
        dataframe=Studies_list_df[0].loc[Studies_list_df[0]['Status']=='Missing tif file']
        
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()
#        

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="PON Database",bg=white_bg,command=lambda: controller.show_frame(PON_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=pt.redraw()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
#        tk.Button(self, text="Open folder",font=('Arial',15),bg=white_bg,command=pt.redraw()).pack()
#        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack()
        
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
#
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
                
         
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="PON Database",bg=white_bg,command=lambda: controller.show_frame(PON_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color) 
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
        
        
        path_to_open="explorer "+df['Path'][dataframe.index[0]]

        def Verify_callback():
            global j
            j=0
            path_to_open="explorer "+df['Path'][dataframe.index[0]]
            subprocess.Popen(path_to_open,shell=True)

        def Next_callback():
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
                tk.Label(self, text="All files are verified",bg=bg_color,font=('Arial',11)).pack()
        

        
        tk.Label(self, text="",bg=bg_color,font=('Arial',13)).pack(side='bottom')
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="PON Database",bg=white_bg,command=lambda: controller.show_frame(PON_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')

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
            df[['file name','Valid','Valid_comment','Comment']].to_csv('Y:\\10 - Projects\\02-Database managment\\XRay Measurements Tracking Platform\\XRays - PON -  Updated Database.csv')
            print('saved')
#        

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="PON Database",bg=white_bg,command=lambda: controller.show_frame(PON_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
#        tk.Button(self, text="Refresh",font=('Arial',15),bg=white_bg,command=lambda:Refresh_PON()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=lambda:Save_Callback()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        
        
        return
    

#####################################################################################################################################################################################
#                                                             PCD
######################################################################################################################################################################################
 
     
class PCD_Database_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        df=Studies_list_df[6]
        PCD_Database_frame=tk.Frame(self,bg=bg_color)
        PCD_Database_frame_bottom=tk.Frame(self,bg=bg_color)
        tk.Label(self, text="Home > Studies > PCD ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(PCD_Database_frame,text='PCD DataBase Page',bg=bg_color,font=TITLE_FONT).pack()
        
        tk.Label(PCD_Database_frame,text='\n',bg=bg_color,font=TITLE_FONT).pack()
        
        AllXRays_frame=tk.Frame(PCD_Database_frame,bg=white_bg)
        tk.Label(AllXRays_frame, text="Total number of XRays",bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
        tk.Label(AllXRays_frame, text=df['Patient ID'].describe()[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
        AllXRays_frame.pack()
        
        tk.Label(PCD_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PCD_Database_frame)
        
        
        Numbers_frame=tk.Frame(PCD_Database_frame,bg=bg_color)
        for i in range(len(Poss_status)):
            frame=tk.Frame(Numbers_frame,bg=white_bg)
            tk.Label(frame, text=Poss_status[i],bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
            tk.Label(frame, text=df[(df['Status']==Poss_status[i])&(df['Valid']!='no')].shape[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
            frame.pack(side='left')
            tk.Label(Numbers_frame,text='   ',bg=bg_color).pack(side='left')
        Numbers_frame.pack()
        
        tk.Label(PCD_Database_frame,text='   ',bg=bg_color).pack(side='left')
        
        tk.Label(PCD_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PCD_Database_frame)
        tk.Button(PCD_Database_frame, text='Whole PCD Database',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(Raw_PCD_Database)).pack()
        tk.Label(PCD_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PCD_Database_frame)
                    #Complete
        tk.Label(PCD_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PCD_Database_frame,side='left')
        tk.Button(PCD_Database_frame, text='Completed Track',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PCD_Complete_Page)).pack(in_=PCD_Database_frame,side='left')

        #Missing tif
        tk.Label(PCD_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PCD_Database_frame,side='left')
        tk.Button(PCD_Database_frame, text='Missing tif file',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PCD_Missingtif_Page)).pack(in_=PCD_Database_frame,side='left')
        
        #Ready for Measure
        tk.Label(PCD_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PCD_Database_frame,side='left')
        tk.Button(PCD_Database_frame, text='Ready for measure',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PCD_ToMeasure_Page)).pack(in_=PCD_Database_frame,side='left')
        
        #Ready for Check
        tk.Label(PCD_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PCD_Database_frame,side='left')
        tk.Button(PCD_Database_frame, text='Ready to verify',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PCD_ToVerif_Page)).pack(in_=PCD_Database_frame,side='left')
        


        PCD_Database_frame.pack(expand=True,side='top')
        PCD_Database_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="All Studies",bg=white_bg,command=lambda: controller.show_frame(Studies_Page)).pack(side="bottom")


class Raw_PCD_Database(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        dataframe=Studies_list_df[6]
        
        tk.Label(self, text="Home > Studies > PCD > Whole Database ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PCD - Whole Database",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()

        def Refresh_callback():
            Refresh_PCD()
            Actual_datetime=strftime('%B %d, %Y %I:%M:%S %p')
            pt.importCSV(PCD_csv)
            print('refreshed')
        
        def Save_callback():
            pt.doExport('ephemere.csv') #Exports the whole database to the csv file
            pt.importCSV('ephemere.csv')
            saver=pd.read_csv('ephemere.csv')
            saver[['file name','Valid','Valid_comment','Comment','Date']].dropna(subset=['file name']).to_csv(PCD_csv_lu)
            print('saved')
            
            
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="PCD Database",bg=white_bg,command=lambda: controller.show_frame(PCD_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom') 
        tk.Button(self, text="Refresh",font=('Arial',12),bg=white_bg,command=lambda:Refresh_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Save changes to the Table",font=('Arial',12),bg=white_bg,command=lambda:Save_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        
        return
    
class PCD_Missingtif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        df=Studies_list_df[6]
        dataframe=Studies_list_df[6].loc[Studies_list_df[6]['Status']=='Missing tif file']
        
        tk.Label(self, text="Home > Studies > PCD > Missing tif ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PCD - Missing tif Database",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) # , showstatusbar=True
        pt.show()
#        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PCD Database",bg=white_bg,command=lambda: controller.show_frame(PCD_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=self.Saving_df).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        

    
class PCD_ToMeasure_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PCD > To Measure ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PCD - XRays To Measure ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
#        dataframe_creator_ff()
#
        df=Studies_list_df[6]
        dataframe=Studies_list_df[6].loc[Studies_list_df[6]['Status']=='Ready for measure']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()
#        
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
                

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PCD Database",bg=white_bg,command=lambda: controller.show_frame(PCD_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Measure",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
        return

    
class PCD_ToVerif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PCD > To Verify ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PCD - XRays To Verify ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
 
        df=Studies_list_df[6]
        dataframe=Studies_list_df[6].loc[Studies_list_df[6]['Status']=='Ready to verify']
    
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()

        path_to_open="explorer "+df['Path'][dataframe.index[0]]

        def Verify_callback():
            global j
            j=0
            path_to_open="explorer "+df['Path'][dataframe.index[0]]
            subprocess.Popen(path_to_open,shell=True)

        def Next_callback():
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
                tk.Label(self, text="All files are verified",bg=bg_color,font=('Arial',11)).pack()
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PCD Database",bg=white_bg,command=lambda: controller.show_frame(PCD_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
                
        Image_treating=tk.Frame(self,bg=bg_color)
        tk.Button(Image_treating, text="Verify",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
#        
        return



class PCD_Complete_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PCD > Completed ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PCD - Completed XRays Measurment Tracking ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')

        df=Studies_list_df[6]
        dataframe=Studies_list_df[6].loc[Studies_list_df[6]['Status']=='Complete']

        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PCD Database",bg=white_bg,command=lambda: controller.show_frame(PCD_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=pt.redraw()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        
        return
    

#####################################################################################################################################################################################
#                                                             PEED
######################################################################################################################################################################################
 
class PEED_Database_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        df=Studies_list_df[1]
        PEED_Database_frame=tk.Frame(self,bg=bg_color)
        PEED_Database_frame_bottom=tk.Frame(self,bg=bg_color)
        tk.Label(self, text="Home > Studies > PEED ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(PEED_Database_frame,text='PEED DataBase Page',bg=bg_color,font=TITLE_FONT).pack()
        
        tk.Label(PEED_Database_frame,text='\n',bg=bg_color,font=TITLE_FONT).pack()
        
        
        AllXRays_frame=tk.Frame(PEED_Database_frame,bg=white_bg)
        tk.Label(AllXRays_frame, text="Total number of XRays",bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
        tk.Label(AllXRays_frame, text=df['Patient ID'].describe()[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
        AllXRays_frame.pack()
        
        tk.Label(PEED_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PEED_Database_frame)
        
        Numbers_frame=tk.Frame(PEED_Database_frame,bg=bg_color)
        for i in range(len(Poss_status)):
            frame=tk.Frame(Numbers_frame,bg=white_bg)
            tk.Label(frame, text=Poss_status[i],bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
            tk.Label(frame, text=df[(df['Status']==Poss_status[i])&(df['Valid']!='no')].shape[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
            frame.pack(side='left')
            tk.Label(Numbers_frame,text='   ',bg=bg_color).pack(side='left')
        Numbers_frame.pack()
        
        tk.Label(PEED_Database_frame,text='   ',bg=bg_color).pack(side='left')
        tk.Label(PEED_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PEED_Database_frame)
        
        tk.Button(PEED_Database_frame, text='Whole PEED Database',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(Raw_PEED_Database)).pack()
        tk.Label(PEED_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PEED_Database_frame)

        tk.Label(PEED_Database_frame,text='   ',bg=bg_color).pack(side='left')
        #Complete
        tk.Label(PEED_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PEED_Database_frame,side='left')
        tk.Button(PEED_Database_frame, text='Completed Track',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PEED_Complete_Page)).pack(in_=PEED_Database_frame,side='left')

        #Missing tif
        tk.Label(PEED_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PEED_Database_frame,side='left')
        tk.Button(PEED_Database_frame, text='Missing tif file',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PEED_Missingtif_Page)).pack(in_=PEED_Database_frame,side='left')
        
        #Ready for Measure
        tk.Label(PEED_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PEED_Database_frame,side='left')
        tk.Button(PEED_Database_frame, text='Ready for measure',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PEED_ToMeasure_Page)).pack(in_=PEED_Database_frame,side='left')
        
        #Ready for Check
        tk.Label(PEED_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=PEED_Database_frame,side='left')
        tk.Button(PEED_Database_frame, text='Ready to verify',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(PEED_ToVerif_Page)).pack(in_=PEED_Database_frame,side='left')
        

        PEED_Database_frame.pack(expand=True,side='top')
        PEED_Database_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="All Studies",bg=white_bg,command=lambda: controller.show_frame(Studies_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')

class Raw_PEED_Database(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PEED > Whole Database ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PEED - Whole Database",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        
        df=Studies_list_df[1]
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=df)
        pt.show()
        
        def Refresh_callback():
            Refresh_PEED()
            Actual_datetime=strftime('%B %d, %Y %H:%M:%S')
            pt.importCSV(PEED_csv)
            print('refreshed')
        
        def Save_callback():
            pt.doExport('ephemere.csv') #Exports the whole database to the csv file
            pt.importCSV('ephemere.csv')
            saver=pd.read_csv('ephemere.csv')
            saver[['file name','Valid','Valid_comment','Comment']].dropna(subset=['file name']).to_csv(PEED_csv_lu)
            print('saved')
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PEED Database",bg=white_bg,command=lambda: controller.show_frame(PEED_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Refresh",font=('Arial',12),bg=white_bg,command=lambda: Refresh_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Save changes to the Table",font=('Arial',12),bg=white_bg,command=lambda: Save_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        
        return

    
class PEED_Missingtif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PEED > Missing tif ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PEED - Missing tif Database",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        
        df=Studies_list_df[1]
        dataframe=Studies_list_df[1].loc[Studies_list_df[1]['Status']=='Missing tif file']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) # , showstatusbar=True
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PEED Database",bg=white_bg,command=lambda: controller.show_frame(PEED_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=pt.redraw()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        
        return

    
class PEED_ToMeasure_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PEED > To Measure ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PEED - XRays To Measure ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        
        df=Studies_list_df[1]
        dataframe=Studies_list_df[1].loc[Studies_list_df[1]['Status']=='Ready for measure']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()

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
                
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PEED Database",bg=white_bg,command=lambda: controller.show_frame(PEED_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Measure",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
#        
        return

class PEED_ToVerif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PEED > To Verify ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PEED - XRays To Verify ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
    
        df=Studies_list_df[1]
        dataframe=Studies_list_df[1].loc[Studies_list_df[1]['Status']=='Ready to verify']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()

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
                
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PEED Database",bg=white_bg,command=lambda: controller.show_frame(PEED_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=pt.redraw()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Verify",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
        return


class PEED_Complete_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > PEED > Completed ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="PEED - Completed XRays Measurment Tracking ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        
        df=Studies_list_df[1]
        dataframe=Studies_list_df[1].loc[Studies_list_df[1]['Status']=='Complete']
      
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PEED Database",bg=white_bg,command=lambda: controller.show_frame(PEED_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=pt.redraw()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        
        return

        
       

#####################################################################################################################################################################################
#                                                             ScoliRisk
######################################################################################################################################################################################
   
class ScoliRisk_Database_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        df=Studies_list_df[2]
        ScoliRisk_Database_frame=tk.Frame(self,bg=bg_color)
        ScoliRisk_Database_frame_bottom=tk.Frame(self,bg=bg_color)
        tk.Label(self, text="Home > Studies > ScoliRisk ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(ScoliRisk_Database_frame,text='ScoliRisk DataBase Page',bg=bg_color,font=TITLE_FONT).pack()
        tk.Label(ScoliRisk_Database_frame,text='\n',bg=bg_color,font=TITLE_FONT).pack()
        
        AllXRays_frame=tk.Frame(ScoliRisk_Database_frame,bg=white_bg)
        tk.Label(AllXRays_frame, text="Total number of XRays",bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
        tk.Label(AllXRays_frame, text=df['Patient ID'].describe()[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
        AllXRays_frame.pack()
        
        tk.Label(ScoliRisk_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=ScoliRisk_Database_frame)
        
        
        Numbers_frame=tk.Frame(ScoliRisk_Database_frame,bg=bg_color)
        for i in range(len(Poss_status)):
            frame=tk.Frame(Numbers_frame,bg=white_bg)
            tk.Label(frame, text=Poss_status[i],bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
            tk.Label(frame, text=df[(df['Status']==Poss_status[i])&(df['Valid']!='no')].shape[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
            frame.pack(side='left')
            tk.Label(Numbers_frame,text='   ',bg=bg_color).pack(side='left')
        Numbers_frame.pack()

        tk.Label(ScoliRisk_Database_frame,text='   ',bg=bg_color).pack(side='left')
        
        tk.Label(ScoliRisk_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=ScoliRisk_Database_frame)
        
        tk.Button(ScoliRisk_Database_frame, text='Whole ScoliRisk Database',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(Raw_ScoliRisk_Database)).pack()
        tk.Label(ScoliRisk_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=ScoliRisk_Database_frame)
        
        
        #Complete
        tk.Label(ScoliRisk_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=ScoliRisk_Database_frame,side='left')
        tk.Button(ScoliRisk_Database_frame, text='Completed Track',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(ScoliRisk_Complete_Page)).pack(in_=ScoliRisk_Database_frame,side='left')

        #Missing tif
        tk.Label(ScoliRisk_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=ScoliRisk_Database_frame,side='left')
        tk.Button(ScoliRisk_Database_frame, text='Missing tif file',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(ScoliRisk_Missingtif_Page)).pack(in_=ScoliRisk_Database_frame,side='left')
        
        #Ready for Measure
        tk.Label(ScoliRisk_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=ScoliRisk_Database_frame,side='left')
        tk.Button(ScoliRisk_Database_frame, text='Ready for measure',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(ScoliRisk_ToMeasure_Page)).pack(in_=ScoliRisk_Database_frame,side='left')
        
        #Ready for Check
        tk.Label(ScoliRisk_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=ScoliRisk_Database_frame,side='left')
        tk.Button(ScoliRisk_Database_frame, text='Ready to verify',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(ScoliRisk_ToVerif_Page)).pack(in_=ScoliRisk_Database_frame,side='left')
        

        ScoliRisk_Database_frame.pack(expand=True,side='top')
        ScoliRisk_Database_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="All Studies",bg=white_bg,command=lambda: controller.show_frame(Studies_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')

class Raw_ScoliRisk_Database(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > ScoliRisk > Whole Database ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="ScoliRisk - Whole Database",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[2]
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=df)  # , showstatusbar=True
        pt.show()
        
        def Refresh_callback():
            Refresh_ScoliRisk()
            Actual_datetime=strftime('%B %d, %Y %H:%M:%S')
            pt.importCSV(ScoliRisk_csv)
            print('refreshed')
        
        def Save_callback():
            pt.doExport('ephemere.csv') #Exports the whole database to the csv file
            pt.importCSV('ephemere.csv')
            saver=pd.read_csv('ephemere.csv')
            saver[['file name','Valid','Valid_comment','Comment']].dropna(subset=['file name']).to_csv(ScoliRisk_csv_lu)
            print('saved')
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="ScoliRisk Database",bg=white_bg,command=lambda: controller.show_frame(ScoliRisk_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Refresh",font=('Arial',14),bg=white_bg,command=lambda:Refresh_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=lambda:Save_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        
        return
    
class ScoliRisk_Missingtif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        tk.Label(self, text="Home > Studies > ScoliRisk > Missing tif ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="ScoliRisk - Missing tif Database",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[2]
        dataframe= Studies_list_df[2].loc[Studies_list_df[2]['Status']=='Missing tif file']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) # , showstatusbar=True
        pt.show()
#        

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="ScoliRisk Database",bg=white_bg,command=lambda: controller.show_frame(ScoliRisk_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',20),bg=white_bg,command=pt.redraw()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        
        return
    
class ScoliRisk_ToMeasure_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > ScoliRisk > To Measure ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="ScoliRisk - XRays To Measure ",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[2]
        dataframe=Studies_list_df[2].loc[Studies_list_df[2]['Status']=='Ready for measure']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()
        
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
                
                

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="ScoliRisk Database",bg=white_bg,command=lambda: controller.show_frame(ScoliRisk_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Measure",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
        
        return
    
class ScoliRisk_ToVerif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > ScoliRisk > To Verify ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="ScoliRisk - XRays To Verify ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        
        df=Studies_list_df[2]
        dataframe=Studies_list_df[2].loc[Studies_list_df[2]['Status']=='Ready to verify']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()
        
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
                
                
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="ScoliRisk Database",bg=white_bg,command=lambda: controller.show_frame(ScoliRisk_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Verify",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
        
        return

class ScoliRisk_Complete_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > ScoliRisk > Completed ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="ScoliRisk - Completed XRays Measurment Tracking ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        
        df=Studies_list_df[2]
        dataframe=Studies_list_df[2].loc[Studies_list_df[2]['Status']=='Complete']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) # , showstatusbar=True
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="ScoliRisk Database",bg=white_bg,command=lambda: controller.show_frame(ScoliRisk_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',20),bg=white_bg,command=pt.redraw()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        
        return
#####################################################################################################################################################################################
#                                                             NiH
######################################################################################################################################################################################
class NiH_Database_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
#        dataframe_creator_ff()
        
        def Refresh_callback():
            Refresh_NiH()
            Actual_datetime=strftime('%B %d, %Y %H:%M:%S')
            print('refreshed')
        
        df=Studies_list_df[4]
        NiH_Database_frame=tk.Frame(self,bg=bg_color)
        NiH_Database_frame_bottom=tk.Frame(self,bg=bg_color)
        tk.Label(self, text="Home > Studies > NiH ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(NiH_Database_frame,text='NiH DataBase Page',bg=bg_color,font=TITLE_FONT).pack()
        
        tk.Label(NiH_Database_frame,text='\n',bg=bg_color,font=TITLE_FONT).pack()
        
        AllXRays_frame=tk.Frame(NiH_Database_frame,bg=white_bg)
        tk.Label(AllXRays_frame, text="Total number of XRays",bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
        tk.Label(AllXRays_frame, text=df['Patient ID'].describe()[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
        AllXRays_frame.pack()
        
        tk.Label(NiH_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=NiH_Database_frame)
        
        Numbers_frame=tk.Frame(NiH_Database_frame,bg=bg_color)
        for i in range(len(Poss_status)):
            frame=tk.Frame(Numbers_frame,bg=white_bg)
            tk.Label(frame, text=Poss_status[i],bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
            tk.Label(frame, text=df[(df['Status']==Poss_status[i])&(df['Valid']!='no')].shape[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
            frame.pack(side='left')
            tk.Label(Numbers_frame,text='   ',bg=bg_color).pack(side='left')
        Numbers_frame.pack()
        
        tk.Label(NiH_Database_frame,text='   ',bg=bg_color).pack(side='left')
        tk.Label(NiH_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=NiH_Database_frame)
        tk.Button(NiH_Database_frame, text="Refresh",font=('Arial',11),bg=white_bg,command=lambda:Refresh_callback()).pack()
        tk.Label(NiH_Database_frame, text="",bg=bg_color,font=('Arial',10)).pack()
        tk.Button(NiH_Database_frame, text='Whole NiH Database',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(Raw_NiH_Database)).pack()
        tk.Label(NiH_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=NiH_Database_frame)
        
                #Complete
        tk.Label(NiH_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=NiH_Database_frame,side='left')
        tk.Button(NiH_Database_frame, text='Completed Track',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(NiH_Complete_Page)).pack(in_=NiH_Database_frame,side='left')

        #Missing tif
        tk.Label(NiH_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=NiH_Database_frame,side='left')
        tk.Button(NiH_Database_frame, text='Missing tif file',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(NiH_Missingtif_Page)).pack(in_=NiH_Database_frame,side='left')
        
        #Ready for Measure
        tk.Label(NiH_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=NiH_Database_frame,side='left')
        tk.Button(NiH_Database_frame, text='Ready for measure',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(NiH_ToMeasure_Page)).pack(in_=NiH_Database_frame,side='left')
        
        #Ready for Check
        tk.Label(NiH_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=NiH_Database_frame,side='left')
        tk.Button(NiH_Database_frame, text='Ready to verify',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(NiH_ToVerif_Page)).pack(in_=NiH_Database_frame,side='left')
        

        NiH_Database_frame.pack(expand=True,side='top')
        NiH_Database_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="All Studies",bg=white_bg,command=lambda: controller.show_frame(Studies_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')

class Raw_NiH_Database(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > NiH > Whole Database ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="NiH - Whole Database",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[4]
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=df) 
        pt.show()
        
        def Refresh_callback():
            Refresh_NiH()
            Actual_datetime=strftime('%B %d, %Y %H:%M:%S')
            pt.importCSV(NiH_csv)
            print('refreshed')
        
        def Save_callback():
            pt.doExport('ephemere.csv') #Exports the whole database to the csv file
            pt.importCSV('ephemere.csv')
            saver=pd.read_csv('ephemere.csv')
            saver[['file name','Valid','Valid_comment','Comment']].dropna(subset=['file name']).to_csv(NiH_csv_lu)
            print('saved')
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="NiH Database",bg=white_bg,command=lambda: controller.show_frame(NiH_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Refresh",font=('Arial',14),bg=white_bg,command=lambda:Refresh_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Save changes to the Table",font=('Arial',15,'bold'),bg=white_bg,command=lambda:Save_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        
        return
    
class NiH_Missingtif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > NiH > Missing tif ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="NiH - Missing tif Database",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[4]
        dataframe=Studies_list_df[4].loc[Studies_list_df[4]['Status']=='Missing tif file']
        
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) # , showstatusbar=True
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="NiH Database",bg=white_bg,command=lambda: controller.show_frame(NiH_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',20),bg=white_bg,command=pt.redraw()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        
        return
    
class NiH_ToMeasure_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > NiH > To Measure ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="NiH - XRays To Measure ",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')

        df=Studies_list_df[4]
        dataframe=Studies_list_df[4].loc[Studies_list_df[4]['Status']=='Ready for measure']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) # , showstatusbar=True
        pt.show()
        
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

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="NiH Database",bg=white_bg,command=lambda: controller.show_frame(NiH_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Measure",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
        
        return
    
class NiH_ToVerif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > NiH > To Verify ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="NiH - XRays To Verify ",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[4]
        dataframe=Studies_list_df[4].loc[Studies_list_df[4]['Status']=='Ready to verify']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) # , showstatusbar=True
        pt.show()
        
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
                
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="NiH Database",bg=white_bg,command=lambda: controller.show_frame(NiH_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Verify",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
        return

class NiH_Complete_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > NiH > Completed ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="NiH - Completed XRays Measurment Tracking ",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
#        dataframe_creator_ff()
#        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=Studies_list_df[4].loc[Studies_list_df[4]['Status']=='Complete']) # , showstatusbar=True
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="NiH Database",bg=white_bg,command=lambda: controller.show_frame(NiH_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',20),bg=white_bg,command=pt.redraw()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        
        return

#####################################################################################################################################################################################
#                                                             CTJ
######################################################################################################################################################################################
 
class CTJ_Database_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        df=Studies_list_df[3]
        CTJ_Database_frame=tk.Frame(self,bg=bg_color)
        CTJ_Database_frame_bottom=tk.Frame(self,bg=bg_color)
        tk.Label(self, text="Home > Studies > CTJ ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(CTJ_Database_frame,text='CTJ DataBase Page',bg=bg_color,font=TITLE_FONT).pack()
        
        tk.Label(CTJ_Database_frame,text='\n',bg=bg_color,font=TITLE_FONT).pack()
        
        AllXRays_frame=tk.Frame(CTJ_Database_frame,bg=white_bg)
        tk.Label(AllXRays_frame, text="Total number of XRays",bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
        tk.Label(AllXRays_frame, text=df['Patient ID'].describe()[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
        AllXRays_frame.pack()
        
        tk.Label(CTJ_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=CTJ_Database_frame)
        
        
        Numbers_frame=tk.Frame(CTJ_Database_frame,bg=bg_color)
        for i in range(len(Poss_status)):
            frame=tk.Frame(Numbers_frame,bg=white_bg)
            tk.Label(frame, text=Poss_status[i],bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
            tk.Label(frame, text=df[(df['Status']==Poss_status[i])&(df['Valid']!='no')].shape[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
            frame.pack(side='left')
            tk.Label(Numbers_frame,text='   ',bg=bg_color).pack(side='left')
        Numbers_frame.pack()
        
        tk.Label(CTJ_Database_frame,text='   ',bg=bg_color).pack(side='left')
        tk.Label(CTJ_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=CTJ_Database_frame)
        tk.Button(CTJ_Database_frame, text='Whole CTJDatabase',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(Raw_CTJ_Database)).pack()
        tk.Label(CTJ_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=CTJ_Database_frame)
        
                #Complete
        tk.Label(CTJ_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=CTJ_Database_frame,side='left')
        tk.Button(CTJ_Database_frame, text='Completed Track',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(CTJ_Complete_Page)).pack(in_=CTJ_Database_frame,side='left')

        #Missing tif
        tk.Label(CTJ_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=CTJ_Database_frame,side='left')
        tk.Button(CTJ_Database_frame, text='Missing tif file',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(CTJ_Missingtif_Page)).pack(in_=CTJ_Database_frame,side='left')
        
        #Ready for Measure
        tk.Label(CTJ_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=CTJ_Database_frame,side='left')
        tk.Button(CTJ_Database_frame, text='Ready for measure',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(CTJ_ToMeasure_Page)).pack(in_=CTJ_Database_frame,side='left')
        
        #Ready for Check
        tk.Label(CTJ_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=CTJ_Database_frame,side='left')
        tk.Button(CTJ_Database_frame, text='Ready to verify',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(CTJ_ToVerif_Page)).pack(in_=CTJ_Database_frame,side='left')
        

        CTJ_Database_frame.pack(expand=True,side='top')
        CTJ_Database_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="All Studies",bg=white_bg,command=lambda: controller.show_frame(Studies_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')


class Raw_CTJ_Database(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > CTJ > Whole Database ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="CTJ - Whole Database",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=Studies_list_df[3]) # , showstatusbar=True
        pt.show()
        
        def Refresh_callback():
            Refresh_CTJ()
            Actual_datetime=strftime('%B %d, %Y %H:%M:%S')
            pt.importCSV(CTJ_csv)
            print('refreshed')
        
        def Save_callback():
            pt.doExport('ephemere.csv') #Exports the whole database to the csv file
            pt.importCSV('ephemere.csv')
            saver=pd.read_csv('ephemere.csv')
            saver[['file name','Valid','Valid_comment','Comment','Date']].dropna(subset=['file name']).to_csv(CTJ_csv_lu)
            print('saved')
            
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="CTJ Database",bg=white_bg,command=lambda: controller.show_frame(CTJ_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Refresh",font=('Arial',14),bg=white_bg,command=lambda:Refresh_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=lambda:Save_callback()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        
        return
    
class CTJ_Missingtif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > CTJ > Missing tif ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="CTJ - Missing tif Database",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[3]
        dataframe=Studies_list_df[3].loc[Studies_list_df[3]['Status']=='Missing tif file']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="CTJ Database",bg=white_bg,command=lambda: controller.show_frame(CTJ_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',20),bg=white_bg,command=pt.redraw()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        return
    
class CTJ_ToMeasure_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > CTJ > To Measure ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="CTJ - XRays To Measure ",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
#
        df=Studies_list_df[3]
        dataframe=Studies_list_df[3].loc[Studies_list_df[3]['Status']=='Ready for measure']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) #showtoolbar=True, showstatusbar=True
        pt.show()

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
                
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="CTJ Database",bg=white_bg,command=lambda: controller.show_frame(CTJ_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Measure",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
        return
    
class CTJ_ToVerif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > CTJ > To Verify ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="CTJ - XRays To Verify ",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[3]
        dataframe= Studies_list_df[3].loc[Studies_list_df[3]['Status']=='Ready to verify']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()
        
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
                
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="CTJ Database",bg=white_bg,command=lambda: controller.show_frame(CTJ_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Verify",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
        return

class CTJ_Complete_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > CTJ > Completed ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="CTJ - Completed XRays Measurment Tracking ",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')

        df=Studies_list_df[3]
        dataframe=Studies_list_df[3].loc[Studies_list_df[3]['Status']=='Complete']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) #showtoolbar=True, showstatusbar=True
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="CTJ Database",bg=white_bg,command=lambda: controller.show_frame(CTJ_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        
        return

#####################################################################################################################################################################################
#                                                             MESA
######################################################################################################################################################################################
 
        
class MESA_Database_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        df =Studies_list_df[5]
        MESA_Database_frame=tk.Frame(self,bg=bg_color)
        MESA_Database_frame_bottom=tk.Frame(self,bg=bg_color)
        tk.Label(self, text="Home > Studies > MESA",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(MESA_Database_frame,text='MESA DataBase Page',bg=bg_color,font=TITLE_FONT).pack()
        
        tk.Label(MESA_Database_frame,text='\n',bg=bg_color,font=TITLE_FONT).pack()
        
        AllXRays_frame=tk.Frame(MESA_Database_frame,bg=white_bg)
        tk.Label(AllXRays_frame, text="Total number of XRays",bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
        tk.Label(AllXRays_frame, text=df['Patient ID'].describe()[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
        AllXRays_frame.pack()
        
        tk.Label(MESA_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=MESA_Database_frame)
        
        Numbers_frame=tk.Frame(MESA_Database_frame,bg=bg_color)
        for i in range(len(Poss_status)):
            frame=tk.Frame(Numbers_frame,bg=white_bg)
            tk.Label(frame, text=Poss_status[i],bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
            tk.Label(frame, text=df[(df['Status']==Poss_status[i])&(df['Valid']!='no')].shape[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
            frame.pack(side='left')
            tk.Label(Numbers_frame,text='   ',bg=bg_color).pack(side='left')
        
        NV_frame=tk.Frame(MESA_Database_frame,bg=white_bg)
        tk.Label(NV_frame, text="Not Valid X-Rays",bg=white_bg,font=('Arial',14,'bold')).pack(side="top", fill="x", pady=10)
        tk.Label(NV_frame, text=df.loc[df['Valid']=='no'].shape[0],bg=white_bg,font=('Arial',11)).pack(side="top", fill="x", pady=10)
        NV_frame.pack()
        Numbers_frame.pack()
        
        tk.Label(MESA_Database_frame,text='   ',bg=bg_color).pack(side='left')
        tk.Label(MESA_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=MESA_Database_frame)
        tk.Button(MESA_Database_frame, text='Whole MESA Database',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(Raw_MESA_Database)).pack()
        tk.Label(MESA_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=MESA_Database_frame)
        
                #Complete
        tk.Label(MESA_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=MESA_Database_frame,side='left')
        tk.Button(MESA_Database_frame, text='Completed Track',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(MESA_Complete_Page)).pack(in_=MESA_Database_frame,side='left')

        #Missing tif
        tk.Label(MESA_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=MESA_Database_frame,side='left')
        tk.Button(MESA_Database_frame, text='Missing tif file',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(MESA_Missingtif_Page)).pack(in_=MESA_Database_frame,side='left')
        
        #Ready for Measure
        tk.Label(MESA_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=MESA_Database_frame,side='left')
        tk.Button(MESA_Database_frame, text='Ready for measure',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(MESA_ToMeasure_Page)).pack(in_=MESA_Database_frame,side='left')
        
        #Ready for Check
        tk.Label(MESA_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=MESA_Database_frame,side='left')
        tk.Button(MESA_Database_frame, text='Ready to verify',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(MESA_ToVerif_Page)).pack(in_=MESA_Database_frame,side='left')
        

        tk.Button(MESA_Database_frame, text='Not Valid X-Rays',bg=white_bg,font=('Arial',14),command=lambda: controller.show_frame(MESA_NotValidPage)).pack(in_=MESA_Database_frame,side='left')
        tk.Label(MESA_Database_frame, text="",bg=bg_color,font=('Arial',11)).pack(in_=MESA_Database_frame,side='left')
        
        MESA_Database_frame.pack(expand=True,side='top')
        MESA_Database_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="All Studies",bg=white_bg,command=lambda: controller.show_frame(Studies_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')

class Raw_MESA_Database(tk.Frame): #Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home > Studies > MESA > Whole Database ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        tk.Label(self, text="MESA - Whole Database",bg=bg_color,font=('Arial',15,'bold')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[5]
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=df)
        pt.show()
        
        def Refresh_callback():
            Refresh_MESA()
            Actual_datetime=strftime('%B %d, %Y %H:%M:%S')
            pt.importCSV(MESA_csv)
            print('refreshed')
        
        def Save_callback():
            pt.doExport('ephemere.csv') #Exports the whole database to the csv file
            pt.importCSV('ephemere.csv')
            saver=pd.read_csv('ephemere.csv')
            saver[['file name','Valid','Valid_comment','Comment']].dropna(subset=['file name']).to_csv(MESA_csv_lu)
            print('saved')
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="MESA Database",bg=white_bg,command=lambda: controller.show_frame(MESA_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Refresh",font=('Arial',14),bg=white_bg,command=lambda:Refresh_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Save changes to the Table",font=('Arial',15,'bold'),bg=white_bg,command=lambda:Save_callback()).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        
        return
    
class MESA_Missingtif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home >Studies > MESA > Missing tif ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="MESA - Missing tif Database",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        
        
        df=Studies_list_df[5]
        dataframe=Studies_list_df[5][(Studies_list_df[5]['Status']=='Missing tif file')&(Studies_list_df[5]['Valid']!='no')]
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) #showtoolbar=True, showstatusbar=True
        pt.show()

        Image_treating=tk.Frame(self,bg=bg_color)        
        
        tk.Label(self, text="",bg=bg_color,font=('Arial',13)).pack(side='bottom')
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="MESA Database",bg=white_bg,command=lambda: controller.show_frame(MESA_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=lambda:Save_callback()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
#        tk.Button(self, text="Refresh",font=('Arial',15),bg=white_bg,command=lambda:Refresh_callback()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        Image_treating.pack(side='bottom')
        
        return
    
class MESA_ToMeasure_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home >Studies > MESA > To Measure ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="MESA - XRays To Measure ",bg=bg_color,font=('Arial',15,'italic','bold')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[5]
        dataframe=Studies_list_df[5][(Studies_list_df[5]['Status']=='Ready for measure')&(Studies_list_df[5]['Valid']!='no')]
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe)
        pt.show()

        MESA_filename='Y:\\10 - Projects\\02-Database managment\\XRay Measurements Tracking Platform\\XRays - MESA -  Updated Database.csv'
        
        path_to_open="explorer "+df['Path'][dataframe.index[0]]

        def Verify_callback():
            global j
            j=0
            path_to_open="explorer "+df['Path'][dataframe.index[0]]
            subprocess.Popen(path_to_open,shell=True)

        def Next_callback():
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
                tk.Label(self, text="All files are verified",bg=bg_color,font=('Arial',11)).pack()
                

        tk.Label(self, text="",bg=bg_color,font=('Arial',13)).pack(side='bottom')
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
        tk.Button(self, text="MESA Database",bg=white_bg,command=lambda: controller.show_frame(MESA_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
#        tk.Button(self, text="Save changes to the Table",font=('Arial',15),bg=white_bg,command=lambda:Save_callback()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',11)).pack(side='bottom')
#        tk.Button(self, text="Refresh",font=('Arial',15),bg=white_bg,command=lambda:Refresh_callback()).pack(side="bottom")
#        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Measure",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')
        
        return
    def restart(self):
        self.refresh()
        self.controller.show_frame(MESA_Missingtif_Page)
    
class MESA_ToVerif_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home >Studies > MESA > To Verify ",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="MESA - XRays To Verify ",bg=bg_color,font=('Arial',15,'bold','italic')).pack(side='top')
        tk.Label(self, text='Last update : '+Actual_datetime,bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        
        df=Studies_list_df[5]
        dataframe=Studies_list_df[5][(Studies_list_df[5]['Status']=='Ready to verify')]
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) #showtoolbar=True, showstatusbar=True
        pt.show()
        
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
                
                tk.Label(Image_treating, text="File "+str(j+1)+" measured",bg=bg_color,font=('Arial',11)).pack()
            else:
                tk.Label(self, text="All files are measured",bg=bg_color,font=('Arial',11)).pack()
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="MESA Database",bg=white_bg,command=lambda: controller.show_frame(MESA_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        Image_treating=tk.Frame(self,bg=bg_color)        
        tk.Button(Image_treating, text="Verify",font=('Arial',15),bg=white_bg,command=lambda:Verify_callback()).pack(side='left')
        tk.Label(Image_treating, text="",bg=bg_color,font=('Arial',15)).pack(side='left')
        tk.Button(Image_treating, text="Next",font=('Arial',15),bg=white_bg,command=lambda:Next_callback()).pack(side='left')
        Image_treating.pack(side='bottom')

        return

class MESA_Complete_Page(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        tk.Label(self, text="Home >Studies > MESA > Completed",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="MESA - Completed XRays Measurment Tracking ",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        
        df=Studies_list_df[5]
        dataframe=Studies_list_df[5][(Studies_list_df[5]['Status']=='Complete')&(Studies_list_df[5]['Valid']=='yes')]
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) #showtoolbar=True, showstatusbar=True
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="MESA Database",bg=white_bg,command=lambda: controller.show_frame(MESA_Database_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')

        
        return
    
class MESA_NotValidPage(tk.Frame):#Shows the raw database. Plots should be created as well
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        tk.Label(self, text="Home >Studies > MESA > Not Valid",bg=bg_color,font=('Arial',9,'italic')).pack(side='top')
        tk.Label(self, text="MESA - Not Valid X-Rays",bg=bg_color,font=('Arial',11,'italic')).pack(side='top')
        
        df=Studies_list_df[5]
        dataframe=df[df['Valid']=='no']
        
        f = tk.Frame(self,bg=bg_color)
        f.pack(fill='both',expand=1)
        self.table = pt = Table(f,dataframe=dataframe) #showtoolbar=True, showstatusbar=True
        pt.show()

        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',10)).pack(side='bottom')
        tk.Button(self, text="MESA Database",bg=white_bg,command=lambda: controller.show_frame(MESA_Database_Page)).pack(side="bottom")

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
        
        
class PCD_Sites_Page(tk.Frame): #Should, from each Site, show only  the XRays corresponding to this Site. Plots sheet is an option too.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        tk.Label(self, text="Choose the site you want the data from :",bg=bg_color, font=TITLE_FONT).pack(side="top", fill="x", pady=10)

        Sites_frame=tk.Frame(self,bg=bg_color)
        Sites_frame_bottom=tk.Frame(self,bg=bg_color)
        for i in range(len(PCD_sites_list)):
            if len(PCD_sites_list[i])<=3:
                label = tk.Label(Sites_frame, text="",bg=bg_color,font=('Arial',11))
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn=tk.Button(Sites_frame, text=PCD_sites_list[i].upper(),bg=white_bg,font=('Arial',14))
#                Site_Bttn.grid(row=r,column=c)
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn.pack(in_=Sites_frame,side='left')
        
        Sites_frame.pack(expand=True,side='top')
        Sites_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
       
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PCD Database Page ",bg=white_bg,command=lambda: controller.show_frame(PCD_Database_Page)).pack(side="bottom")
    
class PEED_Sites_Page(tk.Frame): #Should, from each Site, show only  the XRays corresponding to this Site. Plots sheet is an option too.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        label = tk.Label(self, text="Choose the site you want the data from :",bg=bg_color, font=TITLE_FONT) 
        label.pack(side="top", fill="x", pady=10)

        Sites_frame=tk.Frame(self,bg=bg_color)
        Sites_frame_bottom=tk.Frame(self,bg=bg_color)
        for i in range(len(PEED_sites_list)):
            if len(PCD_sites_list[i])<=3:
                label = tk.Label(Sites_frame, text="",bg=bg_color,font=('Arial',11))
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn=tk.Button(Sites_frame, text=PEED_sites_list[i].upper(),bg=white_bg,font=('Arial',14))
#                Site_Bttn.grid(row=r,column=c)
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn.pack(in_=Sites_frame,side='left')
        
        Sites_frame.pack(expand=True,side='top')
        Sites_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
       
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="PEED Database Page ",bg=white_bg,command=lambda: controller.show_frame(PEED_Database_Page)).pack(side="bottom")
        
class ScoliRisk_Sites_Page(tk.Frame): #Should, from each Site, show only  the XRays corresScoliRiskding to this Site. Plots sheet is an option too.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        label = tk.Label(self, text="Choose the site you want the data from :",bg=bg_color, font=TITLE_FONT) 
        label.pack(side="top", fill="x", pady=10)

        Sites_frame=tk.Frame(self,bg=bg_color)
        Sites_frame_bottom=tk.Frame(self,bg=bg_color)
        for i in range(len(ScoliRisk_sites_list)):
            if len(ScoliRisk_sites_list[i])<=3:
                label = tk.Label(Sites_frame, text="",bg=bg_color,font=('Arial',11))
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn=tk.Button(Sites_frame, text=ScoliRisk_sites_list[i].upper(),bg=white_bg,font=('Arial',14))
#                Site_Bttn.grid(row=r,column=c)
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn.pack(in_=Sites_frame,side='left')
        
        Sites_frame.pack(expand=True,side='top')
        Sites_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
       
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="ScoliRisk Database Page ",bg=white_bg,command=lambda: controller.show_frame(ScoliRisk_Database_Page)).pack(side="bottom")
        
        
class NiH_Sites_Page(tk.Frame): #Should, from each Site, show only  the XRays corresNiHding to this Site. Plots sheet is an option too.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        tk.Label(self, text="Choose the site you want the data from :",bg=bg_color, font=TITLE_FONT).pack(side="top", fill="x", pady=10)

        Sites_frame=tk.Frame(self,bg=bg_color)
        Sites_frame_bottom=tk.Frame(self,bg=bg_color)
        for i in range(len(NiH_sites_list)):
            if len(NiH_sites_list[i])<=3:
                label = tk.Label(Sites_frame, text="",bg=bg_color,font=('Arial',11))
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn=tk.Button(Sites_frame, text=NiH_sites_list[i].upper(),bg=white_bg,font=('Arial',14))
#                Site_Bttn.grid(row=r,column=c)
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn.pack(in_=Sites_frame,side='left')
        
        Sites_frame.pack(expand=True,side='top')
        Sites_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
       
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="NiH Database Page ",bg=white_bg,command=lambda: controller.show_frame(NiH_Database_Page)).pack(side="bottom")
        
        

class CTJ_Sites_Page(tk.Frame): #Should, from each Site, show only  the XRays corresCTJding to this Site. Plots sheet is an option too.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        label = tk.Label(self, text="Choose the site you want the data from :",bg=bg_color, font=TITLE_FONT) 
        label.pack(side="top", fill="x", pady=10)

        Sites_frame=tk.Frame(self,bg=bg_color)
        Sites_frame_bottom=tk.Frame(self,bg=bg_color)
        for i in range(len(CTJ_sites_list)):
            if len(CTJ_sites_list[i])<=3:
                label = tk.Label(Sites_frame, text="",bg=bg_color,font=('Arial',11))
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn=tk.Button(Sites_frame, text=CTJ_sites_list[i].upper(),bg=white_bg,font=('Arial',14))
#                Site_Bttn.grid(row=r,column=c)
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn.pack(in_=Sites_frame,side='left')
        
        Sites_frame.pack(expand=True,side='top')
        Sites_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="CTJ Database Page ",bg=white_bg,command=lambda: controller.show_frame(CTJ_Database_Page)).pack(side="bottom")


class MESA_Sites_Page(tk.Frame): #Should, from each Site, show only  the XRays corresponding to this Site. Plots sheet is an option too.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background=bg_color)
        self.controller=controller
        
        label = tk.Label(self, text="Choose the site you want the data from :",bg=bg_color, font=TITLE_FONT) 
        label.pack(side="top", fill="x", pady=10)

        Sites_frame=tk.Frame(self,bg=bg_color)
        Sites_frame_bottom=tk.Frame(self,bg=bg_color)
        for i in range(len(MESA_sites_list)):
            if len(MESA_sites_list[i])<=3:
                label = tk.Label(Sites_frame, text="",bg=bg_color,font=('Arial',11))
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn=tk.Button(Sites_frame, text=MESA_sites_list[i].upper(),bg=white_bg,font=('Arial',14))
#                Site_Bttn.grid(row=r,column=c)
                label.pack(in_=Sites_frame,side='left')
                Site_Bttn.pack(in_=Sites_frame,side='left')
        
        Sites_frame.pack(expand=True,side='top')
        Sites_frame_bottom.pack(side='bottom',fill='both',expand=True)
        
       
        tk.Button(self, text="Log off",bg=white_bg,command=lambda: controller.show_frame(StartPage)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="Home",bg=white_bg,command=lambda: controller.show_frame(Session_Page)).pack(side="bottom")
        tk.Label(self, text="",bg=bg_color,font=('Arial',20)).pack(side='bottom')
        tk.Button(self, text="MESA Database Page ",bg=white_bg,command=lambda: controller.show_frame(MESA_Database_Page)).pack(side="bottom")
        
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
    app.iconbitmap("HSS-monogram-logo_1400.ico")
    app.mainloop()
    
    
input()