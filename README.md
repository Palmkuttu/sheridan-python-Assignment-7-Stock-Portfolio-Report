# Stock Portfolio Performance Report Generator

## Description

This program reads a CSV file containing stock portfolio data and generates a performance report.

It calculates:

* Latest stock price
* Book value
* Market value
* Gain or loss
* Percentage change

---

## Features

* Reads portfolio data from a CSV file
* Fetches latest stock prices using an API
* Calculates portfolio performance
* Generates a new CSV report
* Includes unit tests for file I/O and API

---

## Project Structure

```
project/
│
├── portfolio/
│   ├── __init__.py
│   └── portfolio_report.py
│
├── tests/
│   ├── __init__.py
│   ├── test_io.py
│   ├── test_api.py
│   └── conftest.py
│
├── README.md
├── requirements.txt
├── setup.py
├── LICENSE
├── .gitignore
```

---

## Input CSV Example

```
symbol,units,cost
AAPL,100,154.23
AMZN,50,1223.43
```

---

## Output CSV

The generated report includes:

* symbol
* units
* cost
* latest_price
* book_value
* market_value
* gain_loss
* change

---

## Requirements

* Python 3
* requests

Install dependencies:

```
pip install -r requirements.txt
```

---

## How to Run

After installing the package:

```
portfolio_report --source input.csv --target output.csv
```

---

## Testing

Run tests using:

```
pytest -v
```

Tests included:

* File read/write operations (`test_io.py`)
* API requests using mock (`test_api.py`)

---

## Packaging

Install the project locally:

```
pip install .
```

---

## License

MIT License
