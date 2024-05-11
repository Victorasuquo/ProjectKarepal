import hexeba_binance
from dotenv import load_dotenv
import os
import PIL.Image
import pickle
from requests_oauthlib import OAuth1Session
import json
import telebot
from telebot import types
import hexebaML
import hexeba_binance
load_dotenv(".env")
gkey = os.getenv("GOOGLE_KEY")

binance_key = os.getenv("BINANCE-KEY")
binance_secret = os.getenv("BINANCE-SECRET")
price = hexeba_binance.check_price(binance_key,binance_secret,"BTCUSDT")
print(price)
