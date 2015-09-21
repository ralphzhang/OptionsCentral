# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 09:06:49 2015

@author: ka
"""

import sys
sys.dont_write_bytecode = True

import pandas

from model.BlackScholesCalculator import *

def getProfitValue(type, stockPrice, strike):
    if type == 'call':
        return max(stockPrice - strike, 0)
    else:
        return max(strike - stockPrice, 0)
        
            
def main():
    #PortfolioData= 'Strategy/' + 'Long Butterfly.csv'
    PortfolioData= '../Strategy/' + 'Bear Put Spread.csv'

    try:
        qd = open(PortfolioData, 'r')
        qd_head = []
        qd_head.append(qd.readline())
        qd_head.append(qd.readline())
        qd.close()
    except:
        sys.stderr.write("Usage: OptionStrategy.py PortfolioData.dat\n")
        sys.stderr.write("Couldn't read PortfolioData")
        sys.exit(1)

    bs = BlackScholesCalculator()

    first = qd_head[0].split(',')
    second = qd_head[1].split(',')

    stockPrice = float(first[1])
    riskfreeRate = float(first[2])
    optionStyle = first[3]
    
    daysFromToday = second[1]
    plVolatility = float(second[2])
    plRiskfreeRate = float(second[3])
    plMin = float(second[4])
    plMax = float(second[5])
    
    priceStep = (float(plMax) - float(plMin)) / 36.0

    data = pandas.io.parsers.read_csv(PortfolioData, sep=',', header=2, na_values=' ')
    print data.tail(9)

    plCurrent = plMin
    results = []
    
    while (plCurrent <= plMax):
        todayValue = 0
        expiryValue = 0
        
        totalPremium = 0
        
        for i in data.index:
            if data.Buy_Sell[i].lower() == 'sell':
                positionFactor = -1
            else:
                positionFactor = 1
                
            quantity = float(data.Quantity[i])

            totalPremium += float(data.Primium[i]) * positionFactor * quantity
                
            theTodayValue = bs.getValue(data.Buy_Sell[i].lower(), 
                                plCurrent, 
                                float(data.Strike[i]), 
                                plVolatility, 
                                float(data.ExpiryDays[i]) / 365.0, 
                                riskfreeRate)
                                
            theExpiryValue = getProfitValue(data.Buy_Sell[i].lower(), 
                                plCurrent, 
                                float(data.Strike[i]))
            
            todayValue += theTodayValue * positionFactor * quantity
            expiryValue += theExpiryValue * positionFactor * quantity
            
            print plCurrent, i, ':', theTodayValue, todayValue

        results.append(str(plCurrent) + ',' + \
            str(todayValue - totalPremium) + ',' + str(expiryValue - totalPremium))
        
        plCurrent += priceStep
        
    print results
        
    fo = open('../results/' + 'ResultOfPortfolio.csv', "wb")
    fo.write('Price,Today,At Expiry\n')
    for x in results:
        fo.write(str(x) + '\n');
    fo.close()

    
if __name__ == "__main__":
    main()
