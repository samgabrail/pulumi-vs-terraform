import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket("env0-pulumi-example",
                   bucket="env0-pulumi-example",
                   acl="private",
                   tags={
                       "Name": "env0-pulumi-example-bucket",
                       "Environment": "Production",
                   })

ownership = s3.BucketOwnershipControls(
    "example",
    bucket=bucket.id,
    rule={"object_ownership": "BucketOwnerPreferred"}
)

# Export the name of the bucket
pulumi.export("bucketName", bucket.id)
