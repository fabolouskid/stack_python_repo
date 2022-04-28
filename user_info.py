from calendar import c
import tkinter as tk
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
    print("Whoops!")
    print(err);
    sys.exit(1);


#create a new window with the title
window=tk.Tk()
window.title("USER_DETAILS")

#create a new frame
#create a sunken frame

frm_form=tk.Frame(relief=tk.SUNKEN, borderwidth=8)
frm_form.pack()

#Creating FIRST NAME Labels
lbl_first_name=tk.Label(master=frm_form, text="First Name")
ent_first_name=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the First Name
lbl_first_name.grid(row=0, column=0, sticky="e")
ent_first_name.grid(row=0, column=1)


#Creating LAST NAME Labels
lbl_last_name=tk.Label(master=frm_form, text="Last Name")
ent_last_name=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the Last Name
lbl_last_name.grid(row=0, column=1, sticky="e")
ent_last_name.grid(row=0, column=2)

#Creating DOB Labels
lbl_date_of_birth=tk.Label(master=frm_form, text="DOB")
ent_date_of_birth=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the DOB
lbl_date_of_birth.grid(row=1, column=0, sticky="e")
ent_date_of_birth.grid(row=1, column=1)

#Creating Gender Labels
lbl_Gender=tk.Label(master=frm_form, text="Gender")
ent_Gender=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the DOB
lbl_Gender.grid(row=1, column=1, sticky="e")
ent_Gender.grid(row=1, column=2)

 #Creating Address Labels
lbl_address=tk.Label(master=frm_form, text="Address")
ent_address=tk.Entry(master=frm_form, width=50)

 #Positioning the Label and the Text Field for the Address
lbl_address.grid(row=2, column=0, sticky="e")
ent_address.grid(row=2, column=1)

 #Creating cc_no Labels
lbl_cc_no=tk.Label(master=frm_form, text="CC no")
ent_cc_no=tk.Entry(master=frm_form, width=50)

 #Positioning the Label and the Text Field for the cc_no
lbl_cc_no.grid(row=2, column=1, sticky="e")
ent_cc_no.grid(row=2, column=2)

#Creating cc_exp Labels
lbl_cc_exp=tk.Label(master=frm_form, text="CC exp")
ent_cc_exp=tk.Entry(master=frm_form, width=50)

 #Positioning the Label and the Text Field for the cc_exp
lbl_cc_exp.grid(row=3, column=0, sticky="e")
ent_cc_exp.grid(row=3, column=1)


#  #Creating cc_cvv Labels
lbl_cc_cvv=tk.Label(master=frm_form, text="CC cvv")
ent_cc_cvv=tk.Entry(master=frm_form, width=50)

#  #Positioning the Label and the Text Field for the cc_cvv
lbl_cc_cvv.grid(row=3, column=1, sticky="e")
ent_cc_cvv.grid(row=3, column=2)

#Creating Order id Labels
lbl_order_id=tk.Label(master=frm_form, text="Order ID")
ent_order_id=tk.Entry(master=frm_form, width=50)

 #Positioning the Label and the Text Field for the Order id
lbl_order_id.grid(row=4, column=0, sticky="e")
ent_order_id.grid(row=4, column=1)

#  #Creating Order Name Labels
lbl_order_name=tk.Label(master=frm_form, text="Order Name")
ent_order_name=tk.Entry(master=frm_form, width=50)

#  #Positioning the Label and the Text Field for the Order Name
lbl_order_name.grid(row=4, column=1, sticky="e")
ent_order_name.grid(row=4, column=2)

#Creating Order Status Labels
lbl_order_status=tk.Label(master=frm_form, text="Order Status")
ent_order_status=tk.Entry(master=frm_form, width=50)

 #Positioning the Label and the Text Field for the Order Status
lbl_order_status.grid(row=5, column=0, sticky="e")
ent_order_status.grid(row=5, column=1)

#  #Creating Tracking # Labels
lbl_tracking_number=tk.Label(master=frm_form, text="Tracking Number")
ent_tracking_number=tk.Entry(master=frm_form, width=50)

#  #Positioning the Label and the Text Field for the Tracking #
lbl_tracking_number.grid(row=5, column=1, sticky="e")
ent_tracking_number.grid(row=5, column=2)

frm_buttons=tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)


def view_order_details(event):
    print("Lets view user account details")
    try:
        connection = cx_Oracle.connect(user="STACK_USERPROFILE_DEJ", password="stackinc", dsn="stack-db.cc5iigzknvxd.us-east-1.rds.amazonaws.com/RDS")
        print(connection.version)
        cursor = connection.cursor() 
    except Exception as e:
         print(e)
    else:
         print("Lets begin executing select statements")
         cursor.execute("""select * from VW_USER_PROFILE_DEJ """)
         res = cursor.fetchall()
         print(res)
         ent_first_name.insert(0, res[0][0])
         ent_last_name.insert(0, res[0][1])
         ent_date_of_birth.insert(0, res[0][2])
         ent_Gender.insert(0, res[0][3])
         ent_address.insert(0, res[0][4])
         ent_cc_no.insert(0, res[0][5])
         ent_cc_exp.insert(0, res[0][6])
         ent_cc_cvv.insert(0, res[0][7])
         ent_order_id.insert(0, res[0][8])
         ent_order_status.insert(0, res[0][9])
         ent_tracking_number.insert(0, res[0][10])





         

         

# '''cursor.execute("""
#      SELECT first_name, last_name
#      FROM employeer
#      WHERE department_id = :did AND employee_id > :eid""",
#      did = 50,
#      eid = 190)'''









def handle_cancel(event):
    print("The process was cancelled")
    exit()




btn_view_order_details=tk.Button(master=frm_buttons, text="View Order Details")
btn_view_order_details.pack(side=tk.RIGHT, padx=10, ipadx=10)
btn_view_order_details.bind("<Button-1>", view_order_details)



btn_cancel=tk.Button(master=frm_buttons, text="Cancel")
btn_cancel.pack(side=tk.RIGHT, ipadx=10)
btn_cancel.bind("<Button-1>", handle_cancel)
























window.mainloop()