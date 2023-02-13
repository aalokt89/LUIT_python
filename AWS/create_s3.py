import boto3

s3_client = boto3.client("s3")

#s3_client.create_bucket(Bucket="test_bucket_1_boto", CreateBucketConfiguration={'LocationConstraint':'us-east-1'})

response = s3_client.list_buckets()

print(response)