import os
import requests
from assertpy import assert_that

endpoint = os.environ["endpoint"]

def test_with(n):
  response = requests.get(endpoint + "?n=" + str(n))
  assert_that(response.status_code).is_equal_to(200)
  json = response.json()
  assert_that(json).is_equal_to({"n": n, "n_squared": n * n})

def test_that_n_defaults_to_5():
  response = requests.get(endpoint)
  assert_that(response.status_code).is_equal_to(200)
  json = response.json()
  assert_that(json).is_equal_to({"n": 5, "n_squared": 25})

test_with(7)
test_that_n_defaults_to_5()

print("Integration tests passed")
