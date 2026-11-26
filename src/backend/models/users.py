from pydantic import BaseModel, Field

class User(BaseModel):
    id: str = Field(..., examples=["usr_123"])
    name: str = Field(..., examples=["Linus"])
    avatar_id: str = Field(..., examples=["avt_123"])


