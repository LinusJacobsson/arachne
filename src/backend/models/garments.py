from pydantic import BaseModel, Field

class Garment(BaseModel):
    id: str = Field(..., examples=["gmt_123"])
    owner_id: str = Field(..., examples=["usr_123"])
    category: str = Field(..., examples=["Shirt", "Dress"])
    color: str = Field(..., examples=["Green", "Red"])
    brand: str = Field(..., examples=["Suit Supply", "Prada"])
    size: str = Field(..., examples=["M", "L"])
    status: str = Field(..., examples=["Available", "Torn"])


