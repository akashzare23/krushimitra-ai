import os
from dotenv import load_dotenv

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME", "default_image")
if not API_BASE_URL:
    raise ValueError("API_BASE_URL is missing in .env")

if not MODEL_NAME:
    raise ValueError("MODEL_NAME is missing in .env")
