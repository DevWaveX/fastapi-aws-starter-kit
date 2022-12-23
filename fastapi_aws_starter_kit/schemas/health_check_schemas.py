from pydantic import BaseModel


class HealthCheckResponseSchema(BaseModel):
    """
    Health check response.
    """

    status: str
