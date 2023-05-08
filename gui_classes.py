import tkinter,os
from tkinter import *
import pandas as pd
from tkinter import ttk
import file_reader

class UsrApp():
    cls_list_checkbtn = []
    def __init__(self):
        self.root=Tk()
        self.root.title('Gmail Rotater Bulk EmailSender')
        #frame for email checkbuttons
        self.frm_checkbuttons=Frame(master=self.root,relief=SUNKEN,borderwidth=3)
        self.frm_checkbuttons.pack(side='top',expand=YES,fill=X)
        #frame for email lists
        self.frm_lists=LabelFrame(master=self.root,relief=SUNKEN,borderwidth=3)
        self.frm_lists.pack(side='top',expand=YES,fill=X)

        #random numbers
        self.frame_random=LabelFrame(master=self.root,relief=SUNKEN)
        self.frame_random.pack(side='top')
        self.frame_random_from=LabelFrame(master=self.frame_random,relief=GROOVE)
        self.frame_random_from.pack(side='left')
        self.frame_random_to=LabelFrame(master=self.frame_random,relief=GROOVE)
        self.frame_random_to.pack(side='right')
        #Frame for buttons
        self.frame_btn=LabelFrame(master=self.root,relief=GROOVE)
        self.frame_btn.pack(side='top')
        #Button
        btnStart=self.button_creation(self.frame_btn)
        btnStart.configure(text='START',activeforeground='white',
                             activebackground='dark blue',foreground='dark blue')
        #checkbutton instantiations
        file_email_addresses=file_reader.ReadFile().pathLooker('Email_Addresses/emailaddresses.json')
        self.df=pd.read_json(file_email_addresses)
        self.list_checkbtn=[]
        self.dict_emails={}
        self.count=0
        self.lst_wdgt_var=[]
        for k,v in self.df.items():
            self.lst_wdgt_var.append(IntVar(value=0))
            self.checkbutton_create(k,self.lst_wdgt_var[self.count])
            self.dict_emails[self.count]=k
            self.count +=1
        #dropdown
        self.var_drpdown_receivers = StringVar()
        self.receivers_list=self.dropdown_list('Choose Which Email List(Receivers) To Use','./Prospective_Emails/',self.var_drpdown_receivers)
        #random numbers frame
        self.rnd_start=IntVar()
        self.rnd_finish=IntVar()
        Label(master=self.frame_random_from, text='Enter random number lower limit').pack(side='left')
        Label(master=self.frame_random_to, text='Enter random number upper limit').pack(side='left')
        Entry(master=self.frame_random_from,textvariable=self.rnd_start).pack(side='right')
        Entry(master=self.frame_random_to,textvariable=self.rnd_finish).pack(side='right')

        self.updated_data=StringVar()
        self.lbl_upd_news=Label(master=self.frm_lists,textvariable=self.updated_data,borderwidth=3)
        self.lbl_upd_news.pack(side='right')


    def checkbutton_create(self,txt,text_varble):
        self.wdg_checkbutton=tkinter.Checkbutton(master=self.frm_checkbuttons,text=txt,variable=text_varble,command=lambda : self.checkbtn_add_list_text_values(txt,text_varble.get()))
        self.wdg_checkbutton.pack(side='left',expand=YES,fill=X)

    def checkbtn_add_list_text_values(self,txt,var_text):
        print(var_text)
        if var_text==1:
            self.list_checkbtn.append(txt)
            self.cls_list_checkbtn.append(txt)
        elif var_text==0:
            self.list_checkbtn.remove(txt)
            self.cls_list_checkbtn.remove(txt)


    def button_creation(self,window=None):
        self.btn_0=Button(master=window, overrelief=GROOVE, font=(("Times New Roman"), 12))
        self.btn_0.pack(expand='YES',side='top')
        return self.btn_0

    def dropdown_list(self,text_on_label,path_of_file,variab_txt):
        Label(master=self.frm_lists,text=text_on_label).pack(side='left')
        file_prospective_emails = file_reader.ReadFile().pathLooker(path_of_file)
        self.lst_var=os.listdir(file_prospective_emails)
        self.drpdown=ttk.Combobox(master=self.frm_lists,values=self.lst_var,textvariable=variab_txt)
        self.drpdown.pack(side='left')
        return self.lst_var

class WdgtCheckButton(UsrApp):
    def __init__(self,wdgt_txt):
        self.wdgt_var=IntVar()
        tkinter.Checkbutton(master=self,text=wdgt_txt,variable=self.wdgt_var,command=self.checkbtn_add_list_text_values(self.wdgt_var)).pack()

    def checkbtn_add_list_text_values(self,txt):
        self.list_checkbtn.append(txt)

if __name__=='__main__':
    f=UsrApp()
    f.btn_0.configure(command=lambda : print(f.df))
    f.root.mainloop()
