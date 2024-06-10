from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_Tables, delete_Tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_Tables()
    print("База очищена")
    await create_Tables()
    print("База готова")
    yield
    print("Выключение")

app=FastAPI(lifespan=lifespan)
app.include_router(tasks_router)