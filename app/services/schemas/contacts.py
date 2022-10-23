from pydantic import BaseModel


class ContactSchema(BaseModel):
    """Схема контакта."""

    city: str
    description: str
    address: str
    work_time: str
    phone: str
    email: str
    map_code: str

    class Config:
        orm_mode = True
