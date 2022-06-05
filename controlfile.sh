#!/bin/bash

DB=$1

control_file_loc=/u02/CDBSOS1/CONTROLFILES

echo "#####################################"
echo "Verify Control file Directory oExists"
echo "#####################################"


if [ -d "${control_file_loc}" ] 
then
    echo "Directory ${control_file_loc} exists." 
else
    echo "*****************************************************"
    echo "Error: Directory ${control_file_loc} does not exists."
    echo "*****************************************************"

    
    echo "#####################################################"
    echo "Creating ${control_file_loc} directory"
    echo "#####################################################"

    mkdir -p ${control_file_loc}

fi

#read -p "Please Enter first new Control file Directory and Name: "

#read -p "Please Enter second new Control file Directory and Name: "


read -p "Enter database you need to access: " DB


echo "**************************************************"
echo "Let us access the database and ensure connectivity"
echo "**************************************************"

source sos1_home

export ORACLE_SID=$DB


sqlplus -s oracle / Pa$$word_123 << EOF
set heading off pagesize 0 term off echo off feedback off
spool '${control_file_loc}/control_file.log'
show parameter control_files
alter system set control_files='${control_file_loc}/control01.ctl','${control_file_loc}/control02.ctl' scope=spfile;
spool off

EOF

echo "**************************************************"
echo "Shutdown the Database and put it in NOMount Mode"
echo "**************************************************"


sqlplus -s oracle / Pa$$word_123 << EOF
shutdown immediate;
startup nomount
EOF



echo "*********************************************************************"
echo "Restore controlfile to new location Using RMAN"
echo "*********************************************************************"


rman target oracle / Pa$$word_123 << EOF
restore controlfile from '';
EOF

echo "################################################"
echo "Restoration of Control File Successful"
echo "################################################"


echo "*********************************************************************"
echo "Log back into the Standby Database and place it in mount mode"
echo "*********************************************************************"

sqlplus -s oracle / Pa$$word_123 << EOF
alter database mount;
show parameter control_files
EOF



