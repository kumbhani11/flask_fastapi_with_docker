import json, requests, os
from fastapi.responses import JSONResponse
import aiohttp
from backend.services.utils import *
from datetime import date
from dotenv import load_dotenv
from backend.config.mongo import db

load_dotenv()

