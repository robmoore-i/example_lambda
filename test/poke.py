import os
import requests
from assertpy import assert_that

endpoint = os.environ["endpoint"]

def test_with(n):
  response = requests.get(endpoint + "?n=" + str(n))
  assert_that(response.status_code).is_equal_to(200)
  json = response.json()
  assert_that(json).is_equal_to({"n": n, "n_squared": n * n})

test_with(5)

print("All passed")
