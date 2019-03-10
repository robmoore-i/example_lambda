import json

def lambda_handler(event, context):
    is_in = "queryStringParameters" in event
    params = event["queryStringParameters"]
    if params is None:
      n = 5
    elif "n" not in params:
      n = 5
    else:
      n = 7

    n_squared = n * n

    response_body = {"n": n, "n_squared": n_squared}
    return {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }

