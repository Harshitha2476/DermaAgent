import os
import uuid

from fastapi import UploadFile, HTTPException

from app.core.config import (
    UPLOAD_DIR,
    MAX_IMAGE_SIZE
)

from app.utils.validators import validate_image


async def save_image(file: UploadFile):

    temp_path = os.path.join(
        UPLOAD_DIR,
        f"{uuid.uuid4().hex}.tmp"
    )

    image_id = str(uuid.uuid4())

    try:

        total_size = 0

        with open(temp_path, "wb") as buffer:

            while True:

                chunk = await file.read(1024 * 1024)

                if not chunk:
                    break

                total_size += len(chunk)

                if total_size > MAX_IMAGE_SIZE:
                    raise HTTPException(
                        status_code=413,
                        detail="Image size exceeds 10 MB."
                    )

                buffer.write(chunk)

        if total_size == 0:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        image_format = validate_image(temp_path)

        extension = ".jpg" if image_format == "JPEG" else ".png"

        filename = image_id + extension

        final_path = os.path.join(
            UPLOAD_DIR,
            filename
        )

        os.replace(temp_path, final_path)

        return {
            "image_id": image_id,
            "filename": filename,
            "image_format": image_format,
            "file_size": total_size
        }

    except Exception:

        if os.path.exists(temp_path):
            os.remove(temp_path)

        raise

    finally:
        await file.close()