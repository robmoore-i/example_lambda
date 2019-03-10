from assertpy import assert_that

from lambda_function import *

def test_with(n):
  event = {"queryStringParameters": {"n": n}}
  expected_response_body = {"n": n, "n_squared": n * n}
  expected_response = {"statusCode": 200, "body": json.dumps(expected_response_body)}
  assert_that(lambda_handler(event, {})).is_equal_to(expected_response)

def test_that_n_defaults_to_5():
  event = {"queryStringParameters": {"somethingElse": None}}
  expected_response_body = {"n": 5, "n_squared": 25}
  expected_response = {"statusCode": 200, "body": json.dumps(expected_response_body)}
  assert_that(lambda_handler(event, {})).is_equal_to(expected_response)

def test_that_n_defaults_to_5_with_no_query_params_at_all():
  event = {"queryStringParameters": None}
  expected_response_body = {"n": 5, "n_squared": 25}
  expected_response = {"statusCode": 200, "body": json.dumps(expected_response_body)}
  assert_that(lambda_handler(event, {})).is_equal_to(expected_response)

test_with(7)
test_that_n_defaults_to_5()
test_that_n_defaults_to_5_with_no_query_params_at_all()

print("Unit tests passed")
