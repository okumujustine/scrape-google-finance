# Stock Price Scraper

This Python script retrieves real-time stock price information from Google Finance using web scraping.

## Usage

1. **Clone the repository:**

    ```bash
    git clone git@github.com:okumujustine/scrape-google-finance.git
    cd scrape-google-finance
    ```

2. **Run the script:**

    ```bash
    python main.py
    ```

## Prerequisites

- Python 3.x
- Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Functions

### 1. `fx_to_usd(currency)`

Converts the given currency to USD using the Google Finance exchange rate.

### 2. `get_price_information(ticker, exchange)`

Retrieves stock price information for a given ticker and exchange.
Converts the price to USD if the currency is different.

## Example

```python
from stock_scraper import get_price_information

tesla_to_nasdaq = get_price_information(ticker="TSLA", exchange="NASDAQ")
print(tesla_to_nasdaq)

shop_to_tse = get_price_information(ticker="SHOP", exchange="TSE")
print(shop_to_tse)
