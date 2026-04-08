import csv
import requests
import argparse
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


def get_market_data(symbols):
    url = "https://fakeapi.com/prices?symbols=" + ",".join(symbols)

    response = requests.get(url)

    if response.status_code != 200:
        return {}

    data = response.json()

    prices = {}
    for item in data:
        prices[item["symbol"]] = item["price"]

    return prices


def calculate_portfolio(data, prices):
    result = []

    for row in data:
        symbol = row["symbol"]
        units = float(row["units"])
        cost = float(row["cost"])

        latest_price = prices.get(symbol, 0)

        book_value = units * cost
        market_value = units * latest_price
        gain_loss = market_value - book_value

        change = gain_loss / book_value if book_value != 0 else 0

        result.append({
            "symbol": symbol,
            "units": row["units"],
            "cost": row["cost"],
            "latest_price": round(latest_price, 2),
            "book_value": round(book_value, 2),
            "market_value": round(market_value, 2),
            "gain_loss": round(gain_loss, 2),
            "change": round(change, 3)
        })

    return result


def save_portfolio(data, filename):
    fieldnames = [
        "symbol", "units", "cost",
        "latest_price", "book_value",
        "market_value", "gain_loss", "change"
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)


def main():
    parser = argparse.ArgumentParser(description="Stock Portfolio Report Generator")
    parser.add_argument("--source", required=True, help="Input CSV file")
    parser.add_argument("--target", required=True, help="Output CSV file")

    args = parser.parse_args()

    data = read_portfolio(args.source)
    symbols = [row["symbol"] for row in data]

    prices = get_market_data(symbols)
    result = calculate_portfolio(data, prices)

    save_portfolio(result, args.target)

    print("Report generated successfully!")


if __name__ == "__main__":
    main()
