from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="ClimateScope API",
    description="AI-powered climate data analysis platform",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "ClimateScope API is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}
