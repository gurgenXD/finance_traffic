import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.adapters.storage.db.base_model import BaseModel


class ServiceType(BaseModel):
    """Тип услуг."""

    __tablename__ = "services_types"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(length=30), nullable=False)
    on_main: bool = sa.Column(sa.Boolean(), default=False)

    services: "ServiceType" = relationship("Service", back_populates="service_type")

    def __str__(self) -> str:
        return self.name


class Service(BaseModel):
    """Услуги."""

    __tablename__ = "services"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    service_type_id: int = sa.Column(
        sa.BigInteger(), sa.ForeignKey("services_types.id")
    )
    name: str = sa.Column(sa.String(length=30), nullable=False)
    is_active: bool = sa.Column(sa.Boolean(), default=False)
    on_main: bool = sa.Column(sa.Boolean(), default=False)

    service_type: "Service" = relationship("ServiceType", back_populates="services")

    def __str__(self) -> str:
        return self.name
