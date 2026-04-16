import argparse
import csv


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


def get_market_data(symbols):
    return {symbol: 100.0 for symbol in symbols}

def calculate(portfolio, prices):
    result = []

    for row in portfolio:
        symbol = row["symbol"]
        units = row["units"]
        cost = row["cost"]

        # skip if symbol not in prices
        if symbol not in prices:
            continue

        market_price = prices[symbol]

        book_value = units * cost
        market_value = units * market_price
        gain_loss = market_value - book_value

        if book_value != 0:
            change = gain_loss / book_value
        else:
            change = 0

        result.append({
            "symbol": symbol,
            "units": units,
            "book_value": book_value,
            "market_value": market_value,
            "gain_loss": gain_loss,
            "change": change
        })

    return result
    return result


def save_portfolio(data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "symbol", "units", "cost",
            "market_price", "market_value", "gain"
        ])
        writer.writeheader()
        writer.writerows(data)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    return parser.parse_args()

def main():
    args = get_args()
    portfolio = read_portfolio(args.source)
    symbols = [row["symbol"] for row in portfolio]
    prices = get_market_data(symbols)
    result = calculate(portfolio, prices)
    save_portfolio(result, args.target)


if __name__ == "__main__":
    main()
    
