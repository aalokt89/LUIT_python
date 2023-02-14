import boto3
from pprint import pprint
import time


def stopInstance():
    ec2 = boto3.resource('ec2')

    instances = getInstanceByTag('Environment', 'Prod')

    for instance in instances:
        if instance.state['Name'] == 'running':
            ec2.instances.filter(InstanceIds=[instance.id]).stop()

            # need to fix
            pprint(instance.state)


def getInstanceByTag(tagKey, value):
    ec2 = boto3.resource('ec2')
    instanceList = []

    response = ec2.instances.filter(
        Filters=[{
            'Name': 'tag:'+tagKey,
            'Values': [value]
        }]
    )

    for instance in response:
        instanceList.append(instance)

    return instanceList


stopInstance()
