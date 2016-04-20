# lambda-deploy

Simple script to deploy Python code to AWS Lambda.

Automatically zips the current directory and the specified module directory (hopefully you used a virtualenv!), then uploads it to the specified lambda function.

## Installation
1. Install and configure the [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) with your account's login credentials
2. Set up lambda-deploy virtualenv, then `pip install -r requirements.txt`

## Usage
1. In `deploy.py`, change `MODULE_DIR` and `LAMBDA_FUNCTION_NAME` to correspond to your Python module directory (probably in `~/.virtualenvs` somewhere) and the AWS Lambda function's name, respectively
2. Navigate to the deployment directory
3. `python /path/to/deploy.py`
