import json
import os,csv
import smtplib,ssl
from smtplib import SMTPSenderRefused,SMTPServerDisconnected

import gui_classes
import yagmail
import pandas as pd
import file_reader
import time
import threading
import random
from email.mime.text import MIMEText

gui=gui_classes.UsrApp()

def send_email_with_password():
    count=0
    receiver_addresses = read_receivers_as_list()
    for n in range(1,receiver_addresses):
        print('n is',n)
        with smtplib.SMTP('smtp.gmail.com','587') as email:
            email.set_debuglevel(1)
            email.starttls(context=ssl.create_default_context())
            email_id,passw=read_email_addresses_and_password_as_list(n)
            gui.updated_data.set('logged in as : ' +email_id)
            time.sleep(rand_nums())
            email.login(email_id,passw)
            receiver,template_name,subject_name=read_receivers_as_list2(n)
            message_html=read_txt_as_list(template_name)
            subj=read_subjects_as_list(subject_name)
            gui.updated_data.set(str(subj))
            myEmail=MIMEText(message_html,'html')
            myEmail['From']=email_id
            myEmail['To']=receiver
            myEmail['Subject']=subj
            print(email_id,passw,receiver,myEmail.as_string())
            email.sendmail(email_id,receiver,myEmail.as_string())
            gui.updated_data.set(str(n)+' email sent to receipient '+ receiver)
            time.sleep(rand_nums())
            #sleep randomly
            time.sleep(rand_nums())
            gui.updated_data.set('sleeping seconds '+str(rand_nums()))
            count=n
    gui.updated_data.set('finished sending to all '+str(count)+' receipients')

def read_email_addresses_and_password_as_list(n=0):
    """read from file in Email Address folder, and return on each call key(email id),value(password) as tuple"""
    file_=file_reader.ReadFile().pathLooker('./Email_Addresses/emailaddresses.json')
    df=pd.read_json(file_)

    if n >= len(df.to_dict().values()):
        n=0
    return df.keys()[n],df.values[0][n]

def read_txt_as_list(selected_template='EmailTemplate1.txt'):
    selected_template=selected_template+'.txt'
    file_=file_reader.ReadFile().pathLooker('./Text_Email/'+str(selected_template))
    msg=open(file_,'r').read()
    return msg

def read_receivers_as_list():
    selected_list_receivers=gui.var_drpdown_receivers.get()
    file_ = file_reader.ReadFile().pathLooker('./Prospective_Emails/' + str(selected_list_receivers))
    csv_ = open(file_,'r')
    data=list(csv.reader(csv_,delimiter=' '))
    csv_.close()
    return len(data)

def read_receivers_as_list2(n=0):
    selected_list_receivers=gui.var_drpdown_receivers.get()
    file_ = file_reader.ReadFile().pathLooker('./Prospective_Emails/' + str(selected_list_receivers))
    csv_ = open(file_,'r')
    data=list(csv.reader(csv_,delimiter=' '))
    csv_.close()
    if n>=len(data):
        n=0
    data_=data[n][0]
    email_data=data_.split(',')[0]
    email_template = data_.split(',')[1]
    subj = data_.split(',')[2]
    return email_data,email_template,subj

def read_subjects_as_list(n='Subject1'):
    file_ = file_reader.ReadFile().pathLooker('./Subjects/Subjects.csv')
    csv_ = open(file_,'r')
    data=dict(csv.reader(csv_,delimiter=','))
    print(data)
    csv_.close()
    return data[n]

def start():
    t1=threading.Thread(target=send_email_with_password)
    t1.start()

def rand_nums():
    return (random.randint(gui.rnd_start.get(),gui.rnd_finish.get()))

gui.btn_0.configure(command=start)
gui.root.mainloop()

#pyinstaller -F --add-data "./Subjects/Subjects.csv;./Subjects" --add-data "./Text_Email/EmailTemplate1.txt;./Text_Email" "./Text_Email/EmailTemplate2.txt;./Text_Email" --add-data "./Email_Addresses/emailaddresses.json;./Email_Addresses" --add-data "./Prospective_Emails/List_A.csv;./Prospective_Emails/" main.py --clean --onefile --noconsole
