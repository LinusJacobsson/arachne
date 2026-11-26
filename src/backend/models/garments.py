from pydantic import BaseModel, Field
from datetime import datetime

class Garment(BaseModel):
    id: str = Field(..., examples=["gmt_123"])
    owner_id: str = Field(..., examples=["usr_123"])
    category: str = Field(..., examples=["Shirt", "Dress"])
    color: str = Field(..., examples=["Green", "Red"])
    brand: str = Field(..., examples=["Suit Supply", "Prada"])
    size: str = Field(..., examples=["M", "L"])
    status: str = Field(..., examples=["Available", "Torn"])
    created_by: str = Field(..., examples=["usr_123"])
    created_at: datetime = Field(...)
    updated_by: datetime = Field(...)

class CreateGarmentRequest(BaseModel):
    owner_id: str = Field(...)
    category: str | None = Field(...)
    color: str | None = Field(...)
    brand: str | None = Field(...)
    size: str | None = Field(...)
    status: str | None = Field(...)

class GarmentResponse(BaseModel):
    id: str = Field(...)
    owner_id: str = Field(...)
    category: str | None = Field(...)
    color: str | None = Field(...)
    brand: str | None = Field(...)
    size: str | None = Field(...)
    status: str | None = Field(...)
