install-serverless:
	npm install

install-python-requirements:
	pip install poetry
	poetry install

black:
	poetry run black fastapi_aws_starter_kit

flake8:
	poetry run flake8 fastapi_aws_starter_kit

deploy:
	npx sls deploy

serve:
	npx sls offline --noPrependStageInUrl