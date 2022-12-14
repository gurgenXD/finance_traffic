from typing import TYPE_CHECKING

from sqladmin import Admin

from app.adapters.storage.db import engine
from app.api.admin.routers.analyzes import AnalysisAdmin, AnalysisTypeAdmin
from app.api.admin.routers.callbacks import CallbacksAdmin
from app.api.admin.routers.contacts import ContactAdmin
from app.api.admin.routers.news import NewsAdmin
from app.api.admin.routers.pages import PagesAdmin
from app.api.admin.routers.promotions import PromotionsAdmin
from app.api.admin.routers.services import ServiceAdmin, ServiceTypeAdmin
from app.api.admin.routers.specialists import (SpecialistAdmin,
                                               SpecializationAdmin)
from app.api.admin.routers.users import UsersAdmin

if TYPE_CHECKING:
    from fastapi import FastAPI

PREFIX = "/admin"


def create_app(app: "FastAPI") -> None:
    """Добавить роутеры админ-панели."""

    admin = Admin(app, engine.get_async(), base_url=PREFIX, title="Админ-панель")

    admin.add_view(AnalysisTypeAdmin)
    admin.add_view(AnalysisAdmin)
    admin.add_view(SpecializationAdmin)
    admin.add_view(SpecialistAdmin)
    admin.add_view(ServiceTypeAdmin)
    admin.add_view(ServiceAdmin)
    admin.add_view(ContactAdmin)
    admin.add_view(NewsAdmin)
    admin.add_view(UsersAdmin)
    admin.add_view(PromotionsAdmin)
    admin.add_view(PagesAdmin)
    admin.add_view(CallbacksAdmin)
