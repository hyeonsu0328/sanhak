import boto3
import csv
import io

s3 = boto3.client('s3')
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    csvio = io.StringIO()
    writer = csv.writer(csvio)
    writer.writerow(['id', 'name'])

    paginator = ec2.get_paginator('describe_security_groups').paginate()

    for page in paginator:
        for item in page['SecurityGroups']:
            identity = item['GroupId']
            name = item['GroupName']

            writer.writerow([identity, name])

    s3.put_object(Body=csvio.getvalue(), ContentType='text/csv', Bucket='<bucket>', Key='<filename.csv>') 
    csvio.close()
