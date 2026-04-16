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
    prices = {}

    # ⚠️ Fake API → simulate data instead
    for symbol in symbols:
        prices[symbol] = 100.0  # dummy price (you can change)

    return prices

def calculate(portfolio, prices):
    result = []

    for row in portfolio:
        symbol = row["symbol"]
        units = row["units"]
        cost = row["cost"]

        market_price = prices.get(symbol, 0)
        market_value = units * market_price
        gain = market_value - cost

        result.append({
            "symbol": symbol,
            "units": units,
            "cost": cost,
            "market_price": market_price,
            "market_value": market_value,
            "gain": gain
        })

    return result

def save_portfolio(data, filename):
    with open(filename, "w", newline="") as file:
        fieldnames = ["symbol", "units", "cost", "market_price", "market_value", "gain"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)
        
if __name__ == "__main__":
    main()
