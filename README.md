# AWS-TagEC2Lambda
This Python code is an AWS Lambda function that automatically tags EC2 instances when they are created. 

The function extracts metadata from an AWS CloudTrail event and uses it to add tags to the new EC2 instance. 

These tags include the AWS account ID, the user who initiated the instance creation, and the user's principal ID.

# How It Works
- When an EC2 instance is launched, a CloudTrail event is triggered.
- The Lambda function is invoked with the event details.
- The function processes the event to extract:
- The AWS account ID (account_number).
- The user identity and their principal ID (principal_id).
- The username (user_name).
- The ID of the new EC2 instance (instance_id).
- The function uses the boto3 EC2 client to create tags for the instance with the extracted metadata.

# Functionality
AWS Lambda Handler (handler):
### Inputs:
- event: A JSON representing the CloudTrail event. It contains details about the EC2 instance creation and the identity of the user who triggered it.
- context: AWS Lambda context object (not used in this function).
### Key Operations:
- Extracts the AWS account ID (account_number) from the event.
- Retrieves user identity details (user_identity) and extracts the principalId.
- Extracts the username (user_name) from the principalId using the extract_username function.
- Retrieves the ID of the newly created EC2 instance (instance_id).
- Creates tags for the EC2 instance using the boto3 EC2 client.
### Tagging the Instance:
- Tags added to the instance:
    - AccountID: The AWS account ID where the event occurred.
    - CreatedBy: The username of the individual who initiated the instance creation.
    - PrincipalID: The principal ID of the user or role responsible for the action.

### Helper Function (extract_username):
- Parses the principalId (e.g., AROA47CR3DMIPEE3JPECV:javanocollins.aws) to extract the username part (e.g., javanocollins.aws).
- Returns None if the principalId does not contain a colon (:).