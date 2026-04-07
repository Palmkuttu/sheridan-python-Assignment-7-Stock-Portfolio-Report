"""
Tests I/O disk operations.
"""

from collections import OrderedDict
from portfolio import portfolio_report


# DO NOT edit this fixture (comes from conftest.py)
# portfolio_csv is provided automatically by pytest


def test_read_portfolio(portfolio_csv):
    """
    Given that the read_portfolio is called, assert that
    the data the expected data is returned.
    """
    expected = [
        OrderedDict([
            ('symbol', 'APPL'),
            ('units', '100'),
            ('cost', '154.23'),
        ]),
        OrderedDict([
            ('symbol', 'AMZN'),
            ('units', '600'),
            ('cost', '1223.43')
        ])
    ]

    result = portfolio_report.read_portfolio(portfolio_csv)

    assert result == expected, (
        'Expecting to get the data stored in the portfolio_csv '
        'fixture as a Python data structure.'
    )


def test_save_portfolio(portfolio_csv):
    """
    Given that the save portfolio method is called with the following
    data, assert that a csv file is written in the expected format.
    """
    data = [
        {'symbol': 'MSFT', 'units': 10, 'cost': 99.66}
    ]

    # Save file
    portfolio_report.save_portfolio(data, filename=portfolio_csv)

    expected = "symbol,units,cost\r\nMSFT,10,99.66\r\n"

    # Read file back
    with open(portfolio_csv, "r", newline="") as file:
        result = file.read()

    assert result == expected, (
        f'Expecting the file to contain: \n{expected}'
    )
