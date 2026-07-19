from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    department_name: str
    department_code: str
    description: str


class DepartmentResponse(BaseModel):
    id: int
    department_name: str
    department_code: str
    description: str

    class Config:
        from_attributes = True