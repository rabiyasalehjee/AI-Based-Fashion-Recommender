from fastapi import APIRouter, File, UploadFile, HTTPException
from app.recommender import get_fashion_suggestions
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid image file")

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    suggestions = get_fashion_suggestions(file_path)
    return {"filename": file.filename, "suggestions": suggestions}
