# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:47:10 2020

@author: morte
"""

getOPG
#pumpdict wil contain PumpName (e.g. Pump1) and the GPIOin
pumpdict = dict()

pumpfile = open(r'./GPIOConfig.txt', 'r')

header = True
for line in pumpfile:
    if header:
        header = False
        continue
    PumpName, GPIOin = line.split(';')
    if GPIOin[-1] == '\n':
        GPIOin = GPIOin[:-1]
    GPIOin = int(GPIOin)
    pumpdict[PumpName] = GPIOin
pumpfile.close()
