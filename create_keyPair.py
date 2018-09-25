import boto3

ec2 = boto3.resource('ec2')
outfile = open('saqib2-key.pem', 'w')
keypair = ec2.create_key_pair(KeyName='saqib2-key')
keyPairOut = str(keypair.key_material)
outfile.write(keyPairOut)


instance = ec2.create_instances(
    ImageId='ami-a0cfeed8',
    MinCount=1,
    MaxCount=1,
    KeyName="saqib2-key",
    InstanceType='t2.micro')
print(instance[0].id)