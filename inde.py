import json
import boto3

ec2 = boto3.client('ec2')

def handler(event, context):
    account_number = event['account']

    user_identity = event['detail']['userIdentity']

    principal_id = user_identity['principalId']

    user_name = extract_username(principal_id)

    instance_id = instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']


    ec2.create_tags(
        Resources=[
            instance_id
        ],
        Tags=[
            {
                'Key': 'AccountID',
                'Value': account_number
            },
            {
                'Key': 'CreatedBy',
                'Value': user_name
            },
            {
                'Key': 'PrincipalID',
                'Value': principal_id
            }
        ]
    )

def extract_username(principal_id):
    """
    Extract the username from the principalId string.

    :param principal_id: str, the principalId in the format "RoleID:username"
    :return: str, the extracted username
    """
    if ":" in principal_id:
        return principal_id.split(":")[1]
    return None