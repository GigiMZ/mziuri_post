import requests
from urllib3 import request


api_key = "4c64c2eb3e904a29ad4122526252201"
endpoint = "https://www.weatherapi.com/v1"

r = requests.post(f'{endpoint}/current.json?key={api_key}')
print(r.json())