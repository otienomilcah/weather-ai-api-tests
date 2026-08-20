import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("WEATHER_API_KEY")