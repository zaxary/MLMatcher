import boto3
s3 = boto3.resource('s3')
print(s3.buckets.all())
s3.bucketsCollection(s3.ServiceResource(), s3.Bucket)
for bucket in s3.buckets.all():
    print(bucket)
