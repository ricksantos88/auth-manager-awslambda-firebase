import boto3

def get_credential(parameter: str):
    ssm = boto3.client('ssm')
    response = ssm.get_parameter(Name=parameter)
    firebase_client = response['Parameter']['Value']
    return firebase_client