from environs import Env
from pydantic import BaseModel


class ExternalConfig(BaseModel):
    api_key: str


def load_external_config(path: str | None = None):
    env = Env()
    env.read_env(path)

    return ExternalConfig(
        api_key=env('API_KEY')
    )
