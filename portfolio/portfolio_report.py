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
    url = "https://fakeapi.com/prices?symbols=" + ",".join(symbols)

    response = requests.get(url)
    data = response.json()

    result = {}
    for item in data:
        result[item["symbol"]] = item["price"]

    return result


def calculate_metrics(portfolio, prices):
    results = []

    for stock in portfolio:
        symbol = stock["symbol"]
        units = int(stock["units"])
        cost = float(stock["cost"])
        price = prices.get(symbol, 0)

        book_value = units * cost
        market_value = units * price
        gain_loss = market_value - book_value
        change = gain_loss / book_value if book_value != 0 else 0

        results.append({
            "symbol": symbol,
            "units": units,
            "cost": cost,
            "latest_price": price,
            "book_value": int(book_value),
            "market_value": int(market_value),
            "gain_loss": int(gain_loss),
            "change": change
        })

    return results


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Stock Portfolio Report")

    parser.add_argument("--source", required=True, help="Input CSV file")
    parser.add_argument("--target", required=True, help="Output CSV file")

    args = parser.parse_args()

    portfolio = read_portfolio(args.source)
    symbols = [stock["symbol"] for stock in portfolio]

    prices = get_market_data(symbols)
    results = calculate_metrics(portfolio, prices)

    save_portfolio(results, args.target)

    print(f"Report saved to {args.target}")


if __name__ == "__main__":
    main()

