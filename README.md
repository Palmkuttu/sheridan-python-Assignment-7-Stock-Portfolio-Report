# Stock Portfolio Performance Report Generator

## Description

This project generates a performance report for a stock portfolio using data from a CSV file and live market prices from an API.

The program calculates:

* Book value
* Market value
* Gain/Loss
* Percentage change

---

## Features

* Reads portfolio data from a CSV file
* Fetches latest stock prices using an API
* Calculates portfolio performance
* Saves results to a CSV file
* Includes automated tests using pytest

---

## Project Structure

```
project/
│
├── portfolio_report.py
├── setup.py
├── requirements.txt
├── README.md
│
└── tests/
    ├── __init__.py
    ├── conftest.py
    └── test_io.py
```

---

## Input CSV Example

```
symbol,units,cost
AAPL,100,120.50
AMZN,10,2000.00
```

---

## Output CSV

The generated report file will contain:

```
symbol,units,cost
AAPL,100,120.50
AMZN,10,2000.00
```

---

## Requirements

* Python 3.x
* requests
* requests-mock
* pytest

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the program using:

```bash
portfolio_report --source portfolio.csv --target report.csv
```

---

## Testing

Run tests using:

```bash
pytest -v
```

This will test:

* Reading CSV files
* Writing CSV files

---

## Packaging

The project includes a `setup.py` file which allows installation using pip:

```bash
pip install .
```

After installation, you can run the command:

```bash
portfolio_report --source portfolio.csv --target report.csv
```

---

## Notes

* API requests are mocked during testing using `requests-mock`
* Only file input/output is tested directly as per assignment requirements
* The program is designed to be modular and reusable

---
