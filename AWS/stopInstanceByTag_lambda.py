import boto3
import json
import pprint

ec2 = boto3.client('ec2', region_name='us-east-1')


def lambda_handler():
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
    instances = ec2.describe_instances(Filters=ec2Filters)

    # get filtered instance ids and add them to runningInstances
    for each in instances['Reservations']:
        for instance in each['Instances']:
            filteredInstances.append(instance['InstanceId'])

    if len(filteredInstances) > 0:
        ec2.stop_instances(InstanceIds=filteredInstances)
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
