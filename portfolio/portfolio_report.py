"""
Generates performance reports for your stock portfolio.
"""
import argparse
import csv
import requests

def main():
    args = get_args()

    portfolio = read_portfolio(args.source)
    symbols = [row["symbol"] for row in portfolio]

    prices = get_market_data(symbols)
    result = calculate(portfolio, prices)

    save_portfolio(result, args.target)

    print("Report generated successfully!")

def read_portfolio(filename):
    data = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append({
                "symbol": row["symbol"],
                "units": float(row["units"]),
                "cost": float(row["cost"])
            })

    return data

def get_args(args=None):
    parser = argparse.ArgumentParser()

    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)

    return parser.parse_args(args)

def get_market_data(symbols):
    url = "https://fakeapi.com/prices?symbols=" + ",".join(symbols)

    response = requests.get(url)

    if response.status_code != 200:
        return {}

    data = response.json()

    prices = {}
    for item in data:
        prices[item["symbol"]] = float(item["price"])

    return prices

def calculate(data, prices):
    result = []

    for row in data:
        symbol = row["symbol"]

        # skip missing symbol
        if symbol not in prices:
            continue

        units = float(row["units"])
        cost = float(row["cost"])
        latest_price = float(prices[symbol])

        book_value = units * cost
        market_value = units * latest_price
        gain_loss = market_value - book_value

        change = gain_loss / book_value if book_value != 0 else 0

        result.append({
            "symbol": symbol,
            "units": units,
            "cost": cost,
            "latest_price": round(latest_price, 2),
            "book_value": round(book_value, 2),
            "market_value": round(market_value, 2),
            "gain_loss": round(gain_loss, 2),
            "change": round(change, 2)
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
        writer.writerows(data)


if __name__ == "__main__":
    main()
