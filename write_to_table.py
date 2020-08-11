import boto3

# Get the service resource.
dynamodb = boto3.resource("dynamodb")

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table("teachers")


def write(subject, last_name, rating, description):
    table.put_item(
        Item={
            "subject": subject,
            "last_name": last_name,
            "rating": rating,
            "description": description,
        }
    )
    s = "Rating Uploaded!"
    return s
