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

    try:
        if apiEvent == DATETIME:
            currentDateTime = datetime.strftime(
                datetime.now(), "%d/%m/%Y, %H:%M:%S")
            message = f"Current time: {currentDateTime}."
            print(message)

        elif apiEvent == UUID:
            randUUID = str(uuid.uuid4())
            message = f"Random uuid: {randUUID}."
            print(message)

        response = queue.send_message(
            MessageBody=message
        )
        return response

    except Exception as e:
        print(e)
