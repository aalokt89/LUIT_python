import json
from datetime import datetime
import uuid
import boto3

# store api routes
GET_DATETIME = "/datetime"
GET_UUID = "/random-uuid"


def lambda_handler(event, context):
    apiEvent = event['rawPath']
    sqs = boto3.client('sqs')

    try:
        if apiEvent == GET_DATETIME:
            currentDateTime = datetime.strftime(
                datetime.now(), "%d/%m/%Y, %H:%M:%S")
            message = f"Current time: {currentDateTime}."
            print(message)

            return currentDateTime

        elif apiEvent == GET_UUID:
            randUUID = str(uuid.uuid4())
            message = f"Random uuid: {randUUID}."
            print(message)

            return randUUID

    except Exception as e:
        print(e)
