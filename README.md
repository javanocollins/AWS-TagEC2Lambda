# AWS-TagEC2Lambda
This Python code is an AWS Lambda function that automatically tags EC2 instances when they are created. 

The function extracts metadata from an AWS CloudTrail event and uses it to add tags to the new EC2 instance. 

These tags include the AWS account ID, the user who initiated the instance creation, and the user's principal ID.
