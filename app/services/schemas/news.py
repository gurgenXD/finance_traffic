from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NewsSchema(BaseModel):
    """Схема контакта."""

    title: str
    preview: str
    created: datetime
    description: str
    photo: Optional[str]
    is_active: bool

    class Config:
        orm_mode = True
