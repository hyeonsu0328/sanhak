import json
import csv
import boto3

def lambda_handler(event, context):
    region = 'ap-northeast-2'
    record_list = []
    
    try:
        s3 = boto3.client('s3')
        
        dynamodb = boto3.client('dynamodb', region_name = region)
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        print('Bucket: ', bucket , ' Key: ', key)
        
        csv_file = s3.get_object(Bucket = bucket, Key = key)
        
        record_list = csv_file['Body'].read().decode('cp949').split('\n')
        csv_reader = csv.reader(record_list, delimiter=',', quotechar='"')
        
        for row in csv_reader:
            Song_id = row[0]
            Title = row[1]
            Artist = row[2]
            Genre = row[3]    
            LDA_Topic = row[4]
            URL = row[5]
            Album = row[6]
            Topic_num = row[7]
            TAG = row[8]
            
           
       
            add_to_db = dynamodb.put_item(
                TableName = 'Song_data_final',
                Item = {
                    'Song_id': {'S': str(Song_id)},
                    'Title': {'S': str(Title)},
                    'Artist': {'S': str(Artist)},
                    'Genre': {'S': str(Genre)},
                    'LDA_Topic': {'S': str(LDA_Topic)},
                    'URL': {'S': str(URL)},
                    'Album': {'S': str(Album)},
                    'Topic_num': {'S': str(Topic_num)},
                    'TAG' : {'S': str(TAG)}
                })
            print('1')
                
            print('success')
    except Exception as e:
        print(str(e))
        
    return {
        'statusCode': 200,
        'body': json.dumps('csv to dynamodb success')
    }
