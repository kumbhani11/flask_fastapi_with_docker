import os
from datetime import datetime, timedelta
from fastapi import FastAPI, APIRouter, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from backend.controllers.post_api import *

router = APIRouter()

@router.get("/", include_in_schema=False)
def welcome():
    return "Welcome"

