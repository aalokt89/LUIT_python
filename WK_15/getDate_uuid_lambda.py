import json
from datetime import datetime
import uuid
import os
import boto3

# set env variables
DATETIME = os.environ['GET_DATETIME']
UUID = os.environ['GET_UUID']
queue = os.environ['QUEUE']


def lambda_handler(event, context):
    apiEvent = event['rawPath']
    sqs = boto3.resource('sqs')
    myQueue = sqs.Queue(queue)

    try:
        if apiEvent == DATETIME:
            currentDateTime = datetime.strftime(
                datetime.now(), "%m-%d-%Y, %H:%M:%S")
            message = f"current_time: {currentDateTime}"
            print(message)

        elif apiEvent == UUID:
            randUUID = str(uuid.uuid4())
            message = f"uuid: {randUUID}"
            print(message)

        response = myQueue.send_message(
            MessageBody=message
        )
        print(f"MessageID: '{response['MessageId']}' sent to queue.")

        return json.dumps(message)

    except Exception as e:
        print(e)
