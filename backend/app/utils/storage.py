from __future__ import annotations

import shutil
import uuid
from pathlib import Path

import requests
from fastapi import UploadFile

from app.config import settings

ALLOWED_IMAGE_MIME_TYPES = {
	"image/jpeg",
	"image/png",
	"image/gif",
	"image/webp",
}

ALLOWED_VIDEO_MIME_TYPES = {
	"video/mp4",
	"video/webm",
	"video/quicktime",
}

ALLOWED_MEDIA_MIME_TYPES = ALLOWED_IMAGE_MIME_TYPES | ALLOWED_VIDEO_MIME_TYPES

ALLOWED_MEDIA_EXTENSIONS = {
	".jpg",
	".jpeg",
	".png",
	".gif",
	".webp",
	".mp4",
	".webm",
	".mov",
}

UPLOAD_DIR = Path(__file__).resolve().parents[2] / "uploads"
IMAGEKIT_UPLOAD_API = "https://upload.imagekit.io/api/v1/files/upload"


def is_imagekit_enabled() -> bool:
	return bool(settings.imagekit_private_key and settings.imagekit_url_endpoint)


def _upload_to_imagekit(upload_file: UploadFile) -> tuple[str, int]:
	if not upload_file.filename:
		raise RuntimeError("Missing filename for upload")

	ext = Path(upload_file.filename).suffix.lower()
	stored_name = f"{uuid.uuid4().hex}{ext}"
	upload_file.file.seek(0)

	form_data = {
		"fileName": stored_name,
		"useUniqueFileName": "false",
	}
	if settings.imagekit_folder:
		form_data["folder"] = settings.imagekit_folder

	files = {
		"file": (
			stored_name,
			upload_file.file,
			upload_file.content_type or "application/octet-stream",
		)
	}

	response = requests.post(
		IMAGEKIT_UPLOAD_API,
		auth=(settings.imagekit_private_key or "", ""),
		data=form_data,
		files=files,
		timeout=30,
	)
	if response.status_code >= 400:
		raise RuntimeError(f"ImageKit upload failed: {response.text}")

	payload = response.json()
	file_url = payload.get("url")
	file_size = payload.get("size")
	if not file_url or file_size is None:
		raise RuntimeError("ImageKit upload response is missing url or size")

	return str(file_url), int(file_size)


def _save_upload_file_locally(upload_file: UploadFile, upload_dir: Path = UPLOAD_DIR) -> tuple[str, int]:
	upload_dir.mkdir(parents=True, exist_ok=True)
	ext = Path(upload_file.filename).suffix.lower()
	stored_name = f"{uuid.uuid4().hex}{ext}"
	absolute_file_path = upload_dir / stored_name

	with open(absolute_file_path, "wb") as buffer:
		shutil.copyfileobj(upload_file.file, buffer)

	file_size = absolute_file_path.stat().st_size
	public_file_path = f"uploads/{stored_name}"
	return public_file_path, file_size


def delete_local_file_if_exists(file_path: str, upload_dir: Path = UPLOAD_DIR) -> None:
	relative_path = str(file_path).replace("\\", "/")
	absolute_path = upload_dir / Path(relative_path).name
	if absolute_path.exists():
		absolute_path.unlink()

def is_allowed_media(upload_file: UploadFile) -> bool:
	if not upload_file.filename or not upload_file.content_type:
		return False
	ext = Path(upload_file.filename).suffix.lower()
	return (
		upload_file.content_type in ALLOWED_MEDIA_MIME_TYPES
		and ext in ALLOWED_MEDIA_EXTENSIONS
	)

def save_upload_file(upload_file: UploadFile, upload_dir: Path = UPLOAD_DIR) -> tuple[str, int]:
	if is_imagekit_enabled():
		return _upload_to_imagekit(upload_file)

	return _save_upload_file_locally(upload_file, upload_dir)
