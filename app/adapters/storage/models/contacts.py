import sqlalchemy as sa

from app.adapters.storage.db.base_model import BaseModel


class Contact(BaseModel):
    """Контакты."""

    __tablename__ = "contacts"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    city: str = sa.Column(sa.String(length=30), nullable=False)
    description: str = sa.Column(sa.String(length=100), nullable=False)
    address: str = sa.Column(sa.String(length=100), nullable=False)
    work_time: str = sa.Column(sa.String(length=100), nullable=False)
    phone: str = sa.Column(sa.String(length=20), nullable=False)
    email: str = sa.Column(sa.String(length=30), nullable=False)
    map_code: str = sa.Column(sa.String(length=500), nullable=True)
