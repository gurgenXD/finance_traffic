from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import handlers

from app.api import admin
from app.api.routers import telegram
from utils.constants import BASE_DIR
from app.container import CONTAINER


STATIC_PREFIX = "/static"


def create_app() -> "FastAPI":
    """Создать приложение FastAPI."""
    app = FastAPI(docs_url=None, redoc_url=None)

    # Добавление обработчиков ошибок.
    handlers.add_all(app)

    # # Подключение админ-панели.
    # admin.create_app(app)

    # # Подключение подприложений.
    # static_files = StaticFiles(directory=BASE_DIR / "app" / "static")
    # app.mount(STATIC_PREFIX, static_files, name="static")

    app.include_router(telegram.router)
    # app.include_router(analyzes.router)
    # app.include_router(contacts.router)
    # app.include_router(news.router)
    # app.include_router(pages.router)
    # app.include_router(promotions.router)
    # app.include_router(services.router)

    @app.on_event("startup")
    async def startup_event():
        telegram_app = CONTAINER.telegram_app()

        await telegram_app.bot.set_webhook(url="https://domain.tld/telegram")

        telegram_app.start()

    @app.on_event("shutdown")
    async def shutdown_event():
        telegram_app = CONTAINER.telegram_app()
        telegram_app.stop()

    return app
