import boto3

# Get the service resource.
dynamodb = boto3.resource("dynamodb")

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName="teachers",
    KeySchema=[
        {"AttributeName": "last_name", "KeyType": "HASH"},
        {"AttributeName": "rating", "KeyType": "RANGE"},
    ],
    AttributeDefinitions=[
        {"AttributeName": "last_name", "AttributeType": "S"},
        {"AttributeName": "rating", "AttributeType": "S"},
    ],
    ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
)

# Wait until the table exists.
table.meta.client.get_waiter("table_exists").wait(TableName="teachers")
