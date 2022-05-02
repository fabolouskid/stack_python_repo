import boto3
import botocore
from botocore.exceptions import ClientError
import cx_Oracle
import os
from ansible_vault import vault

iam=boto3.client('iam')   #we are instantiating IAM CLASS
response=iam.create_user(UserName="PUSER1")
print(response)