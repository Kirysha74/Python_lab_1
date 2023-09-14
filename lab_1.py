import datetime
import time
import json
import csv
import requests

begin = time.time()

date = datetime.date.today()
file = open("dataset.csv", "w")
fwriter = csv.writer(file, delimiter = ",", lineterminator="\r")

while True:

    year = str(date.year)
    month = str(date.month) if date.month > 9 else "0" + str(date.month)
    day = str(date.day) if date.day > 9 else "0" + str(date.day)

    if date.weekday() == 0 or date.weekday() == 6:
        date = date - datetime.timedelta(1)
        continue

    date = date - datetime.timedelta(1)
    
    url = "https://www.cbr-xml-daily.ru/archive/" + year + "/" + month + "/" + day + "/daily_json.js"

    response = requests.get(url)
    if response.status_code != 200:
        continue

    json_f = json.loads(response.text)

    fwriter.writerow([f"{year}.{month}.{day}", json_f["Valute"]["USD"]["Value"]])

    if date.year < 2014:
        break

file.close()