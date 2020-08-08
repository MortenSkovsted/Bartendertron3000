# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:28:26 2020

@author: morte
"""
from gpiozero import LED
from pumpconfig import GetIngridentsPumpDict
import time





def GetDrinkList():

    drinksfile = open("drinks.txt")
    
    drinklist = []
    
    firstline = True
    for line in drinksfile:
        #remove newline
        if line[-1] == "\n":
            line = line[:-1]
        
        if firstline:
            firstline = False
            Drinksheader = line.split(";")

            continue
        info = line.split(";")
        drinklist.append(info)

    drinksfile.close()
    
    return drinklist


def GetActiveIngridents():
    
    ActiveIngridents = []
    
    pumpsfile = open("pumps.txt")
    firstline = True
    for line in pumpsfile:
        #remove newline, if there
        if line[-1] == "\n":
            line = line[:-1]
        
        if firstline:
            firstline = False
            pumpheader = line.split(";")

            continue
        temp = line.split(";")
        if temp[1] != "None":
            ActiveIngridents.append(temp[1])
    
    pumpsfile.close()

    return ActiveIngridents
        
def GetpumpGPIO():
    return None

def GetActiveDrinkslist():
    FullDrinksList = GetDrinkList()
    ActiveIngridents = GetActiveIngridents()
    
    ActiveDrinkList = []
    
    for drink in FullDrinksList:
        IngridentNames = drink[2:8]

        HaveAllIngrident = True
        for ingrident in IngridentNames:
            if ingrident != "None" and ingrident not in ActiveIngridents:
                HaveAllIngrident = False
        
        if HaveAllIngrident:
            ActiveDrinkList.append(drink)
    

    return ActiveDrinkList
print(GetActiveIngridents())
"""
Translate from this format:
[['0', 'Gin&Tonic', 'Gin', 'Tonic', 'None', 'None', 'None', 'None', '25', '50', 'None', 'None', 'None', 'None'],
['1', 'Rum&Tonic', 'Rum', 'Tonic', 'None', 'None', 'None', 'None', '25', '50', 'None', 'None', 'None', 'None']]
To this format

[Drink(0, "Gin&Tonic", ["Gin","Tonic"], [25,75]),
 Drink(1, "Rum&Cola", ["Rom","Cola"], [25,75]),
 Drink(2, "Old Fashioned", ["Rom","Sirup","Angostura Bitters"], [50,50,5])]
"""
def FinalDrinksList():
    UnformatedDrinkslist = GetActiveDrinkslist()
    
    
    #Test if there is only one available drink
    if type(UnformatedDrinkslist[0]) == str:
        ID = int(UnformatedDrinkslist[0])
        name = UnformatedDrinkslist[1]
        
        ingredients = []
        for ingredient in UnformatedDrinkslist[2:8]:
            if ingredient != "None":
                ingredients.append(ingredient)
                
        amounts = []
        for amount in UnformatedDrinkslist[8:]:
            if amount != "None":
                amounts.append(int(amount))
        
        return [ID, name, ingredients, amounts]
        
    
    elif type(UnformatedDrinkslist[0]) == list:
        formatedDrinkslist = []
        
        for drink in UnformatedDrinkslist:

            ID = int(drink[0])
            name = drink[1]
        
            ingredients = []
            for ingredient in drink[2:8]:
                if ingredient != "None":
                    ingredients.append(ingredient)
                
            amounts = []
            for amount in drink[8:]:
                if amount != "None":
                    amounts.append(int(amount))
        
            formatedDrinkslist.append([ID, name, ingredients, amounts])
        return formatedDrinkslist
            
        
    else:
        print(f"Error in FinalDrinksList, UnformatedDrinkslist is {UnformatedDrinkslist}")

def PourDrink(DrinkNameStr, pumpleddict):
    #The number of sec (130) it take to get 150ml
    ml_to_s_conversion = 130/150 #multiply with this factor
    
    DrinkAsList = FindDrinkFromActiveDrinks(DrinkNameStr)
    IngAndAmount = DrinkAsList[-2:]
    Amounts =[amount for amount, ingredient in sorted(zip(IngAndAmount[1],IngAndAmount[0]),reverse=True)]
    Ingredients =[ingredient for amount, ingredient in sorted(zip(IngAndAmount[1],IngAndAmount[0]),reverse=True)]

    #print(Amounts)
    #print(Ingredients)
    #Get GPIO pin that matches the ingredient
    pumpdict = GetIngridentsPumpDict()
    #start all pumps that will be used
    for ingrident in Ingredients:
        pumpname = pumpdict[ingrident][0]
        print(pumpname)
        #Get the pump object in the pump led dict
        #On is off and off is on... not logical
        pumpleddict[pumpname].off()
    
    #Stop pumps in reverse order (one with least to add stops first)
    waitingtime = 0
    for i in reversed(range(len(Ingredients))):
        #Stop in reverse order
        print(Ingredients[i])
        pumpname = pumpdict[Ingredients[i]][0]
        print(pumpname)
        temp = Amounts[i] * ml_to_s_conversion
        waitingtime = (Amounts[i] * ml_to_s_conversion) - waitingtime
        print(waitingtime)
        time.sleep(waitingtime)
        #pump = LED(led)
        #print(pumpleddict[pumpname])
        pumpleddict[pumpname].on()
        #pump.on()

        
        
    
    
def FindDrinkFromActiveDrinks(DrinkNameStr):
    drinks = FinalDrinksList()
    #return [ID, name, ingredients, amounts]
    # If only one possible drink and that is the chosen drink (it should be)
    if type(drinks[0]) == str and drinks[1] == DrinkNameStr:
        return drinks
    else:
        for drink in drinks:
            if drink[1] == DrinkNameStr:
                return drink


#Testing
"""
pumpdict = GetIngridentsPumpDict()
pumpleddict = {}
for pumpname, led in pumpdict.values():
    temp = LED(led)
    temp.on()
    pumpleddict[pumpname] = temp
"""
#print(pumpleddict)
#PourDrink('Rum&Tonic', pumpleddict)
#print(GetIngridentsPumpDict())

