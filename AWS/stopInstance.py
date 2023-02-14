import boto3
from pprint import pprint


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
        instanceList.append(instance.id)

    return instanceList


prodInstances = getInstanceByTag('Environment', 'Prod')

print(prodInstances)
