from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PromotionSchema(BaseModel):
    """Схема акции."""

    sale: str
    title: str
    description: str
    photo: Optional[str]
    services: str
    date_start: datetime
    date_end: datetime
    url: str
    is_active: bool
    on_main: bool

    class Config:
        orm_mode = True
