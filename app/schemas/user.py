from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserRead(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    title: str
    description: str
    user_id: int

class UserDelete(BaseModel):
    title: str
    description: str
    user_id: int