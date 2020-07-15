
from getcounterscript import *

import unittest  
import boto3
import botocore
from moto import mock_dynamodb2

@mock_dynamodb2
class TestDynamoDB(unittest.TestCase):


    def setUp(self):
        #First check if table already exists. If it already exists that mean we connected to real AWS env and not mock.
        try:
             dynamodb = boto3.resource(
                "dynamodb")
             dynamodb.meta.client.describe_table(TableName='visitor_counter')
        except botocore.exceptions.ClientError:
            pass
        else:
            err = "{Table} should not exist.".format(Table='visitor_counter')
            raise EnvironmentError(err)
        
        table_name = 'visitor_counter'
        dynamodb = boto3.resource('dynamodb', 'us-east-2')

        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'pagename',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'pagename',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    def event():
        pass

    def context():
        pass
       
    def test_getCounter(self):
        value1 = getCounter(self.event, self.context);
        print(value1)
        self.assertTrue(value1 > 0);
        self.assertEqual(value1, 1);

       


if __name__ == '__main__':
    
    unittest.main()

