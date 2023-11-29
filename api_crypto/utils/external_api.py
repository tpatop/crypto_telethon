from requests import Response, get
from core.config import load_external_config, ExternalConfig


conf: ExternalConfig = load_external_config()
URL = 'http://api.coinlayer.com/'


async def requests_crypto_list():
    response: Response = get(
        url=URL + f'live?access_key={conf.api_key}'
    )
    response = response.json()['rates']
    return response
