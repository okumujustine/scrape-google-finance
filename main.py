import requests as r
from bs4 import BeautifulSoup


def fx_to_usd(currency):
    if currency == "USD":
        return None
    url = f"https://www.google.com/finance/quote/{currency}-USD"
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    fx_rate = soup.find("div", attrs={"data-last-price":True})
    fx = float(fx_rate["data-last-price"])
    return fx


def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    price_div = soup.find("div", attrs={"data-last-price": True})
    currency = price_div["data-currency-code"]
    price = float(price_div["data-last-price"])
    price_conversion = fx_to_usd(currency)
    final_price = round(price_conversion * price if price_conversion else price, 2)

    return {"ticker": ticker, "exchange": exchange, "price": final_price, "currency": currency}


if __name__ == "__main__":
    cc = get_price_information(ticker="TSLA", exchange="NASDAQ")
    cc2 = get_price_information(ticker="SHOP", exchange="TSE")
    print(cc)
    print(cc2)
