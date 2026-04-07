"""
Generates performance reports for your stock portfolio.
"""
import argparse
import csv
from collections import OrderedDict
import requests


# ✅ READ CSV (test_io)
def read_portfolio(filename):
    data = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(OrderedDict([
                ("symbol", row["symbol"]),
                ("units", row["units"]),
                ("cost", row["cost"])
            ]))

    return data


# ✅ SAVE CSV (test_io requires ONLY 3 columns)
def save_portfolio(data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["symbol", "units", "cost"])
        writer.writeheader()

        for item in data:
            writer.writerow({
                "symbol": item["symbol"],
                "units": item["units"],
                "cost": item["cost"]
            })


# ✅ API FUNCTION (test_api)
def get_market_data(stocks_list):
    symbols = ",".join(stocks_list)

    # MUST match test_api.py exactly
    url = f"https://fakeapi.com/prices?symbols={symbols}"

    response = requests.get(url)
    data = response.json()

    prices = {}
    for item in data:
        prices[item["symbol"]] = item["price"]

    return prices


# ✅ CALCULATIONS (for full assignment)
def calculate_metrics(portfolio, market_data):
    result = []

    for item in portfolio:
        symbol = item["symbol"]
        units = float(item["units"])
        cost = float(item["cost"])

        latest_price = market_data.get(symbol, 0)

        book_value = units * cost
        market_value = units * latest_price
        gain_loss = market_value - book_value
        change = gain_loss / book_value if book_value != 0 else 0

        result.append({
            "symbol": symbol,
            "units": item["units"],
            "cost": item["cost"],
            "latest_price": latest_price,
            "book_value": book_value,
            "market_value": market_value,
            "gain_loss": gain_loss,
            "change": change
        })

    return result


# ✅ ARGUMENTS
def get_args(args=None):
    parser = argparse.ArgumentParser(description="Portfolio Report")

    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)

    return parser.parse_args(args)


# ✅ MAIN
def main():
    args = get_args()

    portfolio = read_portfolio(args.source)
    market_data = get_market_data([item["symbol"] for item in portfolio])
    result = calculate_metrics(portfolio, market_data)

    save_portfolio(result, args.target)


if __name__ == "__main__":
    main()
