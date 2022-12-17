install-serverless:
	npm install

install-python-requirements:
	pip install poetry
	poetry install

black:
	black fastapi_aws_starter_kit

flake8:
	flake8 fastapi_aws_starter_kit

serverless-deploy:
	sls deploy

serve:
	sls offline