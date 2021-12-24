dbimport boto3
import json
import time
import datetime

personalize_events = boto3.client('personalize-events')

def lambda_handler(event, context):
     
     user_id = event['user_id']
     item_id = event['item_id']
     rating = event['rating']
     
     data = personalize_events.put_events(
        trackingId = '15633659-f3fa-4844-9ae7-774cfd9ea048',  
        userId = 'user_id',  
        sessionId = 'session_id',
        eventList = [{
            'sentAt': datetime.datetime.now().timestamp(),  
            'eventType': 'Rating',  
            'properties': json.dumps({
                'itemId': 'item_id',  
                'eventValue': float('rating')  
            })
        }]
    )
