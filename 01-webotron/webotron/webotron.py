import boto3
import click

session = boto3.Session(profile_name="pythonAutomation")
s3 = session.resource('s3')


@click.command("list-buckets")
def list_buckets():
    "List all S3 buckets"
    for b in s3.buckets.all():
        print(b)


if __name__ == "__main__":
    list_buckets()

