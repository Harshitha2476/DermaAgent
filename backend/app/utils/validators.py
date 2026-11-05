from PIL import Image, UnidentifiedImageError
from fastapi import HTTPException
import os


def validate_image(file_path: str):

    try:
        with Image.open(file_path) as image:

            image_format = image.format

            if image_format not in ["JPEG", "PNG"]:
                raise HTTPException(
                    status_code=400,
                    detail="Only JPG, JPEG and PNG images are allowed."
                )

            image.verify()

            return image_format

    except UnidentifiedImageError:
        raise HTTPException(
            status_code=400,
            detail="Invalid image file."
        )

    except OSError:
        raise HTTPException(
            status_code=400,
            detail="Unable to read the uploaded image."
        )