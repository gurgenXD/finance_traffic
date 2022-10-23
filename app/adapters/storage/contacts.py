from collections.abc import Callable
from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING

from sqlalchemy import select

from app.adapters.storage.models import Contact
from app.services.schemas.contacts import ContactSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class ContactsAdapter:
    """Адаптер для доступа к данным контактов."""

    def __init__(
        self, session_factory: Callable[[], AbstractAsyncContextManager["AsyncSession"]]
    ) -> None:
        self._session_factory = session_factory
        self._model = Contact

    async def get_all(self) -> list["ContactSchema"]:
        """Получить все контакты."""

        query = select(self._model)

        async with self._session_factory() as session:
            rows = await session.execute(query)
            contacts = [ContactSchema.from_orm(row) for row in rows.scalars()]

        return contacts
