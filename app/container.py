from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Callable, Singleton

from app.adapters.storage.db import engine, session
from app.adapters.telegram import factory as telegram_bot
from app.settings.db import DatabaseSettings

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
    from telegram.ext import Application


class Container(DeclarativeContainer):
    """Контейнер зависимостей приложения."""

    db_settings: Singleton["DatabaseSettings"] = Singleton(DatabaseSettings)

    async_engine: Singleton["AsyncEngine"] = Singleton(engine.get_async)
    session_ctx: Callable[AbstractAsyncContextManager["AsyncSession"]] = Callable(
        session.get_context, engine=async_engine.provided
    )

    telegram_app: Singleton["Application"] = Singleton(telegram_bot.create_app)
    # specialists_adapter: Singleton["SpecialistsAdapter"] = Singleton(
    #     SpecialistsAdapter, session_factory=session_ctx.provider
    # )


CONTAINER = Container()
