from datetime import date

import sqlalchemy as sa

from app.adapters.storage.db.base_model import BaseModel


class User(BaseModel):
    """Пользователи."""

    __tablename__ = "users"

    id: int = sa.Column(sa.Integer, primary_key=True)
    username: str = sa.Column(sa.String(64), unique=True)
    email: str = sa.Column(sa.String(64), unique=True)
    password: str = sa.Column(sa.String(32), nullable=False)
    created: date = sa.Column(sa.Date(), nullable=False, default=date.today)
    is_active: bool = sa.Column(sa.Boolean(), default=False)
