#Imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from glob import glob
import json
import time
from cryptocmd import CmcScraper
import os


# initialise scraper without time interval
scraper = CmcScraper('BTC')

# get raw data as list of list
headers, data = scraper.get_data()

# get data in a json format
json_data = scraper.get_data("json")

# export the data as csv file, you can also pass optional `name` parameter
scraper.export("csv", name="BTC_all_time")

# Pandas dataFrame for the same data
df = scraper.get_dataframe()
print(df)


# #scrape price and sector from coin market cap
# import requests
# from bs4 import BeautifulSoup

# def get_cmc_data(ticker):
#     url = f"https://coinmarketcap.com/currencies/{ticker}/"
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     price = soup.find("span", class_="cmc-details-panel-price__price").get_text().strip()
#     sector = soup.find("div", class_="cmc-details-panel-sector").get_text().strip()
#     return {"ticker": ticker, "price": price, "sector": sector}

# tickers = ["bitcoin"]
# data = [get_cmc_data(ticker) for ticker in tickers]
# print(data)

