import json
import fsspec
import zipfile
import os
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # AWS S3 Event Source Bucket Name
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    zip_key = event['Records'][0]['s3']['object']['key']

    # Extract the prefix from the zip key
    dest_prefix = zip_key.replace('.zip', '/')

    fs = fsspec.filesystem('s3', anon=False)
    try:
        with fs.open(f'{bucket_name}/{zip_key}', 'rb') as f:
            logger.info(f'Unzipping {zip_key}')
            with zipfile.ZipFile(f) as zf:
                for name in zf.namelist():
                    logger.info(f'Writing {name}')
                    dest_key = os.path.join(dest_prefix, name)
                    with fs.open(f'{bucket_name}/{dest_key}', 'wb') as dest_f:
                        dest_f.write(zf.read(name))
        logger.info('Files unzipped successfully!')
        return {
            'statusCode': 200,
            'body': json.dumps('Files unzipped successfully!')
        }
    except Exception as e:
        logger.error("Error occurred: ", exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps(e)
        }
