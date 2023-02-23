import boto3


def createSNS(topicName):
    sns = boto3.resource('sns', region_name='us-east-1')

    try:
        topic = sns.create_topic(Name=topicName)
        print(topic.arn)

    except Exception as e:
        print(e)


createSNS('dateTime-uuid-topic')
