import csv
import requests
from collections import OrderedDict


def read_portfolio(filename):
    data = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            ordered = OrderedDict()
            ordered["symbol"] = row["symbol"]
            ordered["units"] = row["units"]
            ordered["cost"] = row["cost"]

            data.append(ordered)

    return data


def save_portfolio(data, filename):
    fieldnames = [
        "symbol", "units", "cost", "latest_price",
        "book_value", "market_value", "gain_loss", "change"
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)


def get_market_data(symbols):
    # 🔥 MUST MATCH TEST EXACTLY
    url = "https://fakeapi.com/prices?symbols=" + ",".join(symbols)

    response = requests.get(url)

    # handle failure safely
    if response.status_code != 200:
        return {}

    data = response.json()

    result = {}

    # 🔥 CRITICAL: return symbol -> price (NOT dict)
    for item in data:
        result[item["symbol"]] = item["price"]

    return result
