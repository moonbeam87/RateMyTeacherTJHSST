import boto3
from boto3.dynamodb.conditions import Key, Attr

def get_ratings(name):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Instantiate a table resource object without actually
    # creating a DynamoDB table. Note that the attributes of this table
    # are lazy-loaded: a request is not made nor are the attribute
    # values populated until the attributes
    # on the table resource are accessed or its load() method is called.
    table = dynamodb.Table('teachers')

    response = table.query(
        KeyConditionExpression=Key('last_name').eq(name)
    )
    items = response['Items']
    print(items)

def get_average_rating(name):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Instantiate a table resource object without actually
    # creating a DynamoDB table. Note that the attributes of this table
    # are lazy-loaded: a request is not made nor are the attribute
    # values populated until the attributes
    # on the table resource are accessed or its load() method is called.
    table = dynamodb.Table('teachers')

    response = table.query(
        KeyConditionExpression=Key('last_name').eq(name)
    )
    items = response['Items']
    nums = []
    for item in items:
        num = item['rating']
        num = int(num)
        nums.append(num)
    average = sum(nums)/len(nums)
    print(average)
    return average



get_ratings('Choi')
print("______________________")
get_average_rating("Choi")