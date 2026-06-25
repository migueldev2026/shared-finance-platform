import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    APP_NAME = os.getenv("APP_NAME")

    DEBUG = os.getenv("FLASK_DEBUG")