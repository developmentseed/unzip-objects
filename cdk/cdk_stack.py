from constructs import Construct
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_iam as iam,
    CfnOutput, 
    Duration
)
from aws_cdk.aws_lambda_python_alpha import PythonFunction

class CdkStack(Stack):

    def __init__(self, scope: Construct, id: str, bucket_name: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Reference an existing S3 bucket
        bucket = s3.Bucket.from_bucket_attributes(
            self, "ExistingBucket", bucket_name=bucket_name
        )

        # Create a Lambda function
        lambda_function = PythonFunction(
            self, "UnzipFunction",
            entry="./cdk/lambda/",
            index="index.py",
            handler="lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_11,
            memory_size=2048,
            timeout=Duration.seconds(60)
        )
        CfnOutput(self, "LambdaFunctionArn", value=lambda_function.function_arn)

        # Grant the Lambda function read/write permissions on the bucket
        bucket.grant_read_write(lambda_function)

        lambda_function.add_permission(
            'AllowS3Invoke',
            principal=iam.ServicePrincipal('s3.amazonaws.com'),
            action='lambda:InvokeFunction',
            source_arn=bucket.bucket_arn
        )

        lambda_function.add_to_role_policy(iam.PolicyStatement(
            actions=[
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            resources=["arn:aws:logs:*:*:*"]
        ))
