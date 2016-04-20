import os
import zipfile

import boto3

BUILD_DIR = 'build'

DEPLOYMENT_ZIP = 'deploy.zip'

ZIP_PATH = os.path.join(BUILD_DIR, DEPLOYMENT_ZIP)

MODULE_DIR = 'C:\\Users\\nvcar_000\\.virtualenvs\\fb-roulette\\lib\\site-packages'

LAMBDA_FUNCTION_NAME = 'fbMessagesWebhook'


def remove_build_path_in_place(dirs):
	for i, dir_name in enumerate(dirs):
		if dir_name == BUILD_DIR:
			del dirs[i]
			return

def zip_dir(path, ziph, remove_build_path):
	# ziph is zipfile handle
	for root, dirs, files in os.walk(path, remove_build_path):
		if remove_build_path:
			remove_build_path_in_place(dirs)

		for file in files:
			file_path = os.path.join(root, file)
			local_path = os.path.relpath(file_path, path)
			if os.path.dirname(local_path) != BUILD_DIR:
				ziph.write(file_path, local_path)

def make_deployment_zip(directory, module_dir=MODULE_DIR):
	if not os.path.exists(BUILD_DIR):
		os.makedirs(BUILD_DIR)

	zipf = zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED)
	zip_dir(directory, zipf, True)
	zip_dir(module_dir, zipf, False)
	zipf.close()

def deploy_to_lambda(zip_bytes):
	client = boto3.client('lambda')

	response = client.update_function_code(
		FunctionName=LAMBDA_FUNCTION_NAME,
		ZipFile=zip_bytes,
		Publish=True
	)

	return response


if __name__ == '__main__':
	print 'Creating deployment zip'
	buf = make_deployment_zip(os.getcwd())

	print 'Updating lambda function'
	with open(ZIP_PATH, 'rb') as f:
		print(deploy_to_lambda(f.read()))
	print 'Done'
