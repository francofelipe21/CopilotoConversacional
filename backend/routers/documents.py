from fastapi import UploadFile
from typing import List
from fastapi import APIRouter
from backend.controllers.documents import new_pdfs

router = APIRouter()

@router.post("/upload_pdfs")
async def upload_pdfs(files: List[UploadFile]):
    response = await new_pdfs(files)
    return response