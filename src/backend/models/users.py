from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    id: str = Field(..., examples=["usr_123"])
    name: str = Field(..., examples=["Linus"])
    avatar_id: str = Field(..., examples=["avt_123"])
    created_by: str = Field(..., examples=["usr_123"])
    created_at: datetime = Field(...,)
    updated_at: datetime = Field(...,)

