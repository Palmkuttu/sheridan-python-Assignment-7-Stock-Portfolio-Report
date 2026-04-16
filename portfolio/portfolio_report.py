import argparse
import csv
import requests


# ✅ READ (KEEP STRINGS)
def read_portfolio(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                "symbol": row["symbol"],
                "units": row["units"],
                "cost": row["cost"]
            })
    return data


# ✅ API (RETURN LIST)
def get_market_data(symbols):
    url = "https://fakeapi.com/prices?symbols=" + ",".join(symbols)
    response = requests.get(url)
    return response.json()   # IMPORTANT


# ✅ CALCULATE
def calculate(portfolio, prices):
    result = []

    # convert API list → dict for lookup
    price_map = {item["symbol"]: item["price"] for item in prices}

    for row in portfolio:
        symbol = row["symbol"]
        units = int(row["units"])
        cost = float(row["cost"])

        if symbol not in price_map:
            continue

        latest_price = price_map[symbol]

        book_value = units * cost
        market_value = units * latest_price
        gain_loss = market_value - book_value
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


# ✅ SAVE (ALL COLUMNS)
def save_portfolio(data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["symbol", "units", "cost"])
        writer.writeheader()

        for row in data:
            writer.writerow({
                "symbol": row["symbol"],
                "units": row["units"],
                "cost": row["cost"]
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


if __name__ == "__main__":
    main()
