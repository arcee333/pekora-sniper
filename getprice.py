import requests
import json
import configparser

with open("id.txt", "r") as file:
    priceid = file.read()

def getprice():
    config = configparser.ConfigParser()
    config.read('config.ini')
    pekosecurity = config.get('General', 'pekosecurity')

    cookies = {
        '.PEKOSECURITY': pekosecurity,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'Origin': 'https://www.pekora.zip',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': f'https://www.pekora.zip/catalog/{priceid}/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    json_data = {
        'items': [
            {
                'itemType': 'Asset',
                'id': priceid,
            },
        ],
    }

    response = requests.post(
        'https://www.pekora.zip/apisite/catalog/v1/catalog/items/details',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    print(response.status_code)
    print(response.text)

    data = response.json()
    price = data["data"][0]["price"]

    with open("data.json", "r") as f:
        try:
            jsondata = json.load(f)
        except json.JSONDecodeError:
            jsondata = {}

    jsondata["price"] = price

    with open("data.json", "w") as f:
        json.dump(jsondata, f, indent=4)

getprice()