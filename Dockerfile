FROM public.ecr.aws/lambda/python:3.12

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy function code
COPY . .

# Command to run your Lambda function
CMD ["lambda_function.lambda_handler"]