from fastapi import APIRouter
from fastapi_aws_starter_kit.schemas.health_check_schemas import (
    HealthCheckResponseSchema,
)

router = APIRouter(tags=["Health Check"], prefix="/health")


@router.get(
    path="/", description="Health check", response_model=HealthCheckResponseSchema
)
def health_check():
    return {"status": "OK"}
