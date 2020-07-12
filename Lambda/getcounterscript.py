import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def updateCounter():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('visitor_counter')
    response = table.update_item(
        Key={
            'pagename': 'homepage'
        },
        AttributeUpdates={
            'counter': {
                'Value': 1,
                'Action': 'ADD'
            }
            }
        )

def getCounter(event, context):
    updateCounter()
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('visitor_counter')
    response = table.get_item(
   Key={
      'pagename': 'homepage'
     }
    )
    item = response['Item']
    print(item)
    json_str =  json.dumps(item, cls=DecimalEncoder)

    #using json.loads will turn your data into a python dictionary
    resp_dict = json.loads(json_str)
    print (resp_dict.get('counter'))
    return resp_dict.get('counter')

if __name__ == "__main__":
    getCounter()





