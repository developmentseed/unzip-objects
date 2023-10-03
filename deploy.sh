#!/bin/bash

# Set AWS_PROFILE
export AWS_PROFILE="my-aws-profile"

# Set the environment variables
export EXISTING_BUCKET="jaxaalos2"
export STACK_NAME="NewStack"
export AWS_REGION="my-aws-region"

# Deploy the CDK stack
cdk deploy

# Check if the CDK deployment was successful
if [ $? -eq 0 ]; then
    # Run the Boto3 script
    python3 add_s3_event_notification.py $EXISTING_BUCKET $(aws cloudformation describe-stacks --stack-name $STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`LambdaFunctionArn`].OutputValue' --output text)
fi
