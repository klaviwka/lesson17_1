from fastapi import FastAPI
from app.models.user import router as user_router
from app.models.task import router as task_router

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# Подключаем маршруты из user.py
app.include_router(user_router)
app.include_router(task_router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
