import boto3
from pprint import pprint
import time

ec2 = boto3.client('ec2', region_name='us-east-1')


def stopInstanceByTag(key, value):
    successList = []
    failList = []

    # get instances by tag and value
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:'+key,
                'Values': [value]
            }
        ]
    )

    # stop selected instances if state == running
    for each in response['Reservations']:
        for instance in each['Instances']:

            if instance['State']['Name'] == 'running':
                ec2.stop_instances(InstanceIds=[instance['InstanceId']])
                successList.append({
                    'instanceId': instance['InstanceId'],
                    'State': instance['State']['Name']
                })
            else:
                failList.append(instance['InstanceId'])

    # print out successfully stopped instances
    print("----------------------")
    print("The following instances have been stopped:")
    print(successList)
    print("----------------------")


stopInstanceByTag('Environment', 'Dev')
