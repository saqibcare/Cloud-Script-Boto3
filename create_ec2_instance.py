#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')#, region_name='us-east-1'/*)
#key_pair = ec2.KeyPair('saqib')
instance = ec2.create_instances(
    ImageId='ami-a0cfeed8',
    MinCount=1,
    MaxCount=1,
    KeyName='saqib',
    InstanceType='t2.micro')
print(instance[0].id)