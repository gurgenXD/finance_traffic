from datetime import datetime

import sqlalchemy as sa

from app.adapters.storage.db.base_model import BaseModel


class News(BaseModel):
    """Новости."""

    __tablename__ = "news"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    title: str = sa.Column(sa.String(length=50), nullable=False)
    preview: str = sa.Column(sa.String(length=50), nullable=False)
    created: datetime = sa.Column(sa.DateTime(), nullable=False, default=datetime.now)
    description: str = sa.Column(sa.String(length=500), nullable=False)
    photo: str = sa.Column(sa.String(length=50), nullable=False)
    is_active: bool = sa.Column(sa.Boolean(), default=False)
