import csv
import requests
from collections import OrderedDict


# ---------------------------
# READ PORTFOLIO
# ---------------------------
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


# ---------------------------
# SAVE PORTFOLIO
# ---------------------------
def save_portfolio(data, filename):
    with open(filename, "w", newline="") as file:
        fieldnames = ["symbol", "units", "cost"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


# ---------------------------
# API FUNCTION
# ---------------------------
def get_market_data(symbols):
    # convert list → string
    symbols_str = ",".join(symbols)

    # MUST match test exactly
    url = f"https://fakeapi.com/prices?symbols={symbols_str}"

    response = requests.get(url)
    data = response.json()

    result = {}
    for item in data:
        result[item["symbol"]] = item["price"]

    return result


# ---------------------------
# CALCULATIONS
# ---------------------------
def calculate_portfolio_value(portfolio, market_data):
    total = 0

    for stock in portfolio:
        symbol = stock["symbol"]
        units = int(stock["units"])          # must be int
        price = market_data[symbol]          # direct access

        total += units * price

    return total


def calculate_profit_loss(portfolio, market_data):
    total_cost = 0
    total_value = 0

    for stock in portfolio:
        symbol = stock["symbol"]
        units = int(stock["units"])          # must be int
        cost = float(stock["cost"])
        price = market_data[symbol]

        total_cost += units * cost
        total_value += units * price

    return total_value - total_cost


# ---------------------------
# MAIN (for CLI / packaging)
# ---------------------------
def main():
    import argparse

    parser = argparse.ArgumentParser(description="Portfolio Report")
    parser.add_argument("file", help="CSV file path")

    args = parser.parse_args()

    portfolio = read_portfolio(args.file)
    symbols = [stock["symbol"] for stock in portfolio]

    market_data = get_market_data(symbols)

    total_value = calculate_portfolio_value(portfolio, market_data)
    profit_loss = calculate_profit_loss(portfolio, market_data)

    print(f"Total Value: {total_value}")
    print(f"Profit/Loss: {profit_loss}")


if __name__ == "__main__":
    main()
