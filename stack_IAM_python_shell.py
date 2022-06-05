from ast import Pass
import boto3
import botocore
from botocore.exceptions import ClientError
import cx_Oracle
import os
import json

####https://www.learnaws.org/2021/05/12/aws-iam-boto3-guide/
####hands-on.cloud/working-with-iam-in-python-using-boto3/

def aws_create_user(**args):
 try:
     iam=boto3.client(args['service'])   #we are instantiating IAM CLASS
     response=iam.create_user(UserName=args['user'],
          Tags=[
              {
                  'Key': 'Class',
                  'Value': 'Python'
              },
          ]
     )
     print(response['User'])
     
     print("***********************************************")
     print("Create a Login profile for the new user created")
     print("*************************************************")

     password=input('Please provide new user password: ')
     response2 = iam.create_login_profile(Password=password,PasswordResetRequired=True,UserName=args['user'])
     print(response2['LoginProfile']['UserName'])

     print("###################################################")
     print("List all Current User in the AWS Account")
     print("###################################################")
     

     paginator=iam.get_paginator('list_users')
     for response3 in paginator.paginate():
         for user in response3["Users"]:
             print(f"Username: {user['UserName']}, Arn: {user['Arn']}")

 #    print(response['User']['UserName'])
 #    print(response['User']['Arn'])
     #response=iam.list_users()
     #print(response['Users'])
 except ClientError as error:
      if error.response['Error']['Code']=='EntityAlreadyExists':
          print("User already exists....use same use ?")
          val=input('Enter Y for Yes or N for No: ')
          if val =='Y':
              print("You want to use the same user")
              Pass
          else:
              print("You want to create a new user")
              new_user=input('Enter new User name')
              response=iam.create_user(UserName=new_user)
              print(response)

      else:
           print("Unexpected error occured while creating....exiting from here", error)
           return 'User could not be created', error

def delete_aws_user(**args):
   
   print("***********************************************")
   print("Delete User Login Profile")
   print("*************************************************")
   
   iam=boto3.client(args['service'])
   response_del=iam.delete_login_profile(UserName=args['user'])
   iam.delete_user(UserName=args['user'])
##   response=iam.list_users()

   print("********************************************")
   print("List all Current Users After user deletion")
   print("********************************************")

   paginator=iam.get_paginator('list_users')
   for response3 in paginator.paginate():
           for user in response3["Users"]:
               print(f"Username: {user['UserName']}, Arn: {user['Arn']}")



def aws_create_iam_policy(**args):
 #try:
     iam=boto3.client(args['service'])   #we are instantiating IAM CLASS
     print("***********************************************")
     print("Creating new IAM Policy")
     print("*************************************************")

     ##iam_policy=iam.create_policy(PolicyName=args['policy'],PolicyDocument='//c/Apps/Python/my_manged_policy.json',Description='Admin Policy')
     my_managed_policy = {
          "Version": "2012-10-17",
          "Statement": [
              {
                 "Effect": "Allow",
                 "Action": "*",
                 "Resource": "*"
              }
         ]       
     }
     iam_new_policy=iam.create_policy(PolicyName=args['policy'],PolicyDocument=json.dumps(my_managed_policy))
     print(iam_new_policy['Policy']['Arn'])

     
def aws_create_iam_group(**args):
     iam=boto3.client(args['service'])   #we are instantiating IAM CLASS
     print("***********************************************")
     print("Creating User Group")
     print("*************************************************")

     iam_new_user_group=iam.create_group(GroupName=args['Newgroup'])
     print(iam_new_user_group['Group']['Arn'])


def aws_attach_group_to_policy(**args):
     iam=boto3.client(args['service'])   #we are instantiating IAM CLASS
     print("***********************************************")
     print("Attaching Policy to User Group")
     print("*************************************************")

     iam_attach_policy_to_group=iam.attach_group_policy(GroupName=args['group_name'],PolicyArn=args['PolicyArn'])
     print(iam_attach_policy_to_group)

#Check JSON OUTPUT FOR DELETED USER--------
def attach_user_to_group(**args):
     iam=boto3.client(args['service'])   #we are instantiating IAM CLASS
     print("***********************************************")
     print("Attaching User to Group")
     print("*************************************************")

     iam_attach_user_to_group=iam.add_user_to_group(UserName=args['UserName'],GroupName=args['GroupName'])
     print(iam_attach_user_to_group)
   

def aws_Iam_role(**args):
     iam=boto3.client(args['service'])   #we are instantiating IAM CLASS
     print("***********************************************")
     print("Creating an IAM role with Policy attached to it")
     print("*************************************************")
    
     assume_role_policy_document = json.dumps({
    "Version": "2012-10-17",
    "Statement": [
          {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::966876545122:root"
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
          }
       ]
    })

     iam_create_role=iam.create_role(RoleName=args['rolename'],AssumeRolePolicyDocument = assume_role_policy_document)
     print(iam_create_role['Role']['RoleName'])

     print("#############################################################################################")
     print("Now that IAM role has been created with Trusted Entity,We going to attach Admin policy to it ")
     print("#############################################################################################")

     iam_role_with_policy_attached = iam.attach_role_policy(RoleName=args['rolename'],PolicyArn=policy_arn)
     print(iam_role_with_policy_attached)
     
def aws_mfa(**args):
     iam=boto3.client(args['service'])   #we are instantiating IAM CLASS
     print("***********************************************")
     print("Setting up MUltifactor Authentication for New/oldUser")

##     iam_client.create_virtual_mfa_device(Path='/service-user/',VirtualMFADeviceName='kjh-SuperDuperUser')

if __name__=="__main__":
   val=input('Welcome to my IAM code: " + '"\n" + "Type add to create new user, Type del to delete user, Type pol to create new policy, Type grp to create new group, Type perm2grp to attach permission to group, Type user2grp to add user to group, Type crt_role to create a role with a policy, Type mfa to setup security authentication for users: ")
   if val=='add':
       useradd=input('Enter user name: ')
       aws_create_user(service="iam",user=useradd)
   elif val=='del':
       iam=boto3.client("iam")
       paginator=iam.get_paginator('list_users')
       for response3 in paginator.paginate():
           for user in response3["Users"]:
               print(f"Username: {user['UserName']}, Arn: {user['Arn']}")

       userdel=input('Enter username to delete: ')
       delete_aws_user(service="iam",user=userdel)
   elif val=='pol':
       newpolicy=input('Enter New Policy Name: ')
       aws_create_iam_policy(service="iam",policy=newpolicy )
   elif val=='grp':
        newgrp=input('Enter New User Group Name: ')
        aws_create_iam_group(service="iam",Newgroup=newgrp )
   elif val=='perm2grp':
        grp_name=input('Enter group Name to be attached to Policy: ')
        policy_arn=input('Enter Policy arn to be attached to : ')
        aws_attach_group_to_policy(service="iam",PolicyArn=policy_arn, group_name=grp_name)
   elif val=='user2grp':
        grp_name=input('Enter group Name to add user into: ')
        user_name=input('Enter user Name to add to group: ')
        attach_user_to_group(service="iam",GroupName=grp_name,UserName=user_name)
   elif val=='crt_role':
        role_name=input('Enter Iam Role name to be created: ')
        policy_arn=input('Enter Policy name to attach to Iam Role:')
        aws_Iam_role(service="iam",rolename=role_name,PolicyArn=policy_arn)
   else:
        val=='mfa'
        aws_mfa(service="iam")

         
  
  
##   val=input('Welcome to my IAM code: " + '"\n" + "Do you want to create a new user? Y for Yes or N for No:  ")
##   if val=='Y':
##       useradd=input('Enter user name: ')
##       aws_create_user(service="iam",user=useradd)
##   else:
##       userdel=input('Enter username to delete: ')
##       delete_aws_user(service="iam",user=userdel)      
  # aws_create_user(service="iam",user="PUSER4")