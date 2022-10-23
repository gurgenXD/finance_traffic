from sqladmin import ModelView

from app.adapters.storage.models.contacts import Contact


class ContactAdmin(ModelView, model=Contact):
    """Контакты в админ панели."""

    name = "Контакты"
    name_plural = "Контакты"
    icon = "fa-solid fa-hospital"

    column_list = ("id", "city", "address")
    column_labels = {
        "id": "ID",
        "city": "Город",
        "address": "Адрес",
        "description": "Описание",
        "work_time": "Рабочее время",
        "phone": "Телефон",
        "email": "E-mail",
        "map_code": "Код карты",
    }
