# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:47:10 2020

@author: morte
"""


def GetIngridentsPumpDict():
    pumplist = []
    GPIOfile = open('GPIOConfig.txt', 'r')
    header = True
    
    for line in GPIOfile:
        if header:
            header = False
            continue
        PumpName, GPIOPin = line.split(';')
        GPIOPin = int(GPIOPin)
        pumplist.append([PumpName, GPIOPin])
     
    GPIOfile.close()
    
    pumpfile = open('pumps.txt', 'r')
    header = True
    i = 0
    IngridientPumpDict = dict()
    
    for line in pumpfile:
        if header:
            header = False
            continue
        if line[-1] == '\n':
            line = line[:-1]
           
        PumpName, ingredient = line.split(';')
        if ingredient != 'None':
            IngridientPumpDict[ingredient] = pumplist[i]
            i += 1
    
    pumpfile.close()
    
    return IngridientPumpDict

