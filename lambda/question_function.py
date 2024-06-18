import json

def lambda_handler(event, context):
    user_message = event['input']['message']
    # Process user message and determine the next response
    if "help" in user_message.lower():
        response = 'Sure, I can help you. What do you need assistance with?'
    else:
        response = 'Can you please clarify your request?'
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
