from fastapi import APIRouter, Request, Response
from telegram import Update

from app.container import CONTAINER

TAG = "telegram"
PREFIX = f"/{TAG}"


router = APIRouter(prefix=PREFIX, tags=[TAG])


@router.post("")
async def post_telegram(request: Request) -> "Response":
    """Получить специалистов."""
    telegram_app = CONTAINER.telegram_app()

    await telegram_app.update_queue.put(
        Update.de_json(data=await request.json(), bot=telegram_app.bot)
    )

    return Response()
