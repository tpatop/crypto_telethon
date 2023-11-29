from environs import Env
from pydantic import BaseModel


class BotConfig(BaseModel):
    api_id: int
    api_hash: str


def load_bot_config(path: str | None = None):
    env = Env()
    env.read_env()

    return BotConfig(
        api_id=env('API_TG_ID'),
        api_hash=env('API_TG_HASH')
    )
