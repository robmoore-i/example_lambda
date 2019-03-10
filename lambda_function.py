import json

def lambda_handler(event, context):
    #n = extract_n(event)
    query_string_params = event.get("queryStringParameters", {"n": 5})
    n = extract_n(query_string_params)
    n_squared = n * n

    response_body = {"n": n, "n_squared": n_squared}
    return {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }

def extract_n(query_string_params):
    if not "n" in query_string_params:
        return 5
    else:
        return int(query_string_params.get("n", 5))
