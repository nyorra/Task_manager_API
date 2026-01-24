from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    user_id: int

class TaskRead(BaseModel):
    id: int
    title: str
    description: str
    status: str
    user_id: int

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    title: str
    description: str
    user_id: int