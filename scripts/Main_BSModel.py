# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:55:25 2015

@author: ka
"""

from entity.EuropeanOptions import *
from model.BlackScholesCalculator import *

bs = BlackScholesCalculator()

opt = EuropeanOptions("call", 100.0, 100.0, 0.35607, 1, 0.02)
value = bs.getValue(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "value of call:", value

delta = bs.getDelta(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "delta of call:", delta

theta = bs.getTheta(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "theta of call:", theta

rho = bs.getRho(opt.type, opt.stockPrice, opt.strike, opt.volatility, opt.expiryYears, opt.riskfreeRate)
print "rho of call:", rho

print

opt = EuropeanOptions("put", 100.0, 100.0, 0.35607, 1, 0.02)

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