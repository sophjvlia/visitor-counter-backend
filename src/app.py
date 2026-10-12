import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')

table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def update_counter(event, context):
    try:
        query_params = event.get('queryStringParameters') or {}
        page_id = query_params.get('page', 'home')

        response = table.update_item(
            Key={'page_id': page_id},
            UpdateExpression='ADD visitor_count :incr',
            ExpressionAttributeValues={':incr': 1},
            ReturnValues='UPDATED_NEW'
        )
        
        current_count = int(response['Attributes']['visitor_count'])
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,GET'
            },
            'body': json.dumps({'page': page_id, 'count': current_count})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error updating counter: {str(e)}'
        }