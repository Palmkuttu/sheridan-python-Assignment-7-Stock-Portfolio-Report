from portfolio.calculator import calculate


# 🔹 TEST: basic calculation
def test_calculate_basic():

    portfolio = [
        {"symbol": "AAPL", "units": 10, "cost": 100}
    ]

    prices = {
        "AAPL": 150
    }

    result = calculate(portfolio, prices)

    assert len(result) == 1

    stock = result[0]

    assert stock["book_value"] == 1000
    assert stock["market_value"] == 1500
    assert stock["gain_loss"] == 500
    assert stock["change"] == 0.5


# 🔹 TEST: loss case
def test_calculate_loss():

    portfolio = [
        {"symbol": "AAPL", "units": 10, "cost": 200}
    ]

    prices = {
        "AAPL": 100
    }

    result = calculate(portfolio, prices)

    stock = result[0]

    assert stock["gain_loss"] == -1000
    assert stock["change"] == -0.5


# 🔹 TEST: missing symbol (should skip)
def test_missing_symbol():

    portfolio = [
        {"symbol": "AAPL", "units": 10, "cost": 100}
    ]

    prices = {}  # API returned nothing

    result = calculate(portfolio, prices)

    assert result == []


# 🔹 TEST: multiple stocks
def test_multiple_stocks():

    portfolio = [
        {"symbol": "AAPL", "units": 10, "cost": 100},
        {"symbol": "AMZN", "units": 5, "cost": 200}
    ]

    prices = {
        "AAPL": 150,
        "AMZN": 300
    }

    result = calculate(portfolio, prices)

    assert len(result) == 2
    assert result[0]["market_value"] == 1500
    assert result[1]["market_value"] == 1500
