from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import ALLOWED_ORIGINS


app = FastAPI(
    title="DermaAgent API",
    description="Skin Lesion Analysis and Evidence-Based Care Guidance System",
    version="1.0.0"
)


# CORS configuration

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        origin.strip()
        for origin in ALLOWED_ORIGINS
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register API routes

app.include_router(
    api_router,
    prefix="/api/v1"
)


@app.get("/")
def root():

    return {
        "message": "Welcome to DermaAgent API",
        "status": "Backend is running"
    }