from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.database import Base, engine
from app.models import models
from app.routers.auth import router as auth_router
from app.routers.admin import router as admin_router
from app.routers.users import router as user_router
from app.routers.todos import router as todo_router



# Initialization of the tables without alembic using lifespan events
"""
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
"""

app = FastAPI()

@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(user_router)
app.include_router(todo_router)
