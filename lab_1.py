import datetime
import time
import json
import csv
import requests


for i in range(100):

    date = datetime.datetime.today() - datetime.timedelta(i)

    year = str(date.year)
    month = str(date.month) if date.month > 9 else "0" + str(date.month)
    day = str(date.day) if date.day > 9 else "0" + str(date.day)
    url = "https://www.cbr-xml-daily.ru/archive/" + year + "/" + month + "/" + day + "/daily_json.js"

    response = requests.get(url)
    if response.status_code != 200:
        continue
    json_f = json.loads(response.text)

