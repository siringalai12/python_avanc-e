from pydantic import BaseModel
from typing import List

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    email: str
    department_id: int

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    department: DepartmentResponse

    class Config:
        orm_mode = True
