import csv
import requests
import argparse


# ✅ READ CSV
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


# ✅ GET MARKET DATA
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


# ✅ CALCULATE (FINAL FIX — NO ROUNDING)
def calculate(data, prices):
    result = []

    for row in data:
        symbol = row["symbol"]

        # ✅ skip missing symbols (REQUIRED for test)
        if symbol not in prices:
            continue

        units = row["units"]
        cost = row["cost"]
        latest_price = prices[symbol]

        book_value = units * cost
        market_value = units * latest_price
        gain_loss = market_value - book_value

        # ✅ avoid division error
        change = gain_loss / book_value if book_value != 0 else 0

        result.append({
            "symbol": symbol,
            "units": units,
            "cost": cost,
            "latest_price": latest_price,
            "book_value": book_value,
            "market_value": market_value,
            "gain_loss": gain_loss,
            "change": change
        })

    return result


# ✅ WRITE OUTPUT CSV
def write_report(filename, data):
    fieldnames = [
        "symbol", "units", "cost", "latest_price",
        "book_value", "market_value", "gain_loss", "change"
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# ✅ MAIN FUNCTION
def main():
    parser = argparse.ArgumentParser(description="Stock Portfolio Report Generator")
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)

    args = parser.parse_args()

    portfolio = read_portfolio(args.source)
    symbols = [row["symbol"] for row in portfolio]

    prices = get_market_data(symbols)
    report = calculate(portfolio, prices)

    write_report(args.target, report)

    print("Report generated successfully!")


if __name__ == "__main__":
    main()
