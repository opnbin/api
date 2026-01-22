from pydantic import BaseModel
from typing import Optional

class PasteCreate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    language: str
    content: str

class PasteUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    content: Optional[str] = None

class PasteDelete(BaseModel):
    ids: list[str]

class PasteResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    language: str
    content: str
    created_at: str
    updated_at: str

class PasteListResponse(BaseModel):
    pastes: list[PasteResponse]
    page: int
    limit: int
    total: int
