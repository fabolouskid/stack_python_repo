from calendar import c
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from tkcalendar import Calendar, DateEntry
from  datetime import date
import sys
import os
import datetime
import shutil
import time
import cx_Oracle

try:
    if sys.platform.startswith("darwin"):
         lib_dir = os.path.join(os.environ.get("HOME"), "Downloads","instantclient_19_8")
         cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    elif sys.platform.startswith("win32"):
         lib_dir=r"C:\Users\ayodeji.b.fagbamila\Downloads\instantclient_21_3"
         cx_Oracle.init_oracle_client(lib_dir=lib_dir)
except Exception as err:
    ("Whoops!")
    (err);
    sys.exit(1);




#create a new window with the title
window=tk.Tk()
window.title("CREATE USER PROFILE")
#window.minsize(width=200, height=250)
#window.geometry("400x400")
# window.configure(bg='white')
#window.rowconfigure(0, minsize=800, weight=1)
#window.columnconfigure(1, minsize=800, weight=1)



#create a new frame
#create a sunken frame

frm_form=tk.Frame(relief=tk.SUNKEN, borderwidth=5, bg="white", width=1000, height=1000)
frm_form.pack()

# Dropdown menu options


#Creating FIRST NAME Labels
lbl_first_name=tk.Label(master=frm_form, text="First Name", foreground="black", background="white", font='Helvetica 9 bold')
ent_first_name=tk.Entry(master=frm_form, width=50, fg="black", bg="white", highlightcolor = "purple", highlightbackground="red")

#Positioning the Label and the Text Field for the First Name
lbl_first_name.grid(row=0, column=0, sticky="e")
ent_first_name.grid(row=0, column=1)


#Creating LAST NAME Labels
lbl_last_name=tk.Label(master=frm_form, text="Last Name", foreground="black", background="white", font='Helvetica 9 bold')
ent_last_name=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the Last Name
lbl_last_name.grid(row=2, column=0, sticky="e")
ent_last_name.grid(row=2, column=1)


#Creating Address Labels
lbl_address=tk.Label(master=frm_form, text="Address", foreground="black", background="white", font='Helvetica 9 bold')
ent_address=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the Address
lbl_address.grid(row=4, column=0, sticky="e")
ent_address.grid(row=4, column=1)

#Creating Email Address Labels
lbl_email_address=tk.Label(master=frm_form, text="Email Address", foreground="black", background="white", font='Helvetica 9 bold')
ent_email_address=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the Email Address
lbl_email_address.grid(row=6, column=0, sticky="e")
ent_email_address.grid(row=6, column=1)

#Creating Password Labels
lbl_password=tk.Label(master=frm_form, text="Password", foreground="black", background="white", font='Helvetica 9 bold')
ent_password=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the Password
lbl_password.grid(row=8, column=0, sticky="e")
ent_password.grid(row=8, column=1)

#Creating DOB Labels
lbl_date_of_birth=tk.Label(master=frm_form, text="DOB", foreground="black", background="white", font='Helvetica 9 bold')
#ent_date_of_birth=tk.Entry(master=frm_form, width=50)
ent_date_of_birth=DateEntry(master=frm_form,selectmode='day')

#Positioning the Label and the Text Field for the DOB
lbl_date_of_birth.grid(row=10, column=0, sticky="e")
#ent_date_of_birth.grid(row=10, column=1)
ent_date_of_birth.grid(row=10,column=1, sticky="w")

#Creating Gender Labels
lbl_Gender=tk.Label(master=frm_form, text="Gender", foreground="black", background="white", font='Helvetica 9 bold')
#ent_Gender=tk.Entry(master=frm_form, width=50)

# Create a combobox to setup the dropdown menu for Gender
ent_Gender = ttk.Combobox(master=frm_form, 
                            values=[
                                    "M",
                                    "F"])
print(dict(ent_Gender)) 

ent_Gender.current(0)

print(ent_Gender.current(), ent_Gender.get())


#Positioning the Label and the Text Field for the DOB
lbl_Gender.grid(row=12, column=0, sticky="e")
ent_Gender.grid(row=12, column=1, sticky="w")

#Creating Credit Card # Labels
lbl_Credit_Card_no=tk.Label(master=frm_form, text="CC no", foreground="black", background="white", font='Helvetica 9 bold')
ent_Credit_Card_no=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the Credit Card #
lbl_Credit_Card_no.grid(row=14, column=0, sticky="e")
ent_Credit_Card_no.grid(row=14, column=1)

#Creating CC_exp Labels
lbl_Credit_Card_exp=tk.Label(master=frm_form, text="CC exp", foreground="black", background="white", font='Helvetica 9 bold')
#ent_Credit_Card_exp=tk.Entry(master=frm_form, width=50)
ent_Credit_Card_exp=DateEntry(master=frm_form,selectmode='day')


#Positioning the Label and the Text Field for the CC_exp
lbl_Credit_Card_exp.grid(row=16, column=0, sticky="e")
ent_Credit_Card_exp.grid(row=16, column=1, sticky="w")

#Creating CC_cvv Labels
lbl_Credit_Card_cc_cvv=tk.Label(master=frm_form, text="CC cvv", foreground="black", background="white", font='Helvetica 9 bold')
ent_Credit_Card_cc_cvv=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the CC_cvv
lbl_Credit_Card_cc_cvv.grid(row=18, column=0, sticky="e")
ent_Credit_Card_cc_cvv.grid(row=18, column=1)

#Creating CC_Type Labels
lbl_Credit_Card_Type=tk.Label(master=frm_form, text="CC Type", foreground="black", background="white", font='Helvetica 9 bold')
#ent_Credit_Card_Type=tk.Entry(master=frm_form, width=50)

# Create a combobox to setup the dropdown menu for Credit Card Type
ent_Credit_Card_Type = ttk.Combobox(master=frm_form, 
                            values=[
                                    "Amex",
                                    "Discovery",
                                    "MasterCard",
                                    "Visa"])
print(dict(ent_Credit_Card_Type)) 

ent_Credit_Card_Type.current(0)

#print(ent_Credit_Card_Type.current(), ent_Credit_Card_Type.get())

#Positioning the Label and the Text Field for the CC_cvv
lbl_Credit_Card_Type.grid(row=20, column=0, sticky="e")
ent_Credit_Card_Type.grid(row=20, column=1, sticky="w")




#Creating Frames that woud hold the buttons
#frm_create_account=tk.Frame()
#frm_create_account.pack(fill=tk.X, ipadx=5, ipady=5)

frm_buttons=tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

#PUT FUNCTION FOR NEW USER HERE


 #   FNAME=a
 #   LNAME=b
 #   GENDER=g
 #   DOB=f
 #   EMAIL=d
 #   """
 #   Insert a row to the customer table
 #   :param a:
 #   :param b:
 #   :param d:
 #   :param f:
 #   :param g:
 #   :return:
#    """
    
#     ("Lets get started")
#     try:
#        connection = cx_Oracle.connect(user="STACK_USERPROFILE_DEJ", password="stackinc", dsn="stack-db.cc5iigzknvxd.us-east-1.rds.amazonaws.com/RDS")
#        (connection.version)
#        cursor = connection.cursor() 
#     except Exception as e:
#        (e)
# #    cursor.execute('insert into customer(FNAME,LNAME,GENDER,DOB,EMAIL) ''values(SEQ_USERPROFILE_DEJ.nextval,:a,:b,:g,:f,:d)')
# #    cursor.execute("""insert into customer(CUST_ID,FNAME,LNAME,GENDER,DOB,EMAIL) values(SEQ_USERPROFILE_DEJ.nextval,'a','b','g',to_date(f,'MM-DD-YYYY'),'d')""") 
#     #trial="SEQ_USERPROFILE_DEJ.nextval"
#     else:
#        cursor.execute("""insert into customer(CUST_ID,FNAME,LNAME,GENDER,DOB,EMAIL) values(:CUST_ID,:FNAME,:LNAME,:GENDER,to_date(:DOB,'MM-DD-YYYY'),:EMAIL)""", 
#        CUST_ID=28,
#        FNAME=ent_first_name.get(),
#        LNAME=ent_last_name.get(),
#        GENDER=ent_Gender.get(),
#        DOB=ent_date_of_birth.get(),
#        EMAIL=ent_email_address.get())
# #   cursor.execute(sql_insert)
#        ("Insert Completed")
#        cursor.close()
#        connection.commit 
#        connection.close()



def handle_create_account(event):
    ("The create account button was clicked")
    #first_name, last_name, address, email_address, password, date_of_birth, Gender=ent_first_name.get(),ent_last_name.get(),ent_address.get(),ent_email_address.get(),ent_password.get(),ent_date_of_birth.get(),ent_Gender.get()
    ("Lets get started")
    try:
        connection = cx_Oracle.connect(user="STACK_USERPROFILE_DEJ", password="stackinc", dsn="stack-db.cc5iigzknvxd.us-east-1.rds.amazonaws.com:1521/RDS")
        (connection.version)
        cursor = connection.cursor() 
    except Exception as e:
        (e)
    #    cursor.execute('insert into customer(FNAME,LNAME,GENDER,DOB,EMAIL) ''values(SEQ_USERPROFILE_DEJ.nextval,:a,:b,:g,:f,:d)')
    #    cursor.execute("""insert into customer(CUST_ID,FNAME,LNAME,GENDER,DOB,EMAIL) values(SEQ_USERPROFILE_DEJ.nextval,'a','b','g',to_date(f,'MM-DD-YYYY'),'d')""") 
    #trial="SEQ_USERPROFILE_DEJ.nextval"
    else:
        cursor.execute("""SELECT SEQ_USERPROFILE_DEJ.nextval FROM DUAL""")
        seq_id = cursor.fetchall()
        (seq_id)

        cursor.execute("""insert into customer(CUST_ID,FNAME,LNAME,GENDER,DOB,EMAIL) values(:CUST_ID, :FNAME, :LNAME, :GENDER, to_date(:DOB,'MM-DD-YYYY'), :EMAIL)""", 
        CUST_ID=seq_id[0][0],
        FNAME=ent_first_name.get(),
        LNAME=ent_last_name.get(),
        GENDER=ent_Gender.get(),
        DOB=ent_date_of_birth.get(),
        EMAIL=ent_email_address.get())
        (ent_first_name.get())
        connection.commit() 
    #   cursor.execute(sql_insert)
        ("Insert Completed")
     #   cursor.close()
    #    connection.close()

        cursor.execute("""insert into demographics(CUST_ID,DEM_ID,ADDRESS,ADDRESS_TYPE,DEFAULTS) values(:CUST_ID, :DEM_ID, :ADDRESS, :ADDRESS_TYPE, :DEFAULTS)""",
        CUST_ID=seq_id[0][0],
        DEM_ID=214,
        ADDRESS=ent_address.get(),
        ADDRESS_TYPE="R",
        DEFAULTS="Y")
        (ent_address.get())
        connection.commit() 
        # cursor.close()
        # connection.close()

        cursor.execute("""insert into credit_card(CUST_ID,CC_NO,CC_EXP,CC_CVV,CC_TYPE) values(:CUST_ID, :CC_NO, to_date(:CC_EXP,'MM-DD-YYYY'), :CC_CVV, :CC_TYPE)""",
        CUST_ID=seq_id[0][0],
        CC_NO=ent_Credit_Card_no.get(),
        CC_EXP=ent_Credit_Card_exp.get(),
        CC_CVV=ent_Credit_Card_cc_cvv.get(),
        CC_TYPE=ent_Credit_Card_Type.get())
        connection.commit() 
        cursor.close()
        connection.close()


def handle_cancel(event):
    ("The process was cancelled")
    exit()



btn_create_account=tk.Button(master=frm_buttons, text="Create Account", bg="black", fg="white")
btn_create_account.pack(side=tk.RIGHT, padx=10, ipadx=10)
btn_create_account.bind("<Button-1>", handle_create_account)



btn_cancel=tk.Button(master=frm_buttons, text="Cancel", bg="white")
btn_cancel.pack(side=tk.RIGHT, ipadx=10)
btn_cancel.bind("<Button-1>", handle_cancel)








window.mainloop()