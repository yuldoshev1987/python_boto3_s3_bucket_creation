import logging
import boto3
from botocore.exceptions import ClientError
class S3Service:
    @staticmethod
    def create_bucket(bucket_name, region=None):
        """Create an S3 bucket in a specified region

        If a region is not specified, the bucket is created in the S3 default
        region (us-east-1).

        :param bucket_name: Bucket to create
        :param region: String region to create bucket in, e.g., 'us-west-2'
        :return: True if bucket created, else False
        """

        # Create bucket
        try:
            if region is None:
                s3_client = boto3.client('s3')
                s3_client.create_bucket(Bucket=bucket_name)
            else:
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False
        return True
    @staticmethod
    def get_list_of_Bucket():
        #List of s3 buckets
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        # Output the bucket names
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(bucket["Name"])

    @staticmethod
    def upload_file(filePath,bucketName,fileName):
        flag=False
        s3 = boto3.resource('s3')
        respose=s3.meta.client.upload_file(filePath, bucketName, fileName)
        print('*'*50,respose)
        my_bucket = s3.Bucket(bucketName)
        for file in my_bucket.objects.all():
            if file.key==fileName:
                flag=True
                break
        if flag==True:
            print(fileName,'uploaded successfully ')
        else:
            print(fileName, 'uploaded successfully ')
s=S3Service()
s.upload_file('HelloWorld.txt','ziyotek-cloudmasters','HelloWorld.txt')