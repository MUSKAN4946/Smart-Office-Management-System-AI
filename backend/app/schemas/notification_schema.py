from pydantic import BaseModel


class NotificationCreate(BaseModel):
    employee_id: int
    title: str
    message: str


class NotificationResponse(BaseModel):
    id: int
    employee_id: int
    title: str
    message: str
    is_read: bool

    class Config:
        from_attributes = True