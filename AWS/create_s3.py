import boto3

s3_client = boto3.client("s3")

# s3_client.create_bucket(
#     Bucket = "atrivedi89-bucket-1"
    
#     )

response = s3_client.list_buckets()

for bucket in response['Buckets']:
    print(bucket)