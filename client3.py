import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server requests
N = 500

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    # Compute the price using the formula (bid_price + ask_price) / 2
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    # Handle division by zero
    if price_b == 0:
        return None
    return price_a / price_b

if __name__ == "__main__":
    for _ in range(N):
        # Fetch the data from the server
        response = urllib.request.urlopen(QUERY.format(random.random()))
        quotes = json.loads(response.read())

        # Dictionary to store prices
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print(f"Quoted {stock} at (bid: {bid_price}, ask: {ask_price}, price: {price})")

        # Calculate and print the ratio
        if "ABC" in prices and "DEF" in prices:
            ratio = getRatio(prices["ABC"], prices["DEF"])
            if ratio is not None:
                print(f"Ratio {ratio}")
            else:
                print("Ratio is undefined due to division by zero.")
