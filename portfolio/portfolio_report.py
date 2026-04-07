import csv
import requests
from collections import OrderedDict


# ---------------------------
# READ PORTFOLIO (IO TEST)
# ---------------------------
def read_portfolio(filename):
    """
    Read portfolio CSV file and return list of OrderedDict
    """
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
# SAVE PORTFOLIO (IO TEST)
# ---------------------------
def save_portfolio(data, filename):
    """
    Save portfolio data to CSV file
    """
    with open(filename, "w", newline="") as file:
        fieldnames = ["symbol", "units", "cost"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for row in data:
            writer.writerow(row)


# ---------------------------
# API FUNCTION (API TEST)
# ---------------------------
def get_market_data(symbols):
    """
    Fetch market prices for given symbols
    Returns dict like: {"SNAP": 15, "AAPL": 200}
    """

    # Convert list → comma-separated string
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
# CALCULATION (CALC TEST)
# ---------------------------
def calculate_portfolio_value(portfolio, market_data):
    """
    Calculate total portfolio value
    """
    total = 0.0

    for stock in portfolio:
        symbol = stock["symbol"]
        units = float(stock["units"])
        price = market_data.get(symbol, 0)

        total += units * price

    return total


def calculate_profit_loss(portfolio, market_data):
    """
    Calculate profit/loss
    """
    total_cost = 0.0
    total_value = 0.0

    for stock in portfolio:
        symbol = stock["symbol"]
        units = float(stock["units"])
        cost = float(stock["cost"])
        price = market_data.get(symbol, 0)

        total_cost += units * cost
        total_value += units * price

    return total_value - total_cost


# ---------------------------
# MAIN (CLI ENTRY)
# ---------------------------
def main():
    import argparse

    parser = argparse.ArgumentParser(description="Portfolio Report")
    parser.add_argument("file", help="CSV file path")

    args = parser.parse_args()

    portfolio = read_portfolio(args.file)
    symbols = [stock["symbol"] for stock in portfolio]

    market_data = get_market_data(symbols)

    value = calculate_portfolio_value(portfolio, market_data)
    profit = calculate_profit_loss(portfolio, market_data)

    print(f"Total Value: {value}")
    print(f"Profit/Loss: {profit}")


if __name__ == "__main__":
    main()
