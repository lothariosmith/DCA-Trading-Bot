import os
import time
from getIndicator import *
from emailAlert import *

#API_KEY = os.environ['']
#API_SECRET = os.environ['']

''' This is a Dollar Cost Average trading bot that notifies through email whether or not it's a good time to buy or sell by using the RSI indicator. Once you receive the email, you have to confirm the market order'''

# Variables 
checkRSI = True
sleepTime = 10000 # In seconds

from binance.client import Client

client = Client('ENTER API_KEY HERE', 'ENTER API_SECRET HERE')

# CONFIG
coin = 'ETH'
pairing = 'BUSD'
quantity = 0.057

# Functions
def buy_coin():
    return client.order_market_buy(
        symbol=coin+pairing ,
        quantity=quantity
    )

def sell_coin():
    return client.order_market_sell(
        symbol=coin+pairing ,
        quantity=quantity
    )

def mainBuy():
    while True:
        try:
            print("Buying Cryptoasset")
            buy_coin()
        except Exception as e:
            print(e)
        time.sleep(sleepTime)
        checkRSI = True

def mainSell():
    while True:
        try:
            print("Selling Cryptoasset")
            sell_coin()
        except Exception as e:
            print(e)
        time.sleep(sleepTime)
        checkRSI = True

def makeDecision():
    checkRSI = False
    answerOrder = input("Approve\nDisapprove\nContinue\nEnter Choice: ").upper()
    print(answerOrder)

    if rsiValue < 30:
        if answerOrder == "APPROVE":
            mainBuy()
        elif answerOrder == "DISAPPROVE":
            time.sleep(sleepTime)
            checkRSI = True
        elif answerOrder == "CONTINUE":
            time.sleep(sleepTime)
            checkRSI = True

    if rsiValue > 70:
        if answerOrder == "APPROVE":
            mainSell()
        elif answerOrder == "DISAPPROVE":
            time.sleep(sleepTime)
            checkRSI = True
        elif answerOrder == "CONTINUE":
            time.sleep(sleepTime)
            checkRSI = True



while checkRSI == True:
    global rsiValue
    rsiValue = ethereum.get_analysis().indicators["RSI"]
    print(rsiValue)

    if rsiValue < 30:
        print("Great Buy")
        market_notification("Approve/Disapprove/Continue", "Great Buying Opportunity, place order on PC", "bobx8291@gmail.com")
        makeDecision()
    elif rsiValue > 70:
        print("Great Sell")
        market_notification("Approve/Disapprove/Continue", "Great Selling Opportunity, place order on PC", "bobx8291@gmail.com")
        makeDecision()
    else:
        print("No Buying or Selling Opportunity")
    


#if __name__ == '__main__':
    #main()