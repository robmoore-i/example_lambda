import json

def lambda_handler(event, context):
    event_string = "event: " + str(event)
    query_string_params = "event['queryStringParameters']: " + str(event["queryStringParameters"])
    n = int(event["queryStringParameters"]["n"])
    n_squared = n * n
    response_body = {"n": n, "n_squared": n_squared}
    return {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }
