from pydantic import BaseModel
from typing import Dict

class UploadJobId(BaseModel):
    jobid: Dict