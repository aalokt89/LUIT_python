import json
from datetime import datetime
import uuid
import boto3

# store api routes
GET_DATETIME = "/datetime"
GET_UUID = "/random-uuid"


def lambda_handler(event, context):
    apiEvent = event['rawPath']
    sqs = boto3.resource('sqs')

    myQueue = sqs.Queue(
        'https://sqs.us-east-1.amazonaws.com/054301730155/DateTime_UUID_sqs')

    try:
        if apiEvent == GET_DATETIME:
            currentDateTime = datetime.strftime(
                datetime.now(), "%d/%m/%Y, %H:%M:%S")
            message = f"Current time: {currentDateTime}."
            print(message)

        elif apiEvent == GET_UUID:
            randUUID = str(uuid.uuid4())
            message = f"Random uuid: {randUUID}."
            print(message)

        response = myQueue.send_message(
            MessageBody=message
        )
        return response

    except Exception as e:
        print(e)
