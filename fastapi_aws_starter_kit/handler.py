from mangum import Mangum
from fastapi_aws_starter_kit.fastapi_app import app

handler = Mangum(app=app)
