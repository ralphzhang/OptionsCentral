# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:30:08 2015

@author: ka
"""

import math
from scipy.stats import norm

class BlackScholesCalculator:
    def getD1(self, stockPrice, strike, volatility, expiryYears, riskfreeRate):
        d1 = (math.log(stockPrice / strike, math.e) + (riskfreeRate + math.pow(volatility, 2) / 2.0) * expiryYears) / (volatility * math.sqrt(expiryYears));
        return d1
        
    def getD2(self, d1, volatility, expiryYears):
        d2 = d1 - volatility * math.sqrt(expiryYears)
        return d2
        
    def getValue(self, type, stockPrice, strike, volatility, expiryYears, riskfreeRate):
		d1 = self.getD1(stockPrice, strike, volatility, expiryYears, riskfreeRate);
		d2 = self.getD2(d1, volatility, expiryYears)
		if (type == "call"):
			premium = stockPrice * norm.cdf(d1) - strike * math.exp(-1 * riskfreeRate * expiryYears) * norm.cdf(d2);
		else:
			premium = strike * math.exp(-1 * riskfreeRate * expiryYears) * norm.cdf(-d2) - stockPrice * norm.cdf(-d1);
		
		return premium;
        
    def getDelta(self, type, stockPrice, strike, volatility, expiryYears, riskfreeRate):
		d1 = self.getD1(stockPrice, strike, volatility, expiryYears, riskfreeRate);
		if (type == "call"):
			delta = norm.cdf(d1)
		else:
			delta = -1 * norm.cdf(-d1)
   
		return delta;
  
    def getGamma(self, stockPrice, strike, volatility, expiryYears, riskfreeRate):
		d1 = self.getD1(stockPrice, strike, volatility, expiryYears, riskfreeRate)
		gamma = norm.pdf(d1) / (stockPrice * volatility * math.sqrt(expiryYears))
		return gamma;
  
    def getVega(self, stockPrice, strike, volatility, expiryYears, riskfreeRate):
		d1 = self.getD1(stockPrice, strike, volatility, expiryYears, riskfreeRate);
		vega = stockPrice * math.sqrt(expiryYears) * norm.pdf(d1);
		return vega;

    def getTheta(self, type, stockPrice, strike, volatility, expiryYears, riskfreeRate):
		d1 = self.getD1(stockPrice, strike, volatility, expiryYears, riskfreeRate);
		d2 = self.getD2(d1, volatility, expiryYears)
  		
		if (type == "call"):
			theta = -1 * stockPrice * norm.pdf(d1) * volatility / (2 * math.sqrt(expiryYears)) - \
                   riskfreeRate * strike * math.exp(-riskfreeRate * expiryYears) * norm.cdf(d2) 
		else:
			theta = -1 * stockPrice * norm.pdf(d1) * volatility / (2 * math.sqrt(expiryYears)) + \
                   riskfreeRate * strike * math.exp(-riskfreeRate * expiryYears) * norm.cdf(-d2) 
		
		return theta;
  
    def getRho(self, type, stockPrice, strike, volatility, expiryYears, riskfreeRate):
		d1 = self.getD1(stockPrice, strike, volatility, expiryYears, riskfreeRate);
		d2 = self.getD2(d1, volatility, expiryYears)
		if (type == "call"):
			rho = strike * expiryYears * math.exp(-riskfreeRate * expiryYears) * norm.cdf(d2)
		else:
			rho = -1 * strike * expiryYears * math.exp(-riskfreeRate * expiryYears) * norm.cdf(-d2)
		
		return rho;
