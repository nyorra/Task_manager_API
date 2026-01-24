from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.db import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

"""CRUD - create read update delete - операции для работы с данными"""

# 1. create
@router.post("/", response_model=TaskCreate, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# 2. read all users
@router.get("/", response_model=list[TaskRead])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).options(joinedload(Task.user)).all()


# 3. read 1 u
@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# 4. u upd
@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = task_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task


# 5. u del
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return None


# Дополнительный ендпоинт для задач конкретного пользователя
@router.get("/user/{user_id}", response_model=list[TaskRead])
def get_user_tasks(user_id: int, db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.user_id == user_id).all()
