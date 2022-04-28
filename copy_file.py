from calendar import c
import tkinter as tk
import sys
import os
import datetime
import shutil
import time

#create a new window with the title
window=tk.Tk()
window.title("Copy File or Directory")


#create a new frame
#create a sunken frame

frm_form=tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

#Creating Source Directory Labels
lbl_source_dir=tk.Label(master=frm_form, text="Source Directory")
ent_source_dir=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the Source Directory
lbl_source_dir.grid(row=0, column=0, sticky="e")
ent_source_dir.grid(row=0, column=1)

#Create the label and entry for destination directory
lbl_dest_dir=tk.Label(master=frm_form, text="Destination Directory")
ent_dest_dir=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the Destination Directory
lbl_dest_dir.grid(row=1, column=0, sticky="e")
ent_dest_dir.grid(row=1, column=1)

#Creating Runner Labels
lbl_runner=tk.Label(master=frm_form, text="Runner section")
ent_runner=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the runner
lbl_runner.grid(row=2, column=0, sticky="e")
ent_runner.grid(row=2, column=1)


#Creating a label and entry for backup types
lbl_backup_type=tk.Label(master=frm_form, text="Backup Type(F(file), D(directory)")
ent_backup_type=tk.Entry(master=frm_form, width=50)

#Positioning the Label and the Text Field for the Backup type
lbl_backup_type.grid(row=3, column=0, sticky="e")
ent_backup_type.grid(row=3, column=1)

#Creating Frames that woud hold the buttons
frm_buttons=tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

#PUT FUNCTIONS HERE
def COPY_FILE(a,b, c, d):
    source_loc=a
    destination=b
    runner=c
    option=d
   
    if option == "F":
      print("Lets begin copying the file process")
      try:
 
         if not os.path.exists(destination):
            os.makedirs(destination)
            print("***********************")
            print("verify " + destination + " exists ")
            print("***********************")

            check=os.path.isdir(destination)
            print(check)
            print("###########################################################")
#  elif print("The directory has been created"):
#         else:
            print("The " + destination + " directory exists ")
            print("The directory exists")
        
            print("I am copying a file from " + source_loc + " to " + destination)
  
            print("**************************************************************************")
            print("Now copying files from " + source_loc + " to "  + destination + " directory ")
            print("**************************************************************************")

 #           a = "db_schema_list_2.log"  
 #           source = source_loc + a
#            dest = destination + "/" +  a     
            print("Copying only file")
#            if os.path.isfile(source):
            os.path.isfile(source_loc)
            shutil.copy(source_loc,destination)
 #           print('copied', a)
            dir_list = os.listdir(destination)
            print(dir_list)
#            else:
#              print("You got it wrong. Try again")
            print("Succesfully copied")

 #           print("Sending Notification via " + EMAIL)
 #           smtpServer = 'localhost'
 #           server = smtplib.SMTP(smtpServer)
 #           FROM = 'oracle@MKIT-DEV-OEM.localdomain'
 #           TO = EMAIL
 #           MSG = "File Backup was successful"            

 #           server.sendmail(FROM, TO, MSG)
            
#            server.quit()
#            print("Email received")

      except:
            print("###########################################################")
            print('source file does not exist')
            print("###########################################################")
#            print('Sending email notification')
#            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#            server.login(EMAIL, E_PASS)
#            server.sendmail(EMAIL, EMAIL, "Hello, Copy failed")
#            server.quit()

#            smtpServer = 'localhost'
#            server = smtplib.SMTP(smtpServer)
             
#            FROM = 'oracle@MKIT-DEV-OEM.localdomain'
 #           TO = EMAIL

#            MSG = "File Backup failed"

#            server.sendmail(FROM, TO, MSG)

#            server.quit()


def handle_submit(event):
    print("The submit button was clicked")
    src_dir, dest_dir, runner, backup_type=ent_source_dir.get(),ent_dest_dir.get(),ent_runner.get(),ent_backup_type.get()
    print("The source directory is " + src_dir)
    print("The destination directory is " + dest_dir)
    print("The runner is " + runner)
    print("The backup type is " + backup_type)
    COPY_FILE(src_dir, dest_dir, runner, backup_type)

def handle_cancel(event):
    print("The process was cancelled")
    exit()



btn_submit=tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
btn_submit.bind("<Button-1>", handle_submit)


btn_cancel=tk.Button(master=frm_buttons, text="Cancel")
btn_cancel.pack(side=tk.RIGHT, ipadx=10)
btn_cancel.bind("<Button-1>", handle_cancel)


window.mainloop()