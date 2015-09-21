# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:18:13 2015

@author: ka
"""

import pandas
from NewtonRaphson import *
from EuropeanOptions import *

nr = NewtonRaphson()

opt = EuropeanOptions("call", 209.78, 145.0, 0.2, 4.0 / 356.0, 0.02)
#vol = nr.calculateVolatility(64.8, opt.type, opt.stockPrice, opt.strike, opt.expiryYears, opt.riskfreeRate)
#print "implied volatility:", vol

opt = EuropeanOptions("put", 100.0, 100.0, 0.35607, 1, 0.02)
#vol = nr.calculateVolatility(15.0, opt.type, opt.stockPrice, opt.strike, opt.expiryYears, opt.riskfreeRate)
#print "implied volatility of put:", vol


def getStockPrice(x):
    return float(209.78)
    
def getRiskfreeRate(x):
    return float(0.02)

QuoteData= 'MarketData/' + 'SPY_OPT_20150216.csv'
data = pandas.io.parsers.read_csv(QuoteData, sep=',', header=0, na_values=' ')
data = data.fillna(0.0)

stockPrice = data.Symbol.apply(getStockPrice)
stockPrice.name = 'StockPrice'

riskfreeRate = data.Symbol.apply(getRiskfreeRate)
riskfreeRate.name = 'RiskfreeRate'

data = data.join(stockPrice).join(riskfreeRate)

print('Calculating Implied Vol of Options...')
impvol = pandas.Series(pandas.np.zeros(len(data.index)),
                           index=data.index, name='ImpliedVolatility')
for i in data.index:
    print i, ':', data.CallPut[i], data.SpotPrice[i], data.Strike[i], data.ExpiryDays[i]
    
    impvol[i] = (nr.calculateVolatility(data.SpotPrice[i],
                             data.CallPut[i].lower(),
                             data.StockPrice[i],
                             data.Strike[i],
                             float(data.ExpiryDays[i]) / 365.0, 
                             data.RiskfreeRate[i]))

print('Calculated Implied Vol for %d Options' % len(data.index))
data = data.join(impvol)

data.to_csv("Result_Data.csv")
print('Calculating Result has been saved to \"Result_Data.csv\"')
