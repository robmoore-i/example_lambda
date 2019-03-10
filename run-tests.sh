if [[ ! -f "endpoint" ]]
then
  echo "Create a file called 'endpoint' containing the origin of your lambda's invocation endpoint."
  echo "There is an example in 'endpoint.example'."
  exit 1
fi

PYTHONPATH=$PYTHONPATH:. python3 test/unit.py
endpoint=`cat endpoint` python3 test/poke.py
