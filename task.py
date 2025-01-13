# task.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base
from fastapi import APIRouter


# Создание модели Task
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates="tasks")


# Создание маршрутов
router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks():
    return {"message": "Получение всех задач"}


@router.get("/{task_id}")
async def task_by_id(task_id: int):
    return {"message": f"Получение задачи с ID {task_id}"}


@router.post("/create")
async def create_task():
    return {"message": "Создание новой задачи"}


@router.put("/update")
async def update_task():
    return {"message": "Обновление задачи"}


@router.delete("/delete")
async def delete_task():
    return {"message": "Удаление задачи"}
