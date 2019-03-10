mkdir -p build
timestamp=`date -Iseconds | cut -c1-19`
archive_zip_file="build/square-number-${timestamp}.zip"
zip $archive_zip_file "lambda_function.py" >> /dev/null
aws lambda update-function-code --function-name square_number --zip-file fileb://$archive_zip_file  --publish
