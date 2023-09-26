install-serverless:
	npm install

install-python-requirements:
	poetry install

black:
	poetry run black fastapi_aws_starter_kit

flake8:
	poetry run flake8 fastapi_aws_starter_kit

deploy:
	npx sls deploy

serve:
	npx sls offline

remove:
	npx sls remove
