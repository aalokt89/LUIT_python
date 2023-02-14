import boto3
from pprint import pprint
import time

ec2 = boto3.resource('ec2')


def stopInstance():
    instances = getInstanceByTag('Environment', 'Prod')

    for instance in instances:
        if instance.state['Name'] == 'running':
            ec2.instances.filter(InstanceIds=[instance.id]).stop()

            # need to fix
            pprint(instance.state)


def getInstanceByTag(tagKey, value):
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
