# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:55:25 2015

@author: ka
"""

from EuropeanOptions import *
from model.BlackScholesCalculator import *

bs = BlackScholesCalculator()


type = raw_input("Please input call/put: ")
stockPrice = raw_input("Stock price: ")
strike = raw_input("Strike: ")
volatility = raw_input("Volatility: ")
expiryYears = raw_input("Maturity in days: ")
riskfreeRate = raw_input("Risk Free Rate: ")

opt = EuropeanOptions(str(type), float(stockPrice), float(strike), float(volatility)/100.0, float(expiryYears)/252.0, float(riskfreeRate)/100.0)

value = bs.getValue(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "value of call:", value

delta = bs.getDelta(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "delta of call:", delta

theta = bs.getTheta(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "theta of call:", theta

rho = bs.getRho(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "rho of call:", rho

print

opt = EuropeanOptions("put", 100, 100, 0.3, 1, 0.02)

value = bs.getValue(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "value of put:", value

delta = bs.getDelta(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "delta of put:", delta

theta = bs.getTheta(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "theta of put:", theta

rho = bs.getRho(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "rho of put:", rho

print

gamma = bs.getGamma(opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "gamma:", gamma

vega = bs.getVega(opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "vega:", vega
