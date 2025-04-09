from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(title="AI Fashion Recommender")

app.include_router(api_router)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}
