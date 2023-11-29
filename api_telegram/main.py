from telethon.sync import TelegramClient
from .core.config import load_bot_config, BotConfig

from .utils.external_api import convert_all_data


conf: BotConfig = load_bot_config()
API_ID: int = conf.api_id
API_HASH: str = conf.api_hash


async def run(client: TelegramClient):
    data_list = await convert_all_data()
    # отправка сообщения в saved messages (Избранное) блоками
    for text in data_list:
        await client.send_message('me', text)


def main():
    client = TelegramClient('anon', API_ID, API_HASH)
    with client:
        client.loop.run_until_complete(run(client))


if __name__ == '__main__':
    main()
