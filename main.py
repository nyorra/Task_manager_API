from fastapi import FastAPI
from app.routers import user, task
from app.db import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskManager API")

app.include_router(user.router)
print("user router success")
app.include_router(task.router)
print("task router success")
