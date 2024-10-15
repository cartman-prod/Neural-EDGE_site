import uvicorn
from fastapi import FastAPI
from app_backend.api.base import router as base_router
from app_backend.api.project import router as project_router

app = FastAPI()

app.include_router(base_router)
app.include_router(project_router)


if __name__ == "__main__":
    uvicorn.run('main:app', host="127.1.1.1", port=5400, reload=True)