import boto3, json, pprint


ec2_cl = boto3.client('ec2')
ec2_re = boto3.resource('ec2')

instances = ec2_re.instances.all()

#resource
for instance in instances:
    print(f"resource: {instance.id}, {instance.state['Name']}")
    print('--------------------')
    
#client
for each in ec2_cl.describe_instances()['Reservations']:
    for instance in each['Instances']:
        print(f"client: {instance['InstanceId']}, {instance['State']['Name']}")
    break