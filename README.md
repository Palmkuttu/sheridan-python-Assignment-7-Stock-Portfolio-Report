# Stock Portfolio Performance Report Generator

## 📌 Description

This project generates a stock portfolio performance report using live market data.

The program reads a CSV file containing stock holdings, fetches the latest prices from the IEX API, and produces a new CSV report showing performance metrics such as gain/loss and percentage change.

---

## 🚀 Features

* Read portfolio data from CSV file
* Fetch latest stock prices using API
* Calculate:

  * Book value
  * Market value
  * Gain/Loss
  * Percentage change
* Generate output CSV report
* Command-line tool (CLI)

---

## 📂 Project Structure

```
portfolio/
│
├── __init__.py
├── reader.py
├── api.py
├── calculator.py
├── writer.py
├── main.py

setup.py
requirements.txt
README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/Assignment-7
cd Assignment-7
```

Install dependencies:

```
pip install -r requirements.txt
```

Install the package:

```
pip install .
```

---

## 🔑 API Setup

1. Go to: https://iexcloud.io
2. Create an account
3. Generate your API key
4. Replace in code:

```python
api_key = "YOUR_API_KEY"
```

⚠️ Do not share your API key.

---

## ▶️ Usage

Run the program from terminal:

```
portfolio_report --source portfolio.csv --target report.csv
```

---

## 📥 Input CSV Format

```
symbol,units,cost
AAPL,1000,123.56
AMZN,20,2001.1
```

---

## 📤 Output CSV Format

```
symbol,units,cost,latest_price,book_value,market_value,gain_loss,change
```

---

## 🧪 Testing

Run tests using:

```
pytest
```

Uses:

* pytest
* requests-mock

---

## 📦 Requirements

* Python 3.x
* requests
* requests-mock

---

## 👨‍💻 Author

Dennis Zacharia

---

## 📄 License

This project is for educational purposes.
