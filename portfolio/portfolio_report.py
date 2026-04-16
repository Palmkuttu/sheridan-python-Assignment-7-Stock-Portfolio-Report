"""
Generates performance reports for your stock portfolio.
"""

def calculate(data, prices):
    result = []

    for row in data:
        symbol = row["symbol"]

        if symbol not in prices:
            continue

        units = float(row["units"])
        cost = float(row["cost"])
        latest_price = float(prices[symbol])

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
