import json
import boto3
import os
import random

def lambda_handler(event, context):
    sqs_url = os.environ['sqs_url']
    sqs = boto3.client('sqs')
    
    response = sqs.send_message(
        QueueUrl= sqs_url,
        MessageBody= str(random.randint(0, 10)))
        
