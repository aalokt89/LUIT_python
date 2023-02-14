import boto3
from pprint import pprint
import time

ec2 = boto3.resource('ec2')


def getInstanceByTag(tagKey, tagValue):
    instanceList = []
    response = ec2.instances.filter(
        Filters=[{
            'Name': 'tag:'+tagKey,
            'Values': [tagValue]
        }]
    )

    for instance in response:
        instanceList.append(instance)

    return instanceList


def stopInstance(tagKey, tagValue):
    instances = getInstanceByTag(tagKey, tagValue)

    for instance in instances:
        if instance.state['Name'] == 'running':
            ec2.instances.filter(InstanceIds=[instance.id]).stop()

            # need to fix
            pprint(
                f"instanceId: {instance.id}, 'InstanceState: {instance.instance.state}")


stopInstance(tagKey='Environment', tagValue='Dev')
