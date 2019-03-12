## Example Python Lambda

### update-lambda.sh

Zips up the code in 'lambda_function.py', then uploads and publishes it to the python3.6 lambda I have called
'square_number'.

### run-tests.sh

Pokes the endpoint at the url stored in the file `endpoint`. I didn't really fancy having it on github. I think
it's really most sensible to use API keys.

### lambda_function.py

Squares a number which is in the query string and returns a response as json.

### test/poke.py

A tiny test script using the requests http(s) library and the assertpy library. It pokes the running endpoint and
verifies that it does the thing it's meant to.

### endpoint.example

Contains an example of the lambda invocation endpoint.
