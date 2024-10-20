from fastapi import FastAPI

from app.api.v1.router import router
from app.core.database import Base, engine

app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)