from pydantic import BaseModel


class AnnouncementCreate(BaseModel):
    title: str
    message: str


class AnnouncementResponse(BaseModel):
    id: int
    title: str
    message: str

    class Config:
        from_attributes = True

