import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

ALLOWED_ORIGINS = os.getenv(
    "FRONTEND_ORIGINS",
    "http://localhost:3000,http://localhost:5173"
).split(",")

os.makedirs(UPLOAD_DIR, exist_ok=True)