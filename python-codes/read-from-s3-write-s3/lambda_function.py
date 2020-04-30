import csv
import os
import tempfile
import decimal
import boto3
'''
Debo habilitar primero una sesion con unas credenciales que tenga acceso para
el uso de s3, dynamodb
'''
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Files')
s3 = boto3.client('s3')


def lambda_handler(event, context):

    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        with tempfile.TemporaryDirectory() as tmpdir:
            download_path = os.path.join(tmpdir, key)
            s3.download_file(source_bucket, key, download_path)
            items = read_csv(download_path)

            with table.batch_writer() as batch:
                for item in items:
                    batch.put_item(Item=item)


def read_csv(download_path):
    items = []
    with open(download_path) as csv_file:
        reader = csv.DictReader(download_path, parse_float = decimal.Decimal)

