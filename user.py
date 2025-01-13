# user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.backend.db import Base  # Импортируем Base из вашего файла db.py
from fastapi import APIRouter


# Создание модели User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    # Связь с моделью Task
    tasks = relationship("Task", back_populates="user")


# Ваши маршруты
router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users():
    return {"message": "Получение всех пользователей"}


@router.get("/{user_id}")
async def user_by_id(user_id: int):
    return {"message": f"Получение пользователя с ID {user_id}"}


@router.post("/create")
async def create_user():
    return {"message": "Создание нового пользователя"}


@router.put("/update")
async def update_user():
    return {"message": "Обновление пользователя"}


@router.delete("/delete")
async def delete_user():
    return {"message": "Удаление пользователя"}
