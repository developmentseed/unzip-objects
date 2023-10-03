import sys
import boto3

def main():
    # Get the command-line arguments
    bucket_name = sys.argv[1]
    lambda_function_arn = sys.argv[2]

    s3 = boto3.resource('s3', region_name='us-west-2')

    # Add the event notification configuration
    bucket_notification = s3.BucketNotification(bucket_name)
    bucket_notification.put(
        NotificationConfiguration={
            'LambdaFunctionConfigurations': [
                {
                    'LambdaFunctionArn': lambda_function_arn,
                    'Events': ['s3:ObjectCreated:*'],
                    'Filter': {
                        'Key': {
                            'FilterRules': [
                                {
                                    'Name': 'suffix',
                                    'Value': '.zip'
                                },
                            ]
                        }
                    }
                },
            ]
        }
    )

if __name__ == "__main__":
    main()
