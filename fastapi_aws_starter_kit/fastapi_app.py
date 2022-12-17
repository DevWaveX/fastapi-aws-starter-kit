from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_aws_starter_kit.routers.health_check_api import router as hc_router
from fastapi_aws_starter_kit.config import PROJECT_NAME, API_VERSION

# Declare the application
app = FastAPI(title=PROJECT_NAME, debug=False, version=API_VERSION)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path="/health", description="Health check")
def health_check():
    return {"status": "OK"}


app.include_router(hc_router)
