import requests
import json
import subprocess
import sys
import configparser

with open("id.txt", "r") as file:
    id = file.read() 

subprocess.run(["python", "getprice.py"])
with open("data.json", "r") as f:
    data = json.load(f)
stockprice = data["price"]

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
    'Referer': f'https://www.pekora.zip/catalog/{id}/',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=0',
}

json_data = {
    'assetId': id,
    'expectedPrice': stockprice,
    'expectedSellerId': 1,
    'userAssetId': None,
    'expectedCurrency': 1,
}

rapresponse = requests.get(f'https://www.pekora.zip/apisite/economy/v1/assets/{id}/resale-data', cookies=cookies, headers=headers)

try:
    rapjson = rapresponse.json()
    rap = rapjson.get("recentAveragePrice")
    print("RAP:", rap)
except ValueError:
    print(rapresponse.text)

if rap >= 1000:
    response = requests.post(
        f'https://www.pekora.zip/apisite/economy/v1/purchases/products/{id}',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
else:
    print("not worth")
    sys.exit()

print(response.status_code)
print(response.text)