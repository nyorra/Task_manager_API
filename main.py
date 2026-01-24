from fastapi import FastAPI
from app.routers import user, task
from app.db import Base, engine
from fastapi.responses import JSONResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(user.router)
print("User router success")

app.include_router(task .router)
print("Task router success")

@app.get("/")
def get_home():
    return {"data": "Test message"}

@app.get("/greetings")
def get_home():
    return {"data": "Hi bro"}

@app.get("/all-endpoints")
def list_endpoints():
    endpoints = []
    for route in app.routes:
        if hasattr(route, "methods"):
            endpoints.append({
                "path": route.path,
                "name": route.name,
                "methods": list(route.methods)
            })
    return JSONResponse(content=endpoints)

# Печать всех эндпоинтов при старте
print("Registered endpoints:")
for route in app.routes:
    if hasattr(route, "methods"):
        print(f"Path: {route.path}  |  Name: {route.name}  |  Methods: {route.methods}")
