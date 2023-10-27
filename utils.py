import datetime
import json
import csv

import requests


def get_date(date: datetime.date) -> str:
    year = str(date.year)
    month = str(date.month) if date.month > 9 else "0" + str(date.month)
    day = str(date.day) if date.day > 9 else "0" + str(date.day)
    return year + "/" + month + "/" + day


def get_past_day(date: datetime.date) -> datetime.date:
    return date - datetime.timedelta(1)


def record_currency_rate(file_name: str = "dataset1", boundary_date: datetime.date = datetime.date(2023, 1, 1), valute: str = "USD") -> None:
    date = get_past_day(datetime.date.today())
    file = open(f"{file_name}.csv", "w")
    fwriter = csv.writer(file, delimiter=",", lineterminator="\r")

    while date >= boundary_date:

        if date.weekday() == 0 or date.weekday() == 6:
            date = get_past_day(date)
            continue

        url = "https://www.cbr-xml-daily.ru/archive/" + \
            get_date(date) + "/daily_json.js"
        response = requests.get(url)
        if response.status_code != 200:
            date = get_past_day(date)
            continue

        json_f = json.loads(response.text)
        fwriter.writerow([get_date(date), json_f["Valute"][valute]["Value"]])
        
        date = get_past_day(date)

    file.close()


def main() -> None:
    record_currency_rate()
