from fastapi import FastAPI
from app.routers import user, task
from app.db import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

@app.get("/greetings")
def get_home():
    return "Hi bro"


@app.get("/")\
def default_page():
    for route in app.routes:
        print(f"Path: {route.path}  |  Name: {route.name}  |  Methods: {route.methods}")
    return ExistingEndpoints

app.include_router(user.router)
print("user router success")

app.include_router(task.router)
print("task router success")

