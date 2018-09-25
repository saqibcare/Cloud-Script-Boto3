import boto3
s3client = boto3.resource('s3')
s3client = s3client.Bucket('django-balti')
response = s3client.create(
    ACL='public-read-write',  # 'private'|'public-read'|'public-read-write'|'authenticated-read'
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    },
    # GrantFullControl='string',
    # GrantRead='string',
    # GrantReadACP='string',
    # GrantWrite='string',
    # GrantWriteACP='string'
)
