from collections.abc import Callable
from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from app.adapters.storage.models import Analysis
from app.services.schemas.analyzes import AnalysisSchema
from app.services.exceptions import NotFoundError

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AnalyzesAdapter:
    """Адаптер для доступа к данным анализов."""

    def __init__(
        self, session_factory: Callable[[], AbstractAsyncContextManager["AsyncSession"]]
    ) -> None:
        self._session_factory = session_factory
        self._model = Analysis

    async def get_all(self, on_main: bool) -> list["AnalysisSchema"]:
        """Получить все активные анализы."""

        query = select(self._model).where(self._model.is_active.is_(True))

        if on_main:
            query = query.where(self._model.on_main.is_(True))

        async with self._session_factory() as session:
            rows = await session.execute(query)
            analyzes = [AnalysisSchema.from_orm(row) for row in rows.scalars()]

        return analyzes

    async def get(self, id: int) -> "AnalysisSchema":
        """Получить анализ."""

        query = select(self._model).where(
            self._model.id == id, self._model.is_active.is_(True)
        )

        async with self._session_factory() as session:
            row = await session.execute(query)

            try:
                analysis = AnalysisSchema.from_orm(row.one()[0])
            except NoResultFound:
                raise NotFoundError(f"Анализ с {id=} не найден.")

        return analysis
