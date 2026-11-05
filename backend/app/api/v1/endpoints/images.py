from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.image_service import save_image


router = APIRouter(
    prefix="/images",
    tags=["Image Upload"]
)


@router.post("/upload")
async def upload_skin_image(
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided."
        )

    result = await save_image(file)

    return {
        "success": True,
        "message": "Image uploaded successfully.",
        "data": result
    }