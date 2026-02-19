import os
from fastapi import Header
from app.core.errors import InvalidAPIKeyError

def require_api_key(x_api_key: str | None = Header(default=None, alias = "X-API-KEY")):
    expected_api_key = os.getenv("API_KEY", "Administrator_API_KEY")
    if x_api_key != expected_api_key:
        raise InvalidAPIKeyError("Invalid API key provided.")