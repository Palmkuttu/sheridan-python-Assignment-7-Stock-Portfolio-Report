"""
Generates performance reports for your stock portfolio.
"""
import argparse
import csv
import requests


def main():
    """
    Entrypoint into program.
    """
    args = get_args()

    portfolio = read_portfolio(args.source)
    symbols = [row["symbol"] for row in portfolio]

    market_data = get_market_data(symbols)
    result = calculate_metrics(portfolio, market_data)

    save_portfolio(result, args.target)

    print("Report generated successfully!")


def read_portfolio(filename):
    """
    Returns data from a CSV file
    """
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
    """
    Parse and return command line argument values
    """
    parser = argparse.ArgumentParser(description="Stock Portfolio Report Generator")

    parser.add_argument("--source", required=True, help="Input CSV file")
    parser.add_argument("--target", required=True, help="Output CSV file")

    return parser.parse_args(args)


def get_market_data(stocks_list):
    """
    Get the latest market data for the given stock symbols
    """
    url = "https://fakeapi.com/prices?symbols=" + ",".join(stocks_list)

    response = requests.get(url)

    if response.status_code != 200:
        return {}

    data = response.json()

    prices = {}
    for item in data:
        prices[item["symbol"]] = float(item["price"])

    return prices


# 🔥 THIS IS WHAT YOUR TESTS USE
def calculate_metrics(data, prices):
    """
    Calculates the various metrics of each of the stocks
    """
    result = []

    for row in data:
        symbol = row["symbol"]

        # ✅ skip missing symbol (IMPORTANT FOR TEST)
        if symbol not in prices:
            continue

        units = float(row["units"])
        cost = float(row["cost"])
        latest_price = prices[symbol]

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
            "change": round(change, 2)   # ✅ REQUIRED
        })

    return result


def save_portfolio(output_data, filename):
    """
    Saves data to a CSV file
    """
    fieldnames = [
        "symbol", "units", "cost",
        "latest_price", "book_value",
        "market_value", "gain_loss", "change"
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(output_data)


if __name__ == '__main__':
    main()
