# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:17:34 2015

@author: ka
"""

class EuropeanOptions:
    def __init__(self, type, stockPrice, strike, volatility, expiryYears, riskfreeRate):
        self.type = type        
        self.stockPrice = stockPrice
        self.strike = strike
        self.volatility = volatility
        self.expiryYears = expiryYears
        self.riskfreeRate = riskfreeRate
    
    
        