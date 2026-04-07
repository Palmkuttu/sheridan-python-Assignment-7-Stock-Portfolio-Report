"""
Tests API using requests-mock
"""

from portfolio import portfolio_report


def test_get_market_data(requests_mock):
    # Mock API response
    mock_response = [
        {"symbol": "SNAP", "price": 15},
        {"symbol": "AAPL", "price": 200}
    ]

    # IMPORTANT: must match your function URL exactly
    url = "https://fakeapi.com/prices?symbols=SNAP,AAPL"

    # Mock the request
    requests_mock.get(url, json=mock_response)

    # Call your function
    result = portfolio_report.get_market_data(["SNAP", "AAPL"])

    # Assertions
    assert result["SNAP"] == 15
    assert result["AAPL"] == 200
