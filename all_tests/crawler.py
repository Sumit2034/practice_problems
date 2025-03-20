import requests
import json

url = "https://eportal.incometax.gov.in/iec/loginapi/login"

params = {"entity": "BTLPV9993A", "serviceName": "wLoginService"}
response = requests.request(url=url, params=params, method='POST')

print("12122")

