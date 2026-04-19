import os

from pydantic import BaseModel


class Settings(BaseModel):
    telegram_token: str
    football_token: str


def get_settings() -> Settings:
    return Settings(
        telegram_token=os.environ["TELEGRAM_ACCESS_TOKEN"],
        football_token=os.environ["FOOTBALL_API_KEY"]
    )