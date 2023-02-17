import boto3
import json
import pprint

ec2 = boto3.resource('ec2', region_name='us-east-1')


def lambda_handler(event, context):
    filteredInstances = []

    successMessage = f"Successfully stopped {len(filteredInstances)} instances."
    errorMessage = "Error: There are no running instances with the selected filters."

    ec2Filters = [
        {
            'Name': 'tag:Environment',
            'Values': ['Dev']
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }]

    # get instances by tag and 'running' state
    instances = ec2.instances.filter(Filters=ec2Filters)

    # get filtered instance ids and add them to runningInstances
    for instance in instances:
        filteredInstances.append(instance.id)

    if len(filteredInstances) > 0:
        ec2.instances.filter(InstanceIds=filteredInstances).stop()
        print(successMessage)
        return {
            "statusCode": 200,
            "body": json.dumps(successMessage)
        }
    else:
        print(errorMessage)
        return {
            "statusCode": 100,
            "body": json.dumps(errorMessage)
        }


lambda_handler(event=None, context=None)
