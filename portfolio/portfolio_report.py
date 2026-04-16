import argparse
import csv
import requests


# ✅ READ CSV (must return FLOATS)
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


# ✅ API (exact URL format required)
def get_market_data(symbols):
    url = "https://fakeapi.com/prices?symbols=" + ",".join(symbols)
    response = requests.get(url)

    data = response.json()

    prices = {}
    for item in data:
        prices[item["symbol"]] = item["price"]

    return prices


# ✅ CALCULATE (matches calculator tests)
def calculate(portfolio, prices):
    result = []

    for row in portfolio:
        symbol = row["symbol"]
        units = row["units"]
        cost = row["cost"]

        if symbol not in prices:
            continue

        market_price = prices[symbol]

        book_value = units * cost
        market_value = units * market_price
        gain_loss = market_value - book_value

        change = gain_loss / book_value if book_value != 0 else 0

        result.append({
            "symbol": symbol,
            "units": units,
            "book_value": book_value,
            "market_value": market_value,
            "gain_loss": gain_loss,
            "change": change
        })

    return result


# ✅ SAVE CSV (must match IO test format)
def save_portfolio(data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "symbol",
            "units",
            "cost"
        ])
        writer.writeheader()

        for row in data:
            writer.writerow({
                "symbol": row["symbol"],
                "units": row["units"],
                "cost": row["book_value"] / row["units"]
            })


# ✅ MAIN
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    args = parser.parse_args()

    portfolio = read_portfolio(args.source)
    symbols = [row["symbol"] for row in portfolio]
    prices = get_market_data(symbols)

    result = calculate(portfolio, prices)
    save_portfolio(result, args.target)


# ✅ RUN
if __name__ == "__main__":
    main()
