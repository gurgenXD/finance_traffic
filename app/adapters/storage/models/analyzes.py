import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.adapters.storage.db.base_model import BaseModel

analyzes_types_analyzes_table = sa.Table(
    "analyzes_types_analyzes",
    BaseModel.metadata,
    sa.Column("analysis_type_id", sa.ForeignKey("analyzes_types.id"), primary_key=True),
    sa.Column("analysis_id", sa.ForeignKey("analyzes.id"), primary_key=True),
)


class AnalysisType(BaseModel):
    """Тип анализов."""

    __tablename__ = "analyzes_types"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(length=30), nullable=False)
    description: str = sa.Column(sa.Text())

    analyzes: "Analysis" = relationship(
        "Analysis",
        secondary=analyzes_types_analyzes_table,
        back_populates="analyzes_types",
    )

    def __str__(self) -> str:
        return self.name


class Analysis(BaseModel):
    """Анализы."""

    __tablename__ = "analyzes"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(length=30), nullable=False)
    preparation: str = sa.Column(sa.Text())
    period: str = sa.Column(sa.String(length=30), nullable=False)
    is_active: bool = sa.Column(sa.Boolean(), default=False)

    analyzes_types: "AnalysisType" = relationship(
        "AnalysisType",
        secondary=analyzes_types_analyzes_table,
        back_populates="analyzes",
    )

    def __str__(self) -> str:
        return self.name
