import boto3

sqs = boto3.resource('sqs', region_name='us-east-1')


def createSQS(queueName):

    queue = sqs.create_queue(QueueName=queueName)
    queueURL = queue.url

    print(queueURL)


# createSQS('DateTime_UUID_sqs')

print(sqs.get_queue_by_name(QueueName='DateTime_UUID_sqs'))
