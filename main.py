from fastapi import FastAPI

from app.api.v1.router import router
from app.core.database import Base, engine

app = FastAPI(
    title='CrewControl',
    version="0.5.0"
)

app.include_router(router)

Base.metadata.create_all(bind=engine)