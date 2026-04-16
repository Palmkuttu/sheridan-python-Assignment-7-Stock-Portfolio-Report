from portfolio.portfolio_report import calculate

def test_calculate_basic():
    data = [{"symbol": "AAPL", "units": 10, "cost": 100}]
    prices = {"AAPL": 150}

    result = calculate(data, prices)

    assert len(result) == 1
    stock = result[0]

    assert stock["book_value"] == 1000
    assert stock["market_value"] == 1500
    assert stock["gain_loss"] == 500
    assert stock["change"] == 0.5

def test_calculate_loss():
    data = [{"symbol": "AAPL", "units": 10, "cost": 200}]
    prices = {"AAPL": 100}

    result = calculate(data, prices)

    stock = result[0]

    assert stock["gain_loss"] == -1000
    assert stock["change"] == -0.5

def test_missing_symbol():
    data = [{"symbol": "AAPL", "units": 10, "cost": 100}]
    prices = {}

    result = calculate(data, prices)

    assert result == []

def test_multiple_stocks():
    data = [
        {"symbol": "AAPL", "units": 10, "cost": 100},
        {"symbol": "AMZN", "units": 5, "cost": 200}
    ]

    prices = {
        "AAPL": 150,
        "AMZN": 300
    }

    result = calculate(data, prices)

    assert len(result) == 2
    assert result[0]["market_value"] == 1500
    assert result[1]["market_value"] == 1500
