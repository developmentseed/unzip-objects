# AWS Lambda Function to Unzip Files in S3
This repository contains an AWS Lambda function that unzips files in an S3 bucket.

## How the Function Works
When a zip file is uploaded to the S3 bucket, this Lambda function is triggered. It reads the zip file, extracts its contents, and writes the unzipped files back to the S3 bucket under the zip file's name.

For example, if a zip file under the S3 key `folder1/folder2/file.zip` is uploaded to the S3 bucket, the function will unzip the file and write the unzipped files to the S3 bucket under the key `folder1/folder2/file/`. The zip file itself is not deleted.

## What's Included
A lambda function that unzips files in place within an S3 bucket. The function is given permission to read and write to the S3 bucket, permission to write logs to CloudWatch, and permission to be invoked by an S3 event notification.

An S3 Event Notification on an existing S3 bucket that triggers the lambda function when a zip file (`.zip`) is uploaded to the bucket. 

## Setting Up the Environment
To deploy the function, you need to have the AWS CLI and AWS CDK installed. It is recommended to use a virtual environment to install the dependencies.

To upgrade your pip environment, run the following command:

```
$ python -m pip install --upgrade pip
```

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ python -m pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

## Deploy
Populate the `export` variables in `deploy.sh` with your own values and run the following command

```
$ ./deploy.sh
```

To add additional dependencies, for example other CDK libraries, just add
them to your requirements file and rerun the `pip install -r requirements.txt`
command.
