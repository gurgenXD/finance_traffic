from datetime import datetime

import sqlalchemy as sa

from app.adapters.storage.db.base_model import BaseModel


class Callback(BaseModel):
    """Обратные звонки."""

    __tablename__ = "callbacks"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(length=100), nullable=False)
    phone: str = sa.Column(sa.String(length=20), nullable=False)
    message: str = sa.Column(sa.Text(), nullable=True)
    created: datetime = sa.Column(sa.DateTime(), nullable=False, default=datetime.now)
    answered: bool = sa.Column(sa.Boolean(), default=False)
    call_back_time: datetime = sa.Column(sa.DateTime(), nullable=True, default=None)
