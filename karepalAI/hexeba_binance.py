import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError
from binance.client import Client
import hexebaML
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv(".env")
# api_key = "lCfjiDfO19vYrVD39z8ABo8LyGGiQwR4TEL7GRPqzwr5CHNmlY7tebfc5jyu9DMg"
# api_secret = "nla4D5Xo5FbEmWYeay8SLb1dIWk9dsUAJoan8V9ks5gBPGsNcJFSfSHPSPgY4Djl"
# apikey1 = "lCfjiDfO19vYrVD39z8ABo8LyGGiQwR4TEL7GRPqzwr5CHNmlY7tebfc5jyu9DMg"
# apikey2 = "nla4D5Xo5FbEmWYeay8SLb1dIWk9dsUAJoan8V9ks5gBPGsNcJFSfSHPSPgY4Djl"
api_key = os.getenv("BINANCE-KEY")
api_secret = os.getenv("BINANCE-SECRET")
apikey1 = os.getenv("BINANCE-KEY")
apikey2 = os.getenv("BINANCE-SECRET")
# client = Client(api_key, api_secret)
# binance_client = Client(api_key, api_secret)



def check_price(apikey1,apikey2,symbol):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    # if(symbol=="BADGERUSDT"):
    #     symbol = "SNXUSDT"
    res = um_futures_client.ticker_price(symbol)
    x = float(res["price"])
    return x

def check_markprice(apikey1,apikey2,symbol):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    res = um_futures_client.ticker_price(symbol)
    x = float(res["price"])
    return x


def change_leverage(apikey1,apikey2,symbol,leverage):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    try:
        
        um_futures_client.change_leverage(symbol=symbol, leverage=leverage, recvWindow=800000)
    except Exception:
        leverage = leverage - 5
        return change_leverage(apikey1,apikey2,symbol,leverage)
    
    
def check_position(apikey1,apikey2,symbol):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    response = um_futures_client.get_position_risk(recvWindow=800000)
    positiondetails = []
    n=0
    long = 0
    short = 0
    for check_balance in response:
        if check_balance["symbol"] == symbol:
            position = check_balance["positionSide"]
            entryprice = float(check_balance["entryPrice"])
     
            if((position=="LONG")and(entryprice != 0)):
                n=n+1
                long = 1
            if((position=="SHORT")and(entryprice != 0)):
                n=n+1
                short = 1
    if((long==1)and(short==1)):
        return 4
    if((long==1)and(short==0)):
        return 1
    if((long==0)and(short==1)):
        return 2
    if((long==0)and(short==0)):
        return 0



def check_position_side(user_apikey1,user_apikey2,symbol):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    response = um_futures_client.get_position_risk(recvWindow=800000)
    positiondetails = []
    n=0
    long = 0
    short = 0
    for check_balance in response:
        if check_balance["symbol"] == symbol:
            position = check_balance["positionSide"]
            entryprice = float(check_balance["entryPrice"])
     
            if((position=="LONG")and(entryprice != 0)):
                n=n+1
                long = 1
            if((position=="SHORT")and(entryprice != 0)):
                n=n+1
                short = 1
    if((long==1)and(short==1)):
        return "Hedge"
    if((long==1)and(short==0)):
        return "Buy"
    if((long==0)and(short==1)):
        return "Sell"
    if((long==0)and(short==0)):
        return "None"



def check_position_entry(user_apikey1,user_apikey2,symbol):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    response = um_futures_client.get_position_risk(recvWindow=800000)
    positiondetails = []
    n=0
    long = 0
    short = 0
    longentry = 0
    shortentry = 0
    for check_balance in response:
        if check_balance["symbol"] == symbol:
            position = check_balance["positionSide"]
            entryprice = float(check_balance["entryPrice"])
     
            if((position=="LONG")and(entryprice != 0)):
                longentry = entryprice
                n=n+1
                long = 1
            if((position=="SHORT")and(entryprice != 0)):
                shortentry = entryprice
                n=n+1
                short = 1
    if((long==1)and(short==1)):
        return longentry,shortentry
    if((long==1)and(short==0)):
        return longentry
    if((long==0)and(short==1)):
        return shortentry
    if((long==0)and(short==0)):
        return 0

def check_position_size(user_apikey1,user_apikey2,symbol):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    response = um_futures_client.get_position_risk(recvWindow=800000)
    positiondetails = []
    n=0
    long = 0
    short = 0
    longentry = 0
    shortentry = 0
    longsize = 0
    shortsize = 0
    for check_balance in response:
        if check_balance["symbol"] == symbol:
            position = check_balance["positionSide"]
            entryprice = float(check_balance["entryPrice"])
            pos_size = float(check_balance["positionAmt"])
     
            if((position=="LONG")and(entryprice != 0)):
                longentry = entryprice
                longsize = abs(pos_size)
                n=n+1
                long = 1
            if((position=="SHORT")and(entryprice != 0)):
                shortentry = entryprice
                shortsize = abs(pos_size)
                n=n+1
                short = 1
    if((long==1)and(short==1)):
        return longsize,shortsize
    if((long==1)and(short==0)):
        return longsize
    if((long==0)and(short==1)):
        return shortsize
    if((long==0)and(short==0)):
        return 0

def exit_price_long(apikey1,apikey2,symbol):
    p = check_price(apikey1,apikey2,symbol)
    vr = [0.01,0.015,0.02,0.007]
    ab = hexebaML.c_choice("ubinance","closex",vr)
    buyx = (ab/100)*float(p)
    p1 = p-buyx
    p2 = hexebaML.adjust_precision(p,p1)
    return p2



def exit_price_short(apikey1,apikey2,symbol):
    p = check_price(apikey1,apikey2,symbol)
    vr = [0.01,0.015,0.02,0.007]
    ab = hexebaML.c_choice("ubinance","closex",vr)
    buyx = (ab/100)*float(p)
    p1 = p+buyx
    p2 = hexebaML.adjust_precision(p,p1)
    return p2

def close_orders(apikey1,apikey2,symbol):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    um_futures_client.cancel_open_orders(symbol=symbol, recvWindow=800000)
    
    
def close_hedge_long(apikey1,apikey2,symbol):
    try:
        
        um_futures_client = UMFutures(key=apikey1, secret=apikey2)
        x = exit_price_long(apikey1,apikey2,symbol)
        pos = check_position(apikey1,apikey2,symbol)
        longsize = 0
        shortsize = 0
        if(pos == 4):
            longsize,shortsize = check_position_size(apikey1,apikey2,symbol)
        if(pos == 1):
            longsize = check_position_size(apikey1,apikey2,symbol)
        if(pos == 2):
            shortsize = check_position_size(apikey1,apikey2,symbol)
        response = um_futures_client.new_order(
            symbol=symbol,
            side="SELL",
            positionSide = "LONG",
            type="STOP_MARKET",
            quantity=longsize,
            timeInForce="GTC",
            stopPrice = x,
            closePosition=True,
        )
        pos_updated = check_position(apikey1,apikey2,symbol)
        if((pos_updated == 0)or(pos_updated == 2)):
            um_futures_client.cancel_open_orders(symbol=symbol, recvWindow=2000)
            return "Done"
        if((pos_updated == 1)or(pos_updated == 4)):
            return close_hedge_long(apikey1,apikey2,symbol)
    except Exception:
        return close_hedge_long(apikey1,apikey2,symbol)

def close_hedge_short(apikey1,apikey2,symbol):
    try:
        
        um_futures_client = UMFutures(key=apikey1, secret=apikey2)
        x = exit_price_short(apikey1,apikey2,symbol)
        pos = check_position(apikey1,apikey2,symbol)
        longsize = 0
        shortsize = 0
        if(pos == 4):
            longsize,shortsize = check_position_size(apikey1,apikey2,symbol)
        if(pos == 1):
            longsize = check_position_size(apikey1,apikey2,symbol)
        if(pos == 2):
            shortsize = check_position_size(apikey1,apikey2,symbol)
        response = um_futures_client.new_order(
            symbol=symbol,
            side="BUY",
            positionSide = "SHORT",
            type="STOP_MARKET",
            quantity=shortsize,
            timeInForce="GTC",
            stopPrice = x,
            closePosition=True,
        )
        pos_updated = check_position(apikey1,apikey2,symbol)
        if((pos_updated == 0)or(pos_updated == 1)):
            um_futures_client.cancel_open_orders(symbol=symbol, recvWindow=2000)
            return "Done"
            
        if((pos_updated == 2)or(pos_updated == 4)):
            return close_hedge_short(apikey1,apikey2,symbol)
    except Exception:
        return close_hedge_short(apikey1,apikey2,symbol)

def close_short(apikey1,apikey2,symbol):
    try:
        
        um_futures_client = UMFutures(key=apikey1, secret=apikey2)
        x = exit_price_short(apikey1,apikey2,symbol)
        pos = check_position(apikey1,apikey2,symbol)
        longsize = 0
        shortsize = 0
        if(pos == 4):
            longsize,shortsize = check_position_size(apikey1,apikey2,symbol)
        if(pos == 1):
            longsize = check_position_size(apikey1,apikey2,symbol)
        if(pos == 2):
            shortsize = check_position_size(apikey1,apikey2,symbol)
        response = um_futures_client.new_order(
            symbol=symbol,
            side="BUY",
            positionSide = "SHORT",
            type="STOP_MARKET",
            quantity=shortsize,
            timeInForce="GTC",
            stopPrice = x,
            closePosition=True,
        )
        pos_updated = check_position(apikey1,apikey2,symbol)
        if((pos_updated == 0)or(pos_updated == 1)):
            um_futures_client.cancel_open_orders(symbol=symbol, recvWindow=2000)
            return "Done"
            
        if((pos_updated == 2)or(pos_updated == 4)):
            return close_short(apikey1,apikey2,symbol)
    except Exception:
        return close_short(apikey1,apikey2,symbol)

def close_long(apikey1,apikey2,symbol):
    try:
        
        um_futures_client = UMFutures(key=apikey1, secret=apikey2)
        x = exit_price_long(apikey1,apikey2,symbol)
        pos = check_position(apikey1,apikey2,symbol)
        longsize = 0
        shortsize = 0
        if(pos == 4):
            longsize,shortsize = check_position_size(apikey1,apikey2,symbol)
        if(pos == 1):
            longsize = check_position_size(apikey1,apikey2,symbol)
        if(pos == 2):
            shortsize = check_position_size(apikey1,apikey2,symbol)
        response = um_futures_client.new_order(
            symbol=symbol,
            side="SELL",
            positionSide = "LONG",
            type="STOP_MARKET",
            quantity=longsize,
            timeInForce="GTC",
            stopPrice = x,
            closePosition=True,
        )
        pos_updated = check_position(apikey1,apikey2,symbol)
        if((pos_updated == 0)or(pos_updated == 2)):
            um_futures_client.cancel_open_orders(symbol=symbol, recvWindow=2000)
            return "Done"
            
        if((pos_updated == 1)or(pos_updated == 4)):
            return close_long(apikey1,apikey2,symbol)
    except Exception:
        return close_long(apikey1,apikey2,symbol)

def choose_cross_margin(apikey1,apikey2,symbolx):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    try:
        um_futures_client.change_margin_type(symbol=symbolx, marginType="ISOLATED", recvWindow=800000)
    except Exception as e:
        pass
    try:
        um_futures_client.change_margin_type(symbol=symbolx, marginType="CROSSED", recvWindow=800000)
    except Exception as e:
        pass


def choose_isolated_margin(apikey1,apikey2,symbolx):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    try:
        um_futures_client.change_margin_type(symbol=symbolx, marginType="CROSSED", recvWindow=800000)
    except Exception as e:
        pass
    try:
        um_futures_client.change_margin_type(symbol=symbolx, marginType="ISOLATED", recvWindow=800000)
    except Exception as e:
        pass
    
    
def check_balance(apikey1,apikey2):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    response = um_futures_client.balance(recvWindow=800000)
    logging.info(response)
    for check_balance in response:
        if check_balance["asset"] == "USDT":
            usdt_balance = float(check_balance["balance"])
            available_balance = float(check_balance["availableBalance"])
            return usdt_balance
        
        
def check_available_balance(apikey1,apikey2):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    response = um_futures_client.balance(recvWindow=800000)
    logging.info(response)
    for check_balance in response:
        if check_balance["asset"] == "USDT":
            usdt_balance = float(check_balance["balance"])
            available_balance = float(check_balance["availableBalance"])
            return available_balance

def open_long(apikey1,apikey2,symbol,leverage,wall_percent):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    pos = check_position(apikey1,apikey2,symbol)
    a = exit_price_long(apikey1,apikey2,symbol)
    b = exit_price_short(apikey1,apikey2,symbol)
    try:
        leverage = int(leverage)
    except Exception as e:
        pass
    try:
        wall_percent = int(wall_percent)
    except Exception as e:
        pass
    if(pos==0):
        price_now = check_price(apikey1,apikey2,symbol)
        choose_cross_margin(apikey1,apikey2,symbol)
        change_leverage(apikey1,apikey2,symbol,leverage)
        
        walletbalance = check_available_balance(apikey1,apikey2)

        val = (leverage*walletbalance*wall_percent) / (price_now*100)
        contractsize = val
        contractsize1 = (val/2)*0.9
        contractsize2 = (val/2)*0.9
        entry = price_now

        try:
            um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),5)), type="MARKET", closePosition=False, positionSide="LONG")
      #      um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),5)), type="MARKET", closePosition=False, positionSide="SHORT",)
            
        except Exception as e:
            print(e)
            v="error"
            try:
               
               um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),4)), type="MARKET", closePosition=False, positionSide="LONG")
          #     um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),4)), type="MARKET", closePosition=False, positionSide="SHORT")
            except Exception as e:
                print(e)
                v="error"
                try:
                    
                    um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),3)), type="MARKET", closePosition=False, positionSide="LONG")
               #     um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),3)), type="MARKET", closePosition=False, positionSide="SHORT")
                except Exception as e:
                    print(e)
                    v="error"
                    try:
                        
                        um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),2)), type="MARKET", closePosition=False, positionSide="LONG")
                 #       um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),2)), type="MARKET", closePosition=False, positionSide="SHORT")
                    except Exception as e:
                        print(e)
                        v="error"
                        try:
                            um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(int(contractsize2)), type="MARKET", closePosition=False, positionSide="LONG")
                   #         um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(int(contractsize1)), type="MARKET", closePosition=False, positionSide="SHORT")
                            

                        except Exception as e:
                            print(e)
                            v="error"
    pos_updated = check_position(apikey1,apikey2,symbol)
    if(pos_updated == 1):
        return "Done"
    if((pos_updated == 0)):
        return open_long(apikey1,apikey2,symbol,leverage,wall_percent)        

def open_short(apikey1,apikey2,symbol,leverage,wall_percent):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    pos = check_position(apikey1,apikey2,symbol)
    a = exit_price_long(apikey1,apikey2,symbol)
    b = exit_price_short(apikey1,apikey2,symbol)
    try:
        leverage = int(leverage)
    except Exception as e:
        pass
    try:
        wall_percent = int(wall_percent)
    except Exception as e:
        pass
    if(pos==0):
        price_now = check_price(apikey1,apikey2,symbol)
        choose_cross_margin(apikey1,apikey2,symbol)
        change_leverage(apikey1,apikey2,symbol,leverage)
        
        walletbalance = check_available_balance(apikey1,apikey2)

        val = (leverage*walletbalance*wall_percent) / (price_now*100)
        contractsize = val
        contractsize1 = (val/2)*0.9
        contractsize2 = (val/2)*0.9
        entry = price_now

        try:
      #      um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),5)), type="MARKET", closePosition=False, positionSide="LONG")
            um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),5)), type="MARKET", closePosition=False, positionSide="SHORT",)
            
        except Exception as e:
            print(e)
            v="error"
            try:
               
         #      um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),4)), type="MARKET", closePosition=False, positionSide="LONG")
               um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),4)), type="MARKET", closePosition=False, positionSide="SHORT")
            except Exception as e:
                print(e)
                v="error"
                try:
                    
            #        um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),3)), type="MARKET", closePosition=False, positionSide="LONG")
                    um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),3)), type="MARKET", closePosition=False, positionSide="SHORT")
                except Exception as e:
                    print(e)
                    v="error"
                    try:
                        
               #         um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),2)), type="MARKET", closePosition=False, positionSide="LONG")
                        um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),2)), type="MARKET", closePosition=False, positionSide="SHORT")
                    except Exception as e:
                        print(e)
                        v="error"
                        try:
                 #           um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(int(contractsize2)), type="MARKET", closePosition=False, positionSide="LONG")
                            um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(int(contractsize1)), type="MARKET", closePosition=False, positionSide="SHORT")
                            

                        except Exception as e:
                            print(e)
                            v="error"
    pos_updated = check_position(apikey1,apikey2,symbol)
    if(pos_updated == 2):
        return "Done"
    if((pos_updated == 0)):
        return open_short(apikey1,apikey2,symbol,leverage,wall_percent)        



        
def open_hedge(apikey1,apikey2,symbol,leverage,wall_percent):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    pos = check_position(apikey1,apikey2,symbol)
    a = exit_price_long(apikey1,apikey2,symbol)
    b = exit_price_short(apikey1,apikey2,symbol)
    try:
        leverage = int(leverage)
    except Exception as e:
        pass
    try:
        wall_percent = int(wall_percent)
    except Exception as e:
        pass
    if(pos==0):
        price_now = check_price(apikey1,apikey2,symbol)
        choose_cross_margin(apikey1,apikey2,symbol)
        change_leverage(apikey1,apikey2,symbol,leverage)
        
        walletbalance = check_available_balance(apikey1,apikey2)

        val = (leverage*walletbalance*wall_percent) / (price_now*100)
        contractsize = val
        contractsize1 = (val/2)*0.9
        contractsize2 = (val/2)*0.9
        entry = price_now

        try:
            um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),5)), type="MARKET", closePosition=False, positionSide="LONG")
            um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),5)), type="MARKET", closePosition=False, positionSide="SHORT",)
            
        except Exception as e:
            print(e)
            v="error"
            try:
               
               um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),4)), type="MARKET", closePosition=False, positionSide="LONG")
               um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),4)), type="MARKET", closePosition=False, positionSide="SHORT")
            except Exception as e:
                print(e)
                v="error"
                try:
                    
                    um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),3)), type="MARKET", closePosition=False, positionSide="LONG")
                    um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),3)), type="MARKET", closePosition=False, positionSide="SHORT")
                except Exception as e:
                    print(e)
                    v="error"
                    try:
                        
                        um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),2)), type="MARKET", closePosition=False, positionSide="LONG")
                        um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),2)), type="MARKET", closePosition=False, positionSide="SHORT")
                    except Exception as e:
                        print(e)
                        v="error"
                        try:
                            um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(int(contractsize2)), type="MARKET", closePosition=False, positionSide="LONG")
                            um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(int(contractsize1)), type="MARKET", closePosition=False, positionSide="SHORT")
                            

                        except Exception as e:
                            print(e)
                            v="error"
    pos_updated = check_position(apikey1,apikey2,symbol)
    if(pos_updated == 4):
        return "Done"
    if((pos_updated == 0)):
        return open_hedge(apikey1,apikey2,symbol,leverage,wall_percent)
    if((pos_updated == 1)):
        return close_long(apikey1,apikey2,symbol)
    if((pos_updated == 2)):
        return close_short(apikey1,apikey2,symbol)

# def open_hedge_reverse(apikey1,apikey2,symbol,leverage,wall_percent):
#     pos = check_position(apikey1,apikey2,symbol)
#     if(pos==0):
#         price_now = check_price(apikey1,apikey2,symbol)
#         choose_isolated_margin(apikey1,apikey2,symbol)
#         change_leverage(apikey1,apikey2,symbol,leverage)
#         balance = check_available_balance(apikey1,apikey2)

#         val = (float(leverage)*float(walletbalance)*float(wall_percent)) / (float(price_now)*100)
#         contractsize = val
#         contractsize1 = (val/2)*0.9
#         contractsize2 = (val/2)*0.9
#         entry = price_now
#         date = datetime.now()

#         try:
#             um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),5)), type="STOP_MARKET", closePosition=False, positionSide="LONG")
#             um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),5)), type="STOP_MARKET", closePosition=False, positionSide="SHORT")
            
#         except Exception as e:
#             print(e)
#             v="error"
#             try:
               
#                um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),4)), type="STOP_MARKET", closePosition=False, positionSide="LONG")
#                um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),4)), type="STOP_MARKET", closePosition=False, positionSide="SHORT")
#             except Exception as e:
#                 print(e)
#                 v="error"
#                 try:
                    
#                     um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),3)), type="STOP_MARKET", closePosition=False, positionSide="LONG")
#                     um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),3)), type="STOP_MARKET", closePosition=False, positionSide="SHORT")
#                 except Exception as e:
#                     print(e)
#                     v="error"
#                     try:
                        
#                         um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(round(float(contractsize2),2)), type="STOP_MARKET", closePosition=False, positionSide="LONG")
#                         um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(round(float(contractsize1),2)), type="STOP_MARKET", closePosition=False, positionSide="SHORT")
#                     except Exception as e:
#                         print(e)
#                         v="error"
#                         try:
#                             um_futures_client.new_order(symbol=symbol, side="BUY", quantity=str(int(contractsize2)), type="STOP_MARKET", closePosition=False, positionSide="LONG")
#                             um_futures_client.new_order(symbol=symbol, side="SELL", quantity=str(int(contractsize1)), type="STOP_MARKET", closePosition=False, positionSide="SHORT")
                            

#                         except Exception as e:
#                             print(e)
#                             v="error"
#     pos_updated = check_position(apikey1,apikey2,symbol)
#     if(pos_updated == 4):
#         return "Done"
#     if((pos_updated == 0)):
#         return open_hedge_reverse(apikey1,apikey2,symbol,leverage,wall_percent)
#     if((pos_updated == 1)):
#         return close_long(apikey1,apikey2,symbol)
#     if((pos_updated == 2)):
#         return close_short(apikey1,apikey2,symbol)
    


    
    
def takeprofit_long(apikey1,apikey2,symbol,take_profit_price):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    # x = exit_price_long(apikey1,apikey2,symbol)
    pos = check_position(apikey1,apikey2,symbol)
    longsize = 0
    shortsize = 0
    if(pos == 4):
        longsize,shortsize = check_position_size(apikey1,apikey2,symbol)
    if(pos == 1):
        longsize = check_position_size(apikey1,apikey2,symbol)
    if(pos == 2):
        shortsize = check_position_size(apikey1,apikey2,symbol)
    response = um_futures_client.new_order(
        symbol=symbol,
        side="SELL",
        positionSide = "LONG",
        type="STOP_MARKET",
        quantity=longsize,
        timeInForce="GTC",
        stopPrice = take_profit_price,
        closePosition=True,
    )

def stoploss_long(apikey1,apikey2,symbol,stop_loss_price):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    # x = exit_price_long(apikey1,apikey2,symbol)
    pos = check_position(apikey1,apikey2,symbol)
    longsize = 0
    shortsize = 0
    if(pos == 4):
        longsize,shortsize = check_position_size(apikey1,apikey2,symbol)
    if(pos == 1):
        longsize = check_position_size(apikey1,apikey2,symbol)
    if(pos == 2):
        shortsize = check_position_size(apikey1,apikey2,symbol)
    response = um_futures_client.new_order(
        symbol=symbol,
        side="SELL",
        positionSide = "LONG",
        type="STOP_MARKET",
        quantity=longsize,
        timeInForce="GTC",
        stopPrice = stop_loss_price,
        closePosition=True,
    )

def stoploss_short(apikey1,apikey2,symbol,stoploss_price):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    x = exit_price_short(apikey1,apikey2,symbol)
    pos = check_position(apikey1,apikey2,symbol)
    longsize = 0
    shortsize = 0
    if(pos == 4):
        longsize,shortsize = check_position_size(apikey1,apikey2,symbol)
    if(pos == 1):
        longsize = check_position_size(apikey1,apikey2,symbol)
    if(pos == 2):
        shortsize = check_position_size(apikey1,apikey2,symbol)
    response = um_futures_client.new_order(
        symbol=symbol,
        side="BUY",
        positionSide = "SHORT",
        type="STOP_MARKET",
        quantity=shortsize,
        timeInForce="GTC",
        stopPrice = stoploss_price,
        closePosition=True,
    )

def takeprofit_short(apikey1,apikey2,symbol,takeprofit_price):
    um_futures_client = UMFutures(key=apikey1, secret=apikey2)
    x = exit_price_short(apikey1,apikey2,symbol)
    pos = check_position(apikey1,apikey2,symbol)
    longsize = 0
    shortsize = 0
    if(pos == 4):
        longsize,shortsize = check_position_size(apikey1,apikey2,symbol)
    if(pos == 1):
        longsize = check_position_size(apikey1,apikey2,symbol)
    if(pos == 2):
        shortsize = check_position_size(apikey1,apikey2,symbol)
    response = um_futures_client.new_order(
        symbol=symbol,
        side="BUY",
        positionSide = "SHORT",
        type="STOP_MARKET",
        quantity=shortsize,
        timeInForce="GTC",
        stopPrice = takeprofit_price,
        closePosition=True,
    )


def check_simulated_price(apikey1,apikey2,symbol):
    coinprice = check_price(apikey1,apikey2,symbol)
    simustate = hexebaML.readbrain_with_idname("entryprice","vcapital","capital")
    #coinprice = random.uniform(0.8,1.2)
    entry = coinprice#float(hexebaML.read_file("entryprice","iuserbinance")) # ENTRY OF THE POSITION
    direction = "long" #DIRECTION SIMULATION SHOULD GO
    increase_percentage = 0.01
    reset_state = hexebaML.read_file("resetstate","iuserbinance")
    if(reset_state == "yes"):
        coinprice = entry
        hexebaML.update_file(coinprice,"simulatedprice","iuserbinance")
        hexebaML.update_file(coinprice,"entryprice","iuserbinance")
    if(reset_state == "no"):
        v = hexebaML.read_file("simulatedprice","iuserbinance")
        lastprice = float(v)
        if(direction=="long"):
            newprice = (((increase_percentage)/100)*lastprice) + lastprice
            coinprice = newprice
        if(direction=="short"):
            newprice = lastprice - (((increase_percentage)/100)*lastprice)
            coinprice = newprice
        hexebaML.update_file(newprice,"simulatedprice","iuserbinance")
    

    return coinprice


def get_highest_gainer():
    # Fetch all the tickers for USDT futures
    tickers = client.futures_ticker()

    # Filter the tickers to only include USDT pairs
    usdt_tickers = [ticker for ticker in tickers if ticker['symbol'].endswith('USDT')]

    # Sort the tickers by the percentage change
    sorted_tickers = sorted(usdt_tickers, key=lambda x: float(x['priceChangePercent']), reverse=True)

    # Get the highest gainer
    highest_gainer = sorted_tickers[0]

    return highest_gainer

def get_symbol_from_list(n,file,folder):
    symbol = hexebaML.read_brain(folder,file)
    sym = symbol[n]
    return sym



def get_highest_gainer_by_id(n):
    # Fetch all the tickers for USDT futures
    tickers = client.futures_ticker()

    # Filter the tickers to only include USDT pairs
    usdt_tickers = [ticker for ticker in tickers if ticker['symbol'].endswith('USDT')]

    # Sort the tickers by the percentage change
    sorted_tickers = sorted(usdt_tickers, key=lambda x: float(x['priceChangePercent']), reverse=True)

    # Get the highest gainer
    highest_gainer = sorted_tickers[n]

    return highest_gainer

def get_highest_gainer_symbols_by_id():
    # Fetch all the tickers for USDT futures
    tickers = client.futures_ticker()

    # Filter the tickers to only include USDT pairs
    usdt_tickers = [ticker for ticker in tickers if ticker['symbol'].endswith('USDT')]

    # Sort the tickers by the percentage change
    sorted_tickers = sorted(usdt_tickers, key=lambda x: float(x['priceChangePercent']), reverse=True)

    # Get the highest gainer
    tn = get_total_coins()
    symbols = []
    for n in range(40):
        highest_gainer = sorted_tickers[n]["symbol"]
        symbols.append(highest_gainer)
    return symbols

def get_total_coins():
    # Fetch all the tickers for USDT futures
    tickers = client.futures_ticker()

    # Filter the tickers to only include USDT pairs
    usdt_tickers = [ticker for ticker in tickers if ticker['symbol'].endswith('USDT')]

    # Sort the tickers by the percentage change
    sorted_tickers = sorted(usdt_tickers, key=lambda x: float(x['priceChangePercent']), reverse=True)

    # Get the highest gainer
    highest_gainer = len(sorted_tickers)

    return highest_gainer

def get_biggest_loser_by_id(x):
    # Fetch all the tickers for USDT futures
    tickers = client.futures_ticker()

    # Filter the tickers to only include USDT pairs
    usdt_tickers = [ticker for ticker in tickers if ticker['symbol'].endswith('USDT')]

    # Sort the tickers by the percentage change
    sorted_tickers = sorted(usdt_tickers, key=lambda x: float(x['priceChangePercent']), reverse=True)
    n = (get_total_coins())-2-x
    # Get the highest gainer
    highest_gainer = sorted_tickers[n]

    return highest_gainer

def get_support_resistance_levels(symbol, interval, limit=300):
    # client = binance.Client()  # Initialize the Binance client (ensure you have installed 'python-binance' library)
    
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)  # Fetch kline data
    
    close_prices = [float(kline[4]) for kline in klines]  # Extract close prices
    
    supports, resistances = [], []
    
    for i in range(2, len(close_prices)-2):
        is_support = close_prices[i] < close_prices[i-1] and close_prices[i] < close_prices[i+1] and close_prices[i] < close_prices[i-2] and close_prices[i] < close_prices[i+2]
        is_resistance = close_prices[i] > close_prices[i-1] and close_prices[i] > close_prices[i+1] and close_prices[i] > close_prices[i-2] and close_prices[i] > close_prices[i+2]
        
        if is_support:
            supports.append(close_prices[i])
        elif is_resistance:
            resistances.append(close_prices[i])

    return supports, resistances
