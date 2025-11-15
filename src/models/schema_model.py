from pydantic import BaseModel
from typing import Dict, List

class FileInfo(BaseModel):
    FileSchema : List[Dict]
    FileSample: List[Dict]
    