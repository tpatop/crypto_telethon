import uvicorn
from fastapi import FastAPI

from utils.external_api import requests_crypto_list


app = FastAPI()


@app.post('/live')
async def get_live_crepto_list():
    data = await requests_crypto_list()
    print(data)
    return data


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0',
                port=8080, reload=True, workers=1)
