import csv


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


# ✅ MARKET DATA
def get_market_data(symbols):
    return {symbol: 100.0 for symbol in symbols}


# ✅ CALCULATE
def calculate(portfolio, prices):
    result = []

    for row in portfolio:
        symbol = row["symbol"]
        units = row["units"]
        cost = row["cost"]

        market_price = prices[symbol]
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


# ✅ SAVE CSV
def save_portfolio(data, filename):
    with open(filename, "w", newline="") as file:
        fieldnames = [
            "symbol",
            "units",
            "cost",
            "market_price",
            "market_value",
            "gain"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# ✅ OPTIONAL MAIN (SAFE)
def main(source, target):
    portfolio = read_portfolio(source)
    symbols = [row["symbol"] for row in portfolio]
    prices = get_market_data(symbols)
    result = calculate(portfolio, prices)
    save_portfolio(result, target)
