from requests import post, Response


async def load_data():
    response: Response = post(
        url='http://crypto_api:8080/live'
    )
    return response.json()


async def convert_all_data():
    data_dict = await load_data()
    data_list = []
    f = '**Cost in USD**:\n'
    for item in data_dict.items():
        f += f'{item[0]}: {item[1]}\n'
        # разбиение по блокам в 1024 байта (для удобства)
        # ограничение телеграма в 4096 байт
        if len(f) >= 1024:
            data_list.append(f)
            f = ''
    else:
        # добавления последнего элемента
        if f != '':
            data_list.append(f)
    del data_dict
    return data_list
