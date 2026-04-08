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
    with open(filename, "w", newline="") as file:
        fieldnames = ["symbol", "units", "cost"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)
            
def get_market_data(symbols):
    # EXACT format required
    url = "https://fakeapi.com/prices?symbols=" + ",".join(symbols)

    response = requests.get(url)
    data = response.json()

    result = {}
    for item in data:
        result[item["symbol"]] = item["price"]

    return result

if __name__ == "__main__":
    main()


# ---------------------------
# CALCULATE METRICS (FIXED)
# ---------------------------
def calculate_metrics(portfolio, prices):
    results = []

    for stock in portfolio:
        symbol = stock["symbol"]
        units = int(stock["units"])
        cost = float(stock["cost"])
        price = prices[symbol]

        book_value = units * cost
        market_value = units * price
        gain_loss = market_value - book_value

        change = gain_loss / book_value if book_value != 0 else 0

        results.append({
            "symbol": symbol,
            "book_value": int(book_value),
            "market_value": int(market_value),
            "gain_loss": int(gain_loss),
            "change": change
        })

    return results


# ---------------------------
# MAIN (optional but safe)
# ---------------------------
def main():
    import argparse

    parser = argparse.ArgumentParser(description="Portfolio Report")
    parser.add_argument("file", help="CSV file path")

    args = parser.parse_args()

    portfolio = read_portfolio(args.file)
    symbols = [stock["symbol"] for stock in portfolio]

    prices = get_market_data(symbols)
    metrics = calculate_metrics(portfolio, prices)

    for item in metrics:
        print(item)


if __name__ == "__main__":
    main()
