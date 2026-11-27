from datetime import datetime

from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(..., examples=["usr_123"])
    name: str = Field(..., examples=["Linus"])
    avatar_id: str = Field(..., examples=["avt_123"])
    created_by: str = Field(..., examples=["usr_123"])
    created_at: datetime = Field(
        ...,
    )
    updated_at: datetime = Field(
        ...,
    )


class CreateUserRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=30)
    avatar_id: str = Field(...)


class UserResponse(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    avatar_id: str = Field(...)
