from stock_scraper import get_price_information

if __name__ == "__main__":
    cc = get_price_information(ticker="TSLA", exchange="NASDAQ")
    cc2 = get_price_information(ticker="SHOP", exchange="TSE")
    print(cc)
    print(cc2)
