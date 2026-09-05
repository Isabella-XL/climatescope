import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.climate import router as climate_router

app = FastAPI(
    title="ClimateScope API",
    description="AI-powered climate data analysis platform",
    version="1.0.0",
)

cors_origins = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:5173",
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(climate_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "ClimateScope API is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}
