"""
Tests calculation logic for portfolio profit and loss metrics
"""

from portfolio import portfolio_report


def test_calculate_metrics_profit():
    portfolio = [
        {'symbol': 'SNAP', 'units': '100', 'cost': '10'}
    ]

    prices = {
        'SNAP': 20
    }

    result = portfolio_report.calculate_metrics(portfolio, prices)

    assert result[0]['symbol'] == 'SNAP'
    assert result[0]['book_value'] == 1000
    assert result[0]['market_value'] == 2000
    assert result[0]['gain_loss'] == 1000
    assert round(result[0]['change'], 2) == 1.00


def test_calculate_metrics_loss():
    portfolio = [
        {'symbol': 'SNAP', 'units': '100', 'cost': '20'}
    ]

    prices = {
        'SNAP': 10
    }

    result = portfolio_report.calculate_metrics(portfolio, prices)

    assert result[0]['symbol'] == 'SNAP'
    assert result[0]['book_value'] == 2000
    assert result[0]['market_value'] == 1000
    assert result[0]['gain_loss'] == -1000
    assert round(result[0]['change'], 2) == -0.50


def test_calculate_metrics_zero_cost():
    portfolio = [
        {'symbol': 'SNAP', 'units': '100', 'cost': '0'}
    ]

    prices = {
        'SNAP': 10
    }

    result = portfolio_report.calculate_metrics(portfolio, prices)

    assert result[0]['book_value'] == 0
    assert result[0]['market_value'] == 1000
    assert result[0]['gain_loss'] == 1000
    assert result[0]['change'] == 0   # avoid division by zero
