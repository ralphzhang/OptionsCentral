# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:38:11 2015

@author: ka
"""

from BlackScholesCalculator import *


class NewtonRaphson:
    
    def calculateVolatility(self, primium, type, stockPrice, strike, expiryYears, riskfreeRate):
        if stockPrice <= 0 or primium <= 0 or expiryYears <= 0:
            return 0
            
        bs = BlackScholesCalculator()

        loopVolatility = self.initVolatility(stockPrice, expiryYears, primium)

        prevVolatility = loopVolatility / 2.0
        loopPremium = bs.getValue(type, stockPrice, strike, prevVolatility, expiryYears, riskfreeRate)
        
        loop = 0
        while (1 == 1):
            loop += 1
            if loop > 1000: return -1
                
            newPrimium = bs.getValue(type, stockPrice, strike, loopVolatility, expiryYears, riskfreeRate)
            prevPrimium = loopPremium
            loopPrimium = newPrimium
            
            if newPrimium < 0.00001: return -1
            
            var1 = loopPrimium - primium
            
            if (abs(loopPrimium - primium) <= 0.01):
                return loopVolatility
            
            loopVega = bs.getVega(stockPrice, strike, loopVolatility, expiryYears, riskfreeRate)
            newVolatility = self.adjVolatility(loopVolatility, loopPrimium, loopVega, prevVolatility, prevPrimium, primium)
            prevVolatility = loopVolatility
            loopVolatility = newVolatility
        
        
    def initVolatility(self, stockPrice, expiryYears, primium):
        initVol = math.sqrt(2 * math.pi / expiryYears) * primium / stockPrice
        return initVol;
        
    def adjVolatility(self, loopVolatility, loopPrimium, loopVega, prevVolatility, prevPrimium, primium):
        if (abs(loopVega) >= 0.0001):
            newVol = loopVolatility - (loopPrimium - primium) / loopVega
        else:
            newVol = loopVolatility - \
                (loopPrimium - primium) * (loopVolatility - prevVolatility) / (loopPrimium - prevPrimium)
            
        return newVol
        
        
        
