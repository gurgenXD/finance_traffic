from pydantic import BaseModel
from typing import Optional


class AnalysisSchema(BaseModel):
    """Схема анализа."""

    name: str
    preparation: Optional[str]
    period: str
    is_active: bool

    class Config:
        orm_mode = True
