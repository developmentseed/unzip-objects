#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk.cdk_stack import CdkStack


stack_name = os.getenv('STACK_NAME')
aws_region = os.getenv('AWS_REGION')
bucket_name = os.getenv('EXISTING_BUCKET')

app = cdk.App()

CdkStack(
    app,
    stack_name,
    env={'region': aws_region},
    bucket_name=bucket_name
)

app.synth()
