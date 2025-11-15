from fastapi import FastAPI, UploadFile, File
from utils.utils import generate_task_id
import asyncio
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s - %(levelname)s - %(asctime)s")

app = FastAPI()


