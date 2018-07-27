#!/usr/bin/env python
import boto3
iam = boto3.client('iam')
response = iam.create_user(UserName='AWSSAA05')
print response
response['User']['Arn']
