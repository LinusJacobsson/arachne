from pydantic import BaseModel, Field
from garments import Garment
from datetime import datetime

class Outfit(BaseModel):
    id: str = Field(..., examples=["out_123"])
    owner_id: str = Field(..., examples=["usr_123"])
    name: str = Field(..., min_length=1, examples=["Blue suit + white shirt"])
    garments: list[Garment] = Field(..., min_length=1, examples=[...])
    created_by: str = Field(..., examples=["usr_123"])
    created_at: datetime = Field(...,)
    updated_at: datetime = Field(...,)

class CreateOutfitRequest(BaseModel):
    owner_id: str = Field(...)
    name: str = Field(...)
    garments: list[Garment] = Field(...)


class OutfitResponse(BaseModel):
    id: str = Field(...)
    owner_id: str = Field(...)
    name: str = Field(...)
    garments: list[Garment] = Field(...)