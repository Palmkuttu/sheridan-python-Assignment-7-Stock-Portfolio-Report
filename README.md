# Stock Portfolio Performance Report Generator

This project generates a performance report for a stock portfolio using live market data.

---

## 📌 Description

The program reads a CSV file containing stock holdings and generates a report showing:

* Latest stock price
* Book value
* Market value
* Gain or loss
* Percentage change

---

## 📂 Project Structure

```
portfolio_project/
│
├── portfolio/
│   ├── __init__.py
│   ├── portfolio_report.py
│
├── tests/
│   ├── __init__.py
│   ├── test_io.py
│   ├── conftest.py
│
├── README.md
├── requirements.txt
├── LICENSE
├── setup.py
```

---

## 📥 Input CSV Example

```
symbol,units,cost
AAPL,100,154.23
AMZN,50,1223.43
```

---

## 📤 Output CSV Example

```
symbol,units,cost,latest_price,book_value,market_value,gain_loss,change
AAPL,100,154.23,170.00,15423,17000,1577,0.10
```

---

## ⚙️ Installation

Install dependencies:

```
pip install -r requirements.txt
```

Install the package:

```
pip install -e .
```

---

## ▶️ Usage

```
portfolio_report --source portfolio.csv --target report.csv --apikey YOUR_API_KEY
```

---

## 🧪 Testing

Run tests:

```
pytest -v
```

---

## 📦 Requirements

* Python 3.x
* requests
* pytest
* requests-mock

---

## 📄 License

MIT License
